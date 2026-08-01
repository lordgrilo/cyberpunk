"""Human play shell and JSON adapter for an AI game master."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from copy import deepcopy
from typing import Any

from .engine.campaign import load_campaign
from .engine.session import act, describe, new_game


DEFAULT_CAMPAIGN = Path(__file__).parent / "campaigns" / "v0-hotel"


def _render_view(view: dict[str, Any]) -> None:
    print(f"\n{view['location'].replace('_', ' ').title()}")
    print(f"Objective: {view['objective']}")
    for entity in view["visible"]:
        details = f" ({', '.join(entity['details'])})" if entity["details"] else ""
        print(f"  {entity['id']}: {entity['name']}{details}")
    print(f"Local heat: {view['local_heat']}")


def _render_result(result: dict[str, Any]) -> None:
    for line in result["public"]["observations"]:
        print(line)
    for signal in result["public"]["signals"]:
        print(f"  ✦ {signal}")


def _parse_command(line: str) -> dict[str, Any] | None:
    words = line.strip().split()
    if not words:
        return None
    verb = words[0].lower()
    # GM-only state transitions for NPCs. These use the same mundane engine actions as
    # the player; they merely name a different actor and are intentionally absent from
    # the player-facing help text.
    if verb == "gm" and len(words) >= 2:
        gm_verb = words[1].lower()
        if gm_verb == "move" and len(words) == 4:
            return {"verb": "move", "actor": words[2], "destination": words[3]}
        if gm_verb == "give" and len(words) == 5:
            return {
                "verb": "give",
                "actor": words[2],
                "target": words[3],
                "recipient": words[4],
            }
        if gm_verb == "observe" and len(words) == 4:
            return {"verb": "observe", "actor": words[2], "target": words[3]}
        raise ValueError("Invalid GM transition.")
    if verb == "open" and len(words) == 2:
        return {"verb": "open", "target": words[1]}
    if verb == "close" and len(words) == 2:
        return {"verb": "close", "target": words[1]}
    if verb == "take" and len(words) == 2:
        return {"verb": "take", "target": words[1]}
    if verb == "conceal" and len(words) in {3, 4}:
        action: dict[str, Any] = {"verb": "conceal", "target": words[1], "observer": words[2]}
        if len(words) == 4:
            action["using"] = words[3]
        return action
    if verb == "observe" and len(words) == 2:
        return {"verb": "observe", "target": words[1]}
    if verb == "listen" and len(words) == 2:
        return {"verb": "observe", "target": words[1], "mode": "listen"}
    if verb == "drop" and len(words) in {2, 3}:
        action = {"verb": "drop", "target": words[1]}
        if len(words) == 3:
            action["height"] = int(words[2])
        return action
    if verb in {"say", "utter"} and len(words) >= 3:
        target, claimed_state = words[1], words[2]
        return {
            "verb": "utter",
            "words": f"{target} is {claimed_state}",
            "claim": {"target": target, "state": claimed_state},
        }
    if verb == "speak" and len(words) >= 2:
        return {"verb": "utter", "words": " ".join(words[1:])}
    if verb in {"wait", "time"}:
        return {"verb": "wait", "amount": int(words[1]) if len(words) > 1 else 1}
    if verb == "move" and len(words) == 2:
        return {"verb": "move", "destination": words[1]}
    if verb == "place" and len(words) in {3, 4}:
        action = {"verb": "place", "target": words[1], "destination": words[2]}
        if len(words) == 4:
            action["height"] = int(words[3])
        return action
    if verb == "touch" and len(words) == 2:
        return {"verb": "touch", "target": words[1]}
    if verb == "knock" and len(words) == 2:
        return {"verb": "touch", "target": words[1], "manner": "knock"}
    if verb == "give" and len(words) == 3:
        return {"verb": "give", "target": words[1], "recipient": words[2]}
    raise ValueError("I could not parse that action. Type help for the compact command list.")


def play(campaign_path: Path, arete: int) -> None:
    campaign = load_campaign(campaign_path)
    state = new_game(campaign, arete=arete)
    print("CONSENSUS — The Service Corridor")
    print("There is no cast command. Observe, interfere, and form a theory.")
    _render_view(describe(state))
    while True:
        try:
            line = input("\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if line in {"quit", "exit"}:
            return
        if line == "gm refresh":
            refreshed = load_campaign(campaign_path)
            for entity_id, entity in refreshed["entities"].items():
                state["entities"].setdefault(entity_id, deepcopy(entity))
            state["venue"] = deepcopy(refreshed["venue"])
            campaign = refreshed
            print("Campaign content refreshed; existing state preserved.")
            continue
        if line in {"look", "status"}:
            _render_view(describe(state))
            continue
        if line == "help":
            print("open/close/take THING | conceal THING OBSERVER [USING] | observe THING | drop THING [HEIGHT]")
            print("say THING STATE | wait [BEATS] | place THING LOCATION [HEIGHT] | move LOCATION | quit")
            continue
        try:
            action = _parse_command(line)
        except (ValueError, IndexError) as exc:
            print(exc)
            continue
        if action is None:
            continue
        resolution = act(state, action, campaign)
        state = resolution["state"]
        _render_result(resolution)


def json_action(campaign_path: Path, payload: str) -> None:
    request = json.loads(payload)
    campaign = load_campaign(campaign_path)
    state = request.get("state") or new_game(campaign, arete=request.get("arete", 2), seed=request.get("seed", 1))
    resolution = act(state, request["action"], campaign, seed=request.get("seed"))
    print(json.dumps(resolution, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser(description="Play or drive CONSENSUS")
    parser.add_argument("--campaign", type=Path, default=DEFAULT_CAMPAIGN)
    subparsers = parser.add_subparsers(dest="command")
    play_parser = subparsers.add_parser("play")
    play_parser.add_argument("--arete", type=int, choices=range(2, 4), default=2)
    json_parser = subparsers.add_parser("json")
    json_parser.add_argument("payload")
    args = parser.parse_args()
    if args.command in {None, "play"}:
        play(args.campaign, getattr(args, "arete", 2))
    else:
        json_action(args.campaign, args.payload)


if __name__ == "__main__":
    main()
