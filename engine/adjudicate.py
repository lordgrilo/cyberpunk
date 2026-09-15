"""The consensus kernel: the sole authority on whether an account becomes reality.

The kernel is a pure function of a self-describing request. It performs no raycasts,
owns no entities, and reads no world store. Whoever simulates the world -- the text
engine today, Godot later -- must supply the witness snapshot and the proposed outcome.

Request shape::

    {
      "event":     {"type": "open", "actor": "player", "target": "service_door"},
      "subject":   {"kind": "door", "access_state": "locked"},
      "proposal":  {"open": true},
      "witnesses": [{"observer": "porter", "modality": "direct_sight"}],
      "consensus": {"arete": 2, "patches": [], "advisories": [], "signatures": {}}
    }

Fact vocabulary available to campaign data:

``event.*``            fields of the event being adjudicated
``subject.*``          supplied claims about the entity acted upon
``proposal.*``         the outcome under adjudication, as amended so far
``witness_count.X``    number of supplied witnesses of modality ``X`` (``any`` for all)
``patch.SEAM``         whether that seam has been patched
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from .rules import MISSING, matches, walk


def _resolver(context: dict[str, Any]):
    def resolve(name: str) -> Any:
        parts = name.split(".")
        root = parts.pop(0)
        if root in {"event", "subject", "proposal"}:
            return walk(context[root], parts)
        if root == "patch":
            return ".".join(parts) in context["consensus"].get("patches", [])
        if root == "witness_count":
            modality = parts[0] if parts else "any"
            witnesses = context["witnesses"]
            if modality == "any":
                return len(witnesses)
            return sum(1 for witness in witnesses if witness.get("modality") == modality)
        raise ValueError(f"unknown campaign fact: {name}")

    return resolve


def _set(proposal: dict[str, Any], path: str, value: Any) -> None:
    parts = path.split(".")
    if parts.pop(0) != "proposal":
        raise ValueError(f"the kernel may only amend the proposal, not {path!r}")
    destination = proposal
    for part in parts[:-1]:
        destination = destination.setdefault(part, {})
    destination[parts[-1]] = value


def _heat(effect: dict[str, Any], campaign: dict[str, Any], context, result) -> None:
    signature = effect["signature"]
    amount = int(effect.get("amount", 1))
    result["heat"][signature] = result["heat"].get(signature, 0) + amount
    result["anomaly"] = True

    consensus = context["consensus"]
    seam = campaign["seams"][signature]
    total = consensus.get("signatures", {}).get(signature, 0) + result["heat"][signature]
    known_patches = list(consensus.get("patches", []))
    known_advisories = list(consensus.get("advisories", []))
    if total >= seam["advisory_at"] and signature not in known_advisories + result["advisories"]:
        result["advisories"].append(signature)
        result["observations"].append(seam["advisory"])
    if total >= seam["patch_at"] and signature not in known_patches + result["patches"]:
        result["patches"].append(signature)
        result["observations"].append(seam["patch_notice"])


def adjudicate(request: dict[str, Any], campaign: dict[str, Any]) -> dict[str, Any]:
    """Resolve one event against the consensus rulebase. The request is never mutated."""
    context = {
        "event": request.get("event", {}),
        "subject": request.get("subject", {}),
        "proposal": deepcopy(request.get("proposal", {})),
        "witnesses": request.get("witnesses", []),
        "consensus": request.get("consensus", {}),
    }
    resolve = _resolver(context)
    arete = int(context["consensus"].get("arete", 0))
    result: dict[str, Any] = {
        "status": "succeeded",
        "outcome": context["proposal"],
        "observations": [],
        "signals": [],
        "anomaly": False,
        "fired_rules": [],
        "heat": {},
        "advisories": [],
        "patches": [],
    }

    trigger = context["event"].get("type")
    for rule in sorted(campaign["rules"], key=lambda rule: (rule["priority"], rule["id"])):
        if rule["trigger"] != trigger:
            continue
        if not matches(rule.get("when", {"all": []}), resolve):
            continue

        result["fired_rules"].append(rule["id"])
        instrument = rule.get("instrument", {})
        for tier in range(2, arete + 1):
            signal = instrument.get(f"arete{tier}")
            if signal:
                result["signals"].append(signal)

        for effect in rule.get("effects", []):
            operation = effect["op"]
            if operation == "set":
                _set(context["proposal"], effect["path"], effect["value"])
            elif operation == "outcome":
                result["status"] = effect.get("status", result["status"])
                result["observations"].append(effect["message"])
            elif operation == "heat":
                _heat(effect, campaign, context, result)
            else:
                raise ValueError(f"unsupported rule effect: {operation}")

    return result
