from __future__ import annotations

import unittest
from pathlib import Path

from consensus.engine.campaign import load_campaign
from consensus.engine.session import act, new_game


CAMPAIGN_PATH = Path(__file__).parents[1] / "campaigns" / "v0-hotel"


class RealityEngineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.campaign = load_campaign(CAMPAIGN_PATH)

    def setUp(self) -> None:
        self.state = new_game(self.campaign)

    def resolve(self, action):
        resolution = act(self.state, action, self.campaign)
        self.state = resolution["state"]
        return resolution

    def test_witnessed_locked_door_holds(self):
        result = self.resolve({"verb": "open", "target": "service_door"})
        self.assertFalse(self.state["entities"]["service_door"]["open"])
        self.assertEqual("blocked", result["public"]["status"])
        self.assertIn("threshold-testimony-buggy", result["gm"]["fired_rules"])

    def test_camera_does_not_count_as_witness_before_patch(self):
        self.resolve(
            {
                "verb": "conceal",
                "target": "service_door",
                "observer": "porter",
                "using": "privacy_screen",
            }
        )
        result = self.resolve({"verb": "open", "target": "service_door"})
        self.assertTrue(self.state["entities"]["service_door"]["open"])
        self.assertTrue(result["public"]["anomaly"])
        self.assertEqual(1, self.state["heat"]["signatures"]["S-WITNESS-SCOPE"])

    def test_observer_in_another_location_does_not_count(self):
        self.state["entities"]["porter"]["location"] = "lobby"
        result = self.resolve({"verb": "open", "target": "service_door"})
        self.assertTrue(self.state["entities"]["service_door"]["open"])
        self.assertTrue(result["public"]["anomaly"])

    def test_unsupported_fall_breaks_fragile_object(self):
        self.resolve({"verb": "drop", "target": "porcelain_cup", "height": 2})
        result = self.resolve({"verb": "wait"})
        self.assertFalse(self.state["entities"]["porcelain_cup"]["intact"])
        self.assertFalse(result["public"]["anomaly"])

    def test_first_account_precedes_impact(self):
        self.resolve({"verb": "drop", "target": "porcelain_cup", "height": 2})
        self.resolve(
            {
                "verb": "utter",
                "words": "the cup is intact",
                "claim": {"target": "porcelain_cup", "state": "intact"},
            }
        )
        result = self.resolve({"verb": "wait"})
        self.assertTrue(self.state["entities"]["porcelain_cup"]["intact"])
        self.assertTrue(result["public"]["anomaly"])
        self.assertEqual(
            ["first-account", "impossible-survival-detection"],
            result["gm"]["fired_rules"],
        )

    def test_repeated_signature_is_patched(self):
        for _ in range(3):
            self.resolve({"verb": "place", "target": "porcelain_cup", "destination": "service_corridor", "height": 2})
            self.resolve({"verb": "drop", "target": "porcelain_cup", "height": 2})
            self.resolve(
                {
                    "verb": "utter",
                    "words": "the cup is intact",
                    "claim": {"target": "porcelain_cup", "state": "intact"},
                }
            )
            result = self.resolve({"verb": "wait"})
        self.assertIn("S-FIRST-ACCOUNT", self.state["patches"])
        self.assertTrue(any("impact precedes testimony" in line for line in result["public"]["observations"]))

        self.resolve({"verb": "place", "target": "porcelain_cup", "destination": "service_corridor", "height": 2})
        self.resolve({"verb": "drop", "target": "porcelain_cup", "height": 2})
        self.resolve(
            {
                "verb": "utter",
                "words": "the cup is intact",
                "claim": {"target": "porcelain_cup", "state": "intact"},
            }
        )
        self.resolve({"verb": "wait"})
        self.assertFalse(self.state["entities"]["porcelain_cup"]["intact"])

    def test_resolution_does_not_mutate_input_and_is_deterministic(self):
        action = {"verb": "open", "target": "service_door"}
        before = new_game(self.campaign, seed=17)
        first = act(before, action, self.campaign, seed=17)
        second = act(before, action, self.campaign, seed=17)
        self.assertEqual(first, second)
        self.assertFalse(before["entities"]["service_door"]["open"])
        self.assertEqual([], before["history"])

    def test_arete_three_adds_condition_trace(self):
        action = {"verb": "open", "target": "service_door"}
        attribution = act(new_game(self.campaign, arete=2), action, self.campaign)
        introspection = act(new_game(self.campaign, arete=3), action, self.campaign)
        law = next(r for r in self.campaign["rules"] if r["id"] == "threshold-testimony-buggy")
        self.assertEqual(
            attribution["public"]["signals"] + [law["instrument"]["arete3"]],
            introspection["public"]["signals"],
        )

    def test_take_moves_an_item_with_its_carrier(self):
        self.state["entities"]["player"]["location"] = "records_room"
        self.resolve({"verb": "take", "target": "room_404_key"})
        self.resolve({"verb": "move", "destination": "service_corridor"})
        key = self.state["entities"]["room_404_key"]
        self.assertEqual("player", key["carried_by"])
        self.assertEqual("service_corridor", key["location"])

    def test_openable_objects_can_be_closed(self):
        self.state["entities"]["player"]["location"] = "records_room"
        self.resolve({"verb": "close", "target": "guest_ledger"})
        self.assertFalse(self.state["entities"]["guest_ledger"]["open"])

    def test_physical_examination_is_evidence_without_anomaly(self):
        self.state["entities"]["player"]["location"] = "records_room"
        result = self.resolve({"verb": "touch", "target": "room_404_key"})
        self.assertTrue(any("412" in line for line in result["public"]["observations"]))
        self.assertFalse(result["public"]["anomaly"])
        self.assertEqual([], result["public"]["signals"])

    def test_listening_returns_physical_evidence_without_law_signal(self):
        self.state["entities"]["player"]["location"] = "fourth_floor_corridor"
        result = self.resolve({"verb": "observe", "target": "room_412_door", "mode": "listen"})
        self.assertTrue(any("radio static" in line for line in result["public"]["observations"]))
        self.assertEqual([], result["public"]["signals"])

    def test_opening_container_reveals_persistent_contents(self):
        self.state["entities"]["player"]["location"] = "room_404"
        self.assertTrue(self.state["entities"]["nadia_passport"]["concealed"])
        result = self.resolve({"verb": "open", "target": "nadia_suitcase"})
        self.assertTrue(any("passport" in line for line in result["public"]["observations"]))
        self.assertFalse(self.state["entities"]["nadia_passport"]["concealed"])

    def test_opening_continuity_envelope_reveals_certificate(self):
        self.state["entities"]["player"]["location"] = "room_404"
        self.state["entities"]["continuity_envelope"]["concealed"] = False
        result = self.resolve({"verb": "open", "target": "continuity_envelope"})
        self.assertTrue(any("consensus lodging as 404" in line for line in result["public"]["observations"]))
        self.assertTrue(self.state["entities"]["continuity_envelope"]["open"])


if __name__ == "__main__":
    unittest.main()
