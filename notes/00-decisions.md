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

## 2026-07-31 — Design converged (same day, later)

6. **Engine language: Python.** Fastest for Giovanni to hack on; v1 browser runs it
   behind FastAPI or Pyodide.

7. **Core mechanic: exploit research + rotes** (after two rejected models — see
   notes/03-casting-rework.md). Reality is a simulated rulebase with hidden, seeded,
   *typed* seams; player skill is epistemic (hypothesize → experiment → confirm);
   confirmed seams get composed into reusable role-based **rotes** (dry-run, bind,
   refine, chain). Character stats = instrumentation resolution only (Arete ladder
   1–5); understanding is never purchasable.

8. **Heat economy:** local heat (decays), signature heat (never decays → advisory →
   patch; breaks dependent rotes), personal heat (summons Technocracy). Seams are
   finite wells priced in usage; the economy self-balances.

9. **AI-GM constitution:** the AI never decides what happens, only what it's like.
   Engine = outcomes; AI = texture, NPCs, story, fiction→action translation (always
   echoed back). Codified in PLAY.md.

10. **v0 scope:** engine + one hand-authored venue (residential hotel, ~30 laws, 5–6
    seams, all 4 seam types) + CLI + PLAY.md + play-in-Claude-Code. Arete 2→3 only.
    Deferred: generator, Black Ice skin, browser, Arete 1/4/5.

11. **Spec:** docs/superpowers/specs/2026-07-31-consensus-v0-design.md — approved
    section-by-section in session; awaiting Giovanni's review of the written file.

## Open questions

- **Blind-playtest calibration.** Does Arete 2 reveal enough to support a hypothesis
  without naming the answer? This must be tested with a human before expanding the hotel.

## 2026-07-31 — First playable slice

12. **Build the epistemic loop before the content breadth.** Implemented one micro-venue
    with two contrasting seams, a deterministic data-driven resolver, the eleven-verb
    mundane action boundary, Arete 2/3 feedback, permanent signature heat, advisories,
    and live patches. The slice is intentionally smaller than the planned 30-law hotel.

13. **No dependency for the first playtest.** Campaign `.yaml` files currently use JSON
    syntax (a valid YAML subset) and the standard-library parser. Move to full YAML only
    when the content authoring benefit justifies adding the dependency.

14. **Do not mistake passing tests for validated design.** Automated checks establish
    consistent causality; only a blind playtest can establish discovery, surprise, and
    the feeling of earned magical competence.

15. **The mundane vocabulary must follow ordinary intent.** The first live player tried
    to take a key and close a book and door; neither action existed in the original
    eleven-verb surface. Added `take` and `close` rather than forcing those acts through
    semantically false verbs. A small vocabulary is useful; an artificially complete
    list chosen before play is not.
