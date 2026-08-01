# CONSENSUS

Reality is an opaque rule system. The Awakened can feel its machinery; only the player can
learn what the machinery means.

This first playable slice contains a deterministic, data-driven engine and one hotel
corridor with two hidden seams. It is deliberately small: it tests whether observing,
hypothesizing, and experimenting feels like magic before more content is built.

From the directory containing this repository:

```sh
python3 -m consensus.cli play
```

The shell lists entity IDs and accepts `help`, `look`, and compact mundane actions. There
is no spell command. An AI GM can instead use the JSON adapter and must obey `PLAY.md`.

Run the zero-dependency test suite with:

```sh
python3 -m unittest discover -s consensus/tests -v
```

Campaign files live under `campaigns/`. During play, treat `laws.yaml` and `seams.yaml` as
GM-only material.

