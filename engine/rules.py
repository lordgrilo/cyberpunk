"""Small data-driven condition/effect rule evaluator."""

from __future__ import annotations

from typing import Any


MISSING = object()


def _walk(value: Any, path: list[str]) -> Any:
    for part in path:
        if not isinstance(value, dict) or part not in value:
            return MISSING
        value = value[part]
    return value


def fact(state: dict[str, Any], event: dict[str, Any], name: str) -> Any:
    """Resolve the deliberately small fact vocabulary exposed to campaign data."""
    parts = name.split(".")
    root = parts.pop(0)
    if root == "event":
        return _walk(event, parts)
    if root in {"target", "actor"}:
        entity_id = event.get(root)
        return _walk(state["entities"].get(entity_id, {}), parts)
    if root == "world":
        return _walk(state, parts)
    if root == "patch":
        return ".".join(parts) in state["patches"]
    if root == "observer_count":
        target = event.get("target")
        target_location = state["entities"].get(target, {}).get("location")
        requested_kind = parts[0] if parts else "any"
        count = 0
        for entity_id, entity in state["entities"].items():
            if entity_id == event.get("actor"):
                continue
            if entity.get("location") != target_location:
                continue
            if target not in entity.get("observing", []):
                continue
            if target in entity.get("cannot_see", []):
                continue
            if not entity.get("awake", True):
                continue
            if requested_kind != "any" and entity.get("kind") != requested_kind:
                continue
            count += 1
        return count
    raise ValueError(f"unknown campaign fact: {name}")


def matches(state: dict[str, Any], event: dict[str, Any], condition: dict[str, Any]) -> bool:
    if "all" in condition:
        return all(matches(state, event, item) for item in condition["all"])
    if "any" in condition:
        return any(matches(state, event, item) for item in condition["any"])
    if "not" in condition:
        return not matches(state, event, condition["not"])

    actual = fact(state, event, condition["fact"])
    if "exists" in condition:
        return (actual is not MISSING) is bool(condition["exists"])
    if actual is MISSING:
        return False
    for operator in ("eq", "ne", "gt", "gte", "lt", "lte", "contains"):
        if operator not in condition:
            continue
        expected = condition[operator]
        if operator == "eq":
            return actual == expected
        if operator == "ne":
            return actual != expected
        if operator == "gt":
            return actual > expected
        if operator == "gte":
            return actual >= expected
        if operator == "lt":
            return actual < expected
        if operator == "lte":
            return actual <= expected
        return expected in actual
    raise ValueError(f"condition has no supported comparison: {condition}")


def _set_path(state: dict[str, Any], event: dict[str, Any], path: str, value: Any) -> None:
    parts = path.split(".")
    root = parts.pop(0)
    if root == "event":
        destination = event
    elif root in {"target", "actor"}:
        destination = state["entities"][event[root]]
    elif root == "world":
        destination = state
    else:
        raise ValueError(f"unsupported effect destination: {root}")
    for part in parts[:-1]:
        destination = destination.setdefault(part, {})
    destination[parts[-1]] = value


def _add_heat(
    state: dict[str, Any],
    event: dict[str, Any],
    effect: dict[str, Any],
    campaign: dict[str, Any],
    result: dict[str, Any],
) -> None:
    amount = int(effect.get("amount", 1))
    signature = effect["signature"]
    state["heat"]["local"] += amount
    state["heat"]["personal"] += amount
    signatures = state["heat"]["signatures"]
    signatures[signature] = signatures.get(signature, 0) + amount
    result["anomaly"] = True

    seam = campaign["seams"][signature]
    current = signatures[signature]
    if current >= seam["advisory_at"] and signature not in state["advisories"]:
        state["advisories"].append(signature)
        result["observations"].append(seam["advisory"])
    if current >= seam["patch_at"] and signature not in state["patches"]:
        state["patches"].append(signature)
        result["observations"].append(seam["patch_notice"])


def apply_rules(
    state: dict[str, Any],
    event: dict[str, Any],
    campaign: dict[str, Any],
    result: dict[str, Any],
) -> None:
    rules = sorted(campaign["rules"], key=lambda rule: (rule["priority"], rule["id"]))
    for rule in rules:
        if rule["trigger"] != event["type"]:
            continue
        if not matches(state, event, rule.get("when", {"all": []})):
            continue

        result["fired_rules"].append(rule["id"])
        instrument = rule.get("instrument", {})
        arete = state["arete"]
        if arete >= 2 and instrument.get("arete2"):
            result["signals"].append(instrument["arete2"])
        if arete >= 3 and instrument.get("arete3"):
            result["signals"].append(instrument["arete3"])

        for effect in rule.get("effects", []):
            operation = effect["op"]
            if operation == "set":
                _set_path(state, event, effect["path"], effect["value"])
            elif operation == "outcome":
                result["status"] = effect.get("status", result["status"])
                result["observations"].append(effect["message"])
            elif operation == "heat":
                _add_heat(state, event, effect, campaign, result)
            else:
                raise ValueError(f"unsupported rule effect: {operation}")
