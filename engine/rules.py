"""Generic condition matching.

This module knows how to combine and compare facts. It deliberately does not know what
any fact means; the caller supplies a resolver. That separation is what lets one matcher
serve the consensus kernel without the kernel gaining a world model.
"""

from __future__ import annotations

from typing import Any, Callable


MISSING = object()


def walk(value: Any, path: list[str]) -> Any:
    for part in path:
        if not isinstance(value, dict) or part not in value:
            return MISSING
        value = value[part]
    return value


def matches(condition: dict[str, Any], resolve: Callable[[str], Any]) -> bool:
    if "all" in condition:
        return all(matches(item, resolve) for item in condition["all"])
    if "any" in condition:
        return any(matches(item, resolve) for item in condition["any"])
    if "not" in condition:
        return not matches(condition["not"], resolve)

    actual = resolve(condition["fact"])
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
