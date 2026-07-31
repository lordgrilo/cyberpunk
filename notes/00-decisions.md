# Decision Log — "Consensus" (working title)

A running log of design decisions. Newest at the bottom. Keep this updated every session.

## 2026-07-31 — Founding decisions

1. **Core hook.** A game where magic = hacking reality, and *the player's own skill* at
   constructing magic matters — not just character stats. (Mage: The Ascension's paradigm
   idea, but with player-skill spellcraft instead of dice.)

2. **Medium.** Something between a playable video game and an AI-GM hybrid: a real
   mechanical engine (objective, skill-based) + an AI game master (reactive, narrative).

3. **Fiction/architecture: "Consensus with Root underneath, Black Ice as an example."**
   - **Consensus** (Mage-style) is the game the player sees: reality is negotiated
     consensus; spells are structured *arguments* against it; implausibility accrues Paradox.
   - **Root** (the fusion idea) is the *architecture*: under the hood every spell compiles
     to substrate calls with cost/scope/permission semantics. Paradigms are *skins* —
     surface languages over the same substrate.
   - **Black Ice** (the Neuromancer sketch) is the second skin: a technomancer/exploit
     paradigm over the same substrate. It exists to *prove* the substrate abstraction is
     real, and seeds the late-game fusion reveal (mystics and hackers are rival UIs over
     the same API).

4. **Staging (easiest first, doesn't close the 3D door).**
   - v0: headless engine (pure library, no UI) + playtesting inside Claude Code
     (Claude as GM, engine adjudicates).
   - v1: thin browser client with a real spell-composition UI + Claude API narration.
   - vFuture: the engine becomes the magic system inside a full 3D game
     (GTA / Cyberpunk 2077-class visuals is the stated long-term dream).
   - Rationale: the user cares about *crafting the system* now; visuals are a client
     concern and must never leak into the engine.

5. **Workflow.** Everything gets saved as files/notes in this folder (Dropbox-synced) so
   work can continue remotely. Git repo initialized in `consensus/`.

## Open questions

- Engine implementation language (TypeScript vs Python) — pending.
- Exact shape of the spell language (see notes/01-sketches.md, Sketch 1) — to be designed.
- Scope of v0 scenario (single venue vs small campaign) — pending.
