"""Public, deterministic game-session API.

This module plays the role Godot will play later: it runs the mundane world, asks the
consensus kernel to rule on the events that laws subscribe to, and commits whatever the
kernel returns. It is the only place where an adjudicated outcome becomes world fact.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .actions import InvalidAction, prepare
from .adjudicate import adjudicate
from .campaign import initial_state


def new_game(campaign: dict[str, Any], *, arete: int = 2, seed: int = 1) -> dict[str, Any]:
    return initial_state(campaign, arete=arete, seed=seed)


def _commit(
    state: dict[str, Any],
    request: dict[str, Any],
    resolution: dict[str, Any],
    result: dict[str, Any],
) -> None:
    """Write an adjudicated outcome into the world. Keys prefixed ``_`` stay internal."""
    target = state["entities"].get(request["event"].get("target"))
    if target is not None:
        for key, value in resolution["outcome"].items():
            if not key.startswith("_"):
                target[key] = value

    for signature, amount in resolution["heat"].items():
        state["heat"]["local"] += amount
        state["heat"]["personal"] += amount
        signatures = state["heat"]["signatures"]
        signatures[signature] = signatures.get(signature, 0) + amount
    for signature in resolution["advisories"]:
        if signature not in state["advisories"]:
            state["advisories"].append(signature)
    for signature in resolution["patches"]:
        if signature not in state["patches"]:
            state["patches"].append(signature)

    result["observations"].extend(resolution["observations"])
    result["signals"].extend(resolution["signals"])
    result["fired_rules"].extend(resolution["fired_rules"])
    result["anomaly"] = result["anomaly"] or resolution["anomaly"]
    if resolution["fired_rules"]:
        result["status"] = resolution["status"]


def act(
    state: dict[str, Any],
    action: dict[str, Any],
    campaign: dict[str, Any],
    *,
    seed: int | None = None,
) -> dict[str, Any]:
    """Resolve one action without mutating the supplied state.

    ``seed`` is explicit in the API even though the first slice contains no random laws.
    That makes determinism a contract before randomness is introduced.
    """
    next_state = deepcopy(state)
    if seed is not None:
        next_state["seed"] = seed
    result: dict[str, Any] = {
        "status": "succeeded",
        "observations": [],
        "signals": [],
        "anomaly": False,
        "fired_rules": [],
    }
    try:
        for request in prepare(next_state, action, result):
            _commit(next_state, request, adjudicate(request, campaign), result)
    except InvalidAction as exc:
        return {
            "state": state,
            "public": {
                "status": "invalid",
                "observations": [str(exc)],
                "signals": [],
                "anomaly": False,
            },
            "gm": {"fired_rules": []},
        }

    if action.get("verb") == "open" and not result["observations"]:
        door = next_state["entities"][action["target"]]
        result["observations"].append(f"{door['name']} opens.")

    history_entry = {
        "tick": next_state["tick"],
        "action": deepcopy(action),
        "status": result["status"],
        "anomaly": result["anomaly"],
    }
    next_state["history"].append(history_entry)
    public = {key: result[key] for key in ("status", "observations", "signals", "anomaly")}
    return {
        "state": next_state,
        "public": public,
        "gm": {"fired_rules": result["fired_rules"], "seed": next_state["seed"]},
    }


def describe(state: dict[str, Any]) -> dict[str, Any]:
    """Return player-safe, factual scene state (never seam metadata)."""
    player_location = state["entities"]["player"]["location"]
    visible = []
    for entity_id, entity in state["entities"].items():
        if entity_id == "player" or entity.get("location") != player_location or entity.get("concealed"):
            continue
        details = []
        if entity.get("kind") == "door":
            details.extend(["locked" if entity.get("locked") else "unlocked", "open" if entity.get("open") else "closed"])
        if entity.get("fragile"):
            details.append("intact" if entity.get("intact") else "broken")
        visible.append({"id": entity_id, "name": entity["name"], "details": details})
    return {
        "location": player_location,
        "objective": state["objective"],
        "visible": visible,
        "local_heat": state["heat"]["local"],
    }
