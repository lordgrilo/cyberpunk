"""Campaign data loading.

The v0 files use JSON syntax inside ``.yaml`` files. JSON is valid YAML, which lets the
prototype remain dependency-free while preserving the eventual content format.
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any


def _read_yaml(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"{path} must currently use JSON-shaped YAML (the zero-dependency v0 subset)"
        ) from exc


def load_campaign(path: str | Path) -> dict[str, Any]:
    root = Path(path)
    campaign = _read_yaml(root / "scene.yaml")
    campaign["rules"] = _read_yaml(root / "laws.yaml")["rules"]
    campaign["seams"] = _read_yaml(root / "seams.yaml")["seams"]
    campaign["path"] = str(root)
    return campaign


def initial_state(campaign: dict[str, Any], *, arete: int = 2, seed: int = 1) -> dict[str, Any]:
    return {
        "campaign": campaign["id"],
        "venue": campaign["venue"],
        "objective": campaign["objective"],
        "tick": 0,
        "seed": seed,
        "arete": arete,
        "entities": deepcopy(campaign["entities"]),
        "pending": [],
        "heat": {"local": 0, "personal": 0, "signatures": {}},
        "advisories": [],
        "patches": [],
        "history": [],
    }

