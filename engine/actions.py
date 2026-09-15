"""The mundane action surface. No spell-casting verb exists."""

from __future__ import annotations

from typing import Any

from .worldmodel import request_for


VERBS = {
    "move",
    "place",
    "conceal",
    "drop",
    "open",
    "close",
    "take",
    "utter",
    "observe",
    "wait",
    "touch",
    "give",
    "time",
}


class InvalidAction(ValueError):
    pass


def _entity(state: dict[str, Any], entity_id: str | None) -> dict[str, Any]:
    if not entity_id or entity_id not in state["entities"]:
        raise InvalidAction(f"unknown entity: {entity_id!r}")
    return state["entities"][entity_id]


def prepare(
    state: dict[str, Any], action: dict[str, Any], result: dict[str, Any]
) -> list[dict[str, Any]]:
    """Apply mundane state changes and return adjudication requests."""
    verb = action.get("verb")
    if verb not in VERBS:
        raise InvalidAction(f"verb must be one of: {', '.join(sorted(VERBS))}")

    actor_id = action.get("actor", "player")
    actor = _entity(state, actor_id)
    target_id = action.get("target")
    requests: list[dict[str, Any]] = []

    if verb == "open":
        target = _entity(state, target_id)
        if "open" not in target:
            raise InvalidAction(f"{target_id} is not something that opens")
        if target.get("open"):
            result["observations"].append(f"{target['name']} is already open.")
            result["status"] = "unchanged"
            return []
        if target.get("kind") == "door":
            # A threshold is consensus-governed: propose the opening, never commit it.
            requests.append(
                request_for(
                    state,
                    {"type": "open", "actor": actor_id, "target": target_id},
                    proposal={"open": True},
                )
            )
        else:
            target["open"] = True
            for contained_id in target.get("contains", []):
                contained = state["entities"].get(contained_id)
                if contained:
                    contained["concealed"] = False
            if target.get("on_open"):
                result["observations"].append(target["on_open"])

    elif verb == "close":
        target = _entity(state, target_id)
        if "open" not in target:
            raise InvalidAction(f"{target_id} is not something that closes")
        if not target["open"]:
            result["observations"].append(f"{target['name']} is already closed.")
            result["status"] = "unchanged"
            return []
        target["open"] = False
        result["observations"].append(f"You close {target['name']}.")

    elif verb == "take":
        target = _entity(state, target_id)
        if not target.get("portable"):
            raise InvalidAction(f"{target_id} cannot be taken")
        target["owner"] = actor_id
        target["carried_by"] = actor_id
        target["location"] = actor["location"]
        result["observations"].append(f"You take {target['name']}.")

    elif verb == "conceal":
        _entity(state, target_id)
        observer_id = action.get("observer")
        observer = _entity(state, observer_id)
        if target_id not in observer.setdefault("cannot_see", []):
            observer["cannot_see"].append(target_id)
        using = action.get("using")
        suffix = f" with {state['entities'][using]['name']}" if using in state["entities"] else ""
        result["observations"].append(
            f"You conceal {state['entities'][target_id]['name']} from {observer['name']}{suffix}."
        )

    elif verb == "observe":
        target = _entity(state, target_id)
        observing = actor.setdefault("observing", [])
        if target_id not in observing:
            observing.append(target_id)
        if target_id in actor.setdefault("cannot_see", []):
            actor["cannot_see"].remove(target_id)
        mode = action.get("mode", "observe")
        detail = target.get(mode) or target.get("examine")
        if detail:
            result["observations"].append(detail)
        else:
            result["observations"].append(f"{actor['name']} watches {target['name']}.")

    elif verb == "drop":
        target = _entity(state, target_id)
        if not target.get("portable"):
            raise InvalidAction(f"{target_id} cannot be dropped")
        height = int(action.get("height", target.get("height", 1)))
        target["location"] = actor["location"]
        target["height"] = 0
        state["pending"].append(
            {
                "type": "fall_settlement",
                "actor": actor_id,
                "target": target_id,
                "height": height,
                "due": state["tick"] + 1,
            }
        )
        result["observations"].append(
            f"{target['name']} strikes the tile with a sharp, strangely unresolved crack."
        )

    elif verb == "utter":
        words = action.get("words", "")
        claim = action.get("claim")
        if claim:
            claim_target = claim.get("target")
            _entity(state, claim_target)
            for pending in reversed(state["pending"]):
                if pending["target"] == claim_target and "claim" not in pending:
                    pending["claim"] = {
                        "state": claim.get("state"),
                        "speaker": actor_id,
                    }
                    break
        result["observations"].append(f'{actor["name"]} says, “{words}”')

    elif verb in {"wait", "time"}:
        amount = max(1, int(action.get("amount", 1)))
        state["tick"] += amount
        due, future = [], []
        for pending in state["pending"]:
            (due if pending["due"] <= state["tick"] else future).append(pending)
        state["pending"] = future
        for settlement in due:
            requests.append(request_for(state, settlement, proposal={"_stabilized": False}))
        if not due:
            result["observations"].append("A quiet beat passes.")

    elif verb == "move":
        destination = action.get("destination")
        if destination not in state["venue"]["locations"]:
            raise InvalidAction(f"unknown location: {destination!r}")
        actor["location"] = destination
        for entity in state["entities"].values():
            if entity.get("carried_by") == actor_id:
                entity["location"] = destination
        result["observations"].append(f"{actor['name']} moves to {destination.replace('_', ' ')}.")

    elif verb == "place":
        target = _entity(state, target_id)
        destination = action.get("destination", actor["location"])
        target["location"] = destination
        target.pop("carried_by", None)
        if "height" in action:
            target["height"] = int(action["height"])
        result["observations"].append(f"{target['name']} is placed at {destination.replace('_', ' ')}.")

    elif verb == "give":
        target = _entity(state, target_id)
        recipient_id = action.get("recipient")
        recipient = _entity(state, recipient_id)
        target["owner"] = recipient_id
        target["location"] = recipient["location"]
        requests.append(
            request_for(
                state,
                {"type": "give", "actor": actor_id, "target": target_id, "recipient": recipient_id},
            )
        )

    elif verb == "touch":
        target = _entity(state, target_id)
        if action.get("manner") != "knock" and target.get("examine"):
            result["observations"].append(target["examine"])
        requests.append(
            request_for(
                state,
                {
                    "type": "touch",
                    "actor": actor_id,
                    "target": target_id,
                    "manner": action.get("manner", "touch"),
                },
            )
        )

    return requests
