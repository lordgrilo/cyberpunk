"""The world model: everything the consensus kernel is forbidden to know.

Today these functions read the text engine's entity dictionary. In Godot the same
questions are answered by navigation, raycasts and device state. Neither side changes
the other, because the kernel request shape is the contract between them.
"""

from __future__ import annotations

from typing import Any


#: How an observer's nature becomes the modality of the evidence it produces.
MODALITY_BY_KIND = {"human": "direct_sight", "device": "optical_record"}


def witnesses_of(state: dict[str, Any], target_id: str, *, exclude: str | None = None) -> list[dict[str, str]]:
    """Snapshot who is actually observing ``target_id`` right now.

    A sleeping guard or an occluded camera simply does not appear. The kernel therefore
    never reasons about wakefulness or sightlines; it only counts what it was handed.
    """
    location = state["entities"].get(target_id, {}).get("location")
    witnesses = []
    for observer_id, observer in state["entities"].items():
        if observer_id == exclude or observer.get("location") != location:
            continue
        if target_id not in observer.get("observing", []):
            continue
        if target_id in observer.get("cannot_see", []) or not observer.get("awake", True):
            continue
        modality = MODALITY_BY_KIND.get(observer.get("kind"))
        if modality:
            witnesses.append({"observer": observer_id, "modality": modality})
    return witnesses


def subject_claims(entity: dict[str, Any]) -> dict[str, Any]:
    """Describe the acted-upon entity as claims, not as an entity reference."""
    claims: dict[str, Any] = {"kind": entity.get("kind")}
    if "locked" in entity:
        claims["access_state"] = "locked" if entity["locked"] else "unlocked"
    if "fragile" in entity:
        claims["fragile"] = entity["fragile"]
    return claims


def consensus_snapshot(state: dict[str, Any]) -> dict[str, Any]:
    return {
        "arete": state["arete"],
        "patches": list(state["patches"]),
        "advisories": list(state["advisories"]),
        "signatures": dict(state["heat"]["signatures"]),
    }


def request_for(state: dict[str, Any], event: dict[str, Any], *, proposal: dict[str, Any] | None = None) -> dict[str, Any]:
    """Assemble one self-describing adjudication request."""
    target_id = event.get("target")
    return {
        "event": event,
        "subject": subject_claims(state["entities"].get(target_id, {})),
        "proposal": dict(proposal or {}),
        "witnesses": witnesses_of(state, target_id, exclude=event.get("actor")),
        "consensus": consensus_snapshot(state),
    }
