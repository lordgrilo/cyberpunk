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

## 2026-08-01 — THE 3D PIVOT ("back to the basis")

16. **Giovanni rejected the text-first framing after feeling it in play**: "not good
    enough… let's plan a whole 3D cool game with cyberrunners… go back and fish game
    design principles and then let's wrap our game idea around it." The reality-hacking
    core stays; the product is a 3D game, designed principles-first.

17. **Principles doc:** notes/04-game-design-principles.md — MDA, Koster, flow, SDT,
    second-order/systemic design, immersive-sim creed, skill taxonomy, loop budget,
    game feel/legibility, Bushnell's law, open-world lessons, ludonarrative harmony,
    economy design, failure design — each with "demands of us", plus a
    tensions-and-rulings section.

18. **3D vision:** notes/05-3d-vision.md — pillars P1–P6; loop budget by timescale; the
    Ward district (witness graph / belief field / schedules / infrastructure); the Lens
    (Arete instrumentation as AR perception layers); experiments as physical staging;
    rotes as AR-ghost spatial choreography; heat/patch made world-visible; the Suits as
    organizational memory (nemesis-patent-safe); avoidance-first combat; a fully mundane
    runner floor under everything. Scope ladder: Stage 0 kernel testbed (exists) →
    Stage 1 grey-box vertical slice (one block, 2 seams) → Stage 2 the Ward →
    Stage 3 the dream (C77-class art, generator, Black Ice skin).

19. **The v0 kernel survives the pivot whole** (laws, typed seams, heat ledgers, rotes,
    constitution, grimoire). The text client is demoted to permanent balance testbed.
    The playable micro-slice from entry 12 is committed as-is and stays runnable.

20. **Repo on GitHub:** https://github.com/lordgrilo/cyberpunk — push after every work
    chunk; remote sessions pull before working.

## 2026-08-01 — Forks resolved, 3D spec written

21. **First-person.** Lens-native, immersive-sim lineage, no protagonist animation cost.

22. **Godot 4 for Stages 0–1** (Giovanni delegated; confirmed): GDScript≈Python,
    fastest grey-box iteration, plain-text project fully AI-collaborable. Unreal
    reconsidered at Stage 3; kernel/content engine-portable by construction.

23. **Action-forward combat (Giovanni's call, over the avoidance lean).** Deus Ex
    pattern. Folded in: mundane weapon/gadget lane with accessibility toggles; vulgar
    seam-forcing as combat verb (spectacular, heat-ruinous); witness pressure makes
    firefights consensus-loud; knowledge multiplies combat, never purchasable damage.

24. **3D spec:** docs/superpowers/specs/2026-08-01-consensus-3d-design.md — twin-kernel
    architecture (Python testbed + GDScript port, golden JSON fixtures keep lockstep),
    Stage 1 vertical slice defined (one block, two seams, full glint→patch loop, 6
    success criteria). v0 spec remains canonical for the kernel internals.

## Open questions

- Giovanni to review the 3D spec file before we write the Stage 1 implementation plan.
- (Carried) Blind-playtest calibration of Arete 2 — now Stage 1 criterion 2/3.

## 2026-09-15 — Gate 0 built (kernel/world-model split)

25. **The kernel no longer owns the world.** `adjudicate(request, campaign)` is a pure
    function of a self-describing request: `event`, `subject` (claim-shaped facts),
    `proposal` (the outcome under adjudication), `witnesses` (evidence records with
    modality), `consensus` (arete/patches/signatures). It returns deltas — it never
    mutates the request and never writes world state.

26. **Geometry moved out to `engine/worldmodel.py`.** The old `observer_count` fact
    walked every entity checking location, `observing`, `cannot_see` and `awake`. That
    logic is now the world model's job — the text engine today, Godot tomorrow. The
    kernel only counts witnesses it was handed, so it cannot reason about wakefulness or
    sightlines even by accident.

27. **Witnesses carry modality, not species.** `observer_count.human` became
    `witness_count.direct_sight`; `kind: device` observers produce `optical_record`.
    This states the scope-gap seam in its true terms: the buggy law queries the wrong
    *evidence modality*, which is exactly what Gate 2's cameras and Gate 3's port need.

28. **`rules.py` is now a generic matcher** parameterised by a fact resolver; it knows
    how to compare facts, not what any fact means. Effects may only amend the proposal;
    keys prefixed `_` (e.g. `_stabilized`) are adjudication-internal and are never
    committed to entities.

29. **Five golden fixtures frozen** in `tests/golden/threshold-seam.json` as
    language-neutral JSON: enforcement, the seam, the unwitnessed baseline, post-patch
    behaviour, and an unlocked-door negative control. These are the lockstep contract the
    GDScript kernel must satisfy at Gate 3.

30. **A brittle test was rewritten, not deleted.** `test_arete_three_adds_condition_trace`
    asserted on the literal phrase "awake human witnesses"; since the kernel no longer
    knows about wakefulness, that prose would now be a lie. It now asserts the behaviour:
    Arete 3 returns Arete 2's signals plus the law's introspection trace.

**Status:** 17 tests + 5 golden subtests green; the text slice runs unchanged. Gate 0's
pass condition is met — a door resolves from a supplied human/camera snapshot with no
geometry or narrative code in the kernel.

**Not yet done from Gate 0's bullet list:** the full eight-phase lifecycle is only
partly explicit (PROPOSE / ADJUDICATE / COMMIT are real; INTENT, CONTEXT, REACT and
SETTLE remain implicit in the caller). The network and authority graphs are Gate 2.
