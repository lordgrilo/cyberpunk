"""Public, deterministic game-session API."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .actions import InvalidAction, prepare
from .campaign import initial_state
from .rules import apply_rules


def new_game(campaign: dict[str, Any], *, arete: int = 2, seed: int = 1) -> dict[str, Any]:
    return initial_state(campaign, arete=arete, seed=seed)


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
        events = prepare(next_state, action, result)
        for event in events:
            apply_rules(next_state, event, campaign, result)
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
