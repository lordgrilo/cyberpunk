"""Gate 0 contract: the consensus kernel resolves events from a supplied snapshot.

These cases are frozen. The future GDScript kernel must reproduce them exactly, so
they are stored as language-neutral JSON rather than as Python literals.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from consensus.engine.adjudicate import adjudicate
from consensus.engine.campaign import load_campaign


ROOT = Path(__file__).parents[1]
CAMPAIGN_PATH = ROOT / "campaigns" / "v0-hotel"
GOLDEN_PATH = Path(__file__).parent / "golden" / "threshold-seam.json"


class ThresholdSeamGoldenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.campaign = load_campaign(CAMPAIGN_PATH)
        cls.golden = json.loads(GOLDEN_PATH.read_text(encoding="utf-8"))

    def test_every_golden_case_resolves_exactly(self):
        for case in self.golden["cases"]:
            with self.subTest(case=case["name"]):
                resolution = adjudicate(case["request"], self.campaign)
                expected = case["expect"]
                self.assertEqual(expected["status"], resolution["status"])
                self.assertEqual(expected["outcome"], resolution["outcome"])
                self.assertEqual(expected["anomaly"], resolution["anomaly"])
                self.assertEqual(expected["fired_rules"], resolution["fired_rules"])
                self.assertEqual(expected["heat"], resolution["heat"])

    def test_adjudication_does_not_mutate_the_request(self):
        case = self.golden["cases"][0]
        before = json.dumps(case["request"], sort_keys=True)
        adjudicate(case["request"], self.campaign)
        self.assertEqual(before, json.dumps(case["request"], sort_keys=True))

    def test_arete_gates_instrumentation_depth(self):
        request = json.loads(json.dumps(self.golden["cases"][0]["request"]))
        request["consensus"]["arete"] = 1
        self.assertEqual([], adjudicate(request, self.campaign)["signals"])
        request["consensus"]["arete"] = 2
        self.assertEqual(1, len(adjudicate(request, self.campaign)["signals"]))
        request["consensus"]["arete"] = 3
        self.assertEqual(2, len(adjudicate(request, self.campaign)["signals"]))
