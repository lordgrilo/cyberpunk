# The Three Sketches (2026-07-31)

Original brainstorm: three ways to build a "reality-hacking where player skill matters"
game. Decision: build Sketch 1 as the game, Sketch 3 as the architecture, Sketch 2 as the
second paradigm skin. Kept verbatim-ish for reference.

---

## Sketch 1 — Mage-style: "Consensus"  ← THE GAME

**The world.** Reality is a negotiated settlement. What most people believe is what
physics enforces. Mages have noticed the negotiation is still open — but every working is
an *argument* submitted against consensus, and reality pushes back on arguments it finds
implausible (Paradox).

**What the player does.** Magic is a small formal language of **claims**. A spell is a
structured argument with three parts:

- **Premise** — what you assert is true ("this lock is old and poorly made")
- **Leverage** — which Sphere/domain you're twisting (Matter, Forces, Time, Mind…), each
  with primitive operators you've learned
- **Coincidence wrapper** — the mundane story that lets consensus swallow the effect
  ("old locks fail")

The engine scores the spell on:
- *internal coherence* — do the premises actually entail the effect?
- *sphere reach* — are you claiming more than your operators can express?
- *plausibility* — how much does the wrapper strain the local consensus?

A tight, plausible argument works silently. A sloppy or vulgar one still works — but
accrues **Paradox**, which the engine tracks and eventually spends against you in kind
(your own bad premises become true in the worst way).

**Player skill** = operator vocabulary, composing minimal arguments, reading the *local*
consensus (a hospital believes in death; a casino believes in luck — the same spell scores
differently by venue).

**AI-GM layer.** Narrates consequences, plays NPCs (rival mages, Technocracy-style
enforcers), and adjudicates the coincidence wrapper: the engine scores structure
numerically; the AI judges whether the mundane cover story is narratively plausible in
context, and describes how reality "explains away" the magic.

**Mastery feels like** becoming a lawyer against the universe. Early game: brute-force
spells and Paradox burns. Late game: three-word spells that look like luck.

---

## Sketch 2 — Neuromancer-style: "Black Ice"  ← THE SECOND SKIN

**The world.** Near-future sprawl. The matrix is a consensual hallucination of the
world's data — corporate cores as geometry, ICE patrolling the approaches.

**What the player does.** Every target is a generated **system graph** — nodes (gateways,
logs, vaults, ICE processes) with states, trust relationships, daemons. You act by writing
small **programs** in a constrained exploit language: probe, spoof, pivot, splice, wipe.
Programs run in real time inside the system; ICE runs *its* programs against you
concurrently. Skill: reading unfamiliar topology, chaining minimal exploits, managing
heat/trace, knowing when to cut and run. (cf. Hacknet, else Heart.Break())

**AI-GM layer.** Generates the fiction around runs — fixers, jobs, betrayals, what stolen
data *means* — and plays the matrix AIs (the Wintermute figures) whose goals emerge
across runs.

**Mastery feels like** competence porn: the run that took twenty minutes now takes ninety
seconds and leaves no logs.

**Role in the final design:** the technomancer paradigm skin over the Root substrate.
Proves the substrate abstraction is real; seeds the fusion reveal.

---

## Sketch 3 — Fusion: "Root"  ← THE ARCHITECTURE

**The world.** Cyberspace was never a metaphor. Reality runs on a substrate; magic and
intrusion are two UI skins over the same access layer. Mages chant; technomancers type;
both issue calls against the same API. The war between traditions is a war over *which
interface becomes standard* — the substrate optimizes for its most common client.

**What the player does.** One underlying formal system — substrate calls with cost,
scope, and permission semantics — with swappable **paradigm skins**: hermetic skin =
sigil-grammar, technomantic skin = pseudocode, shamanic skin = bargains with
process-spirits. Same semantics, different affordances: each skin makes some calls cheap
and others awkward (the code skin loops beautifully but can't express sacrifice; the
bargain skin gets huge effects at deferred, negotiated cost). Paradox becomes **type
error**: claims contradicting the local runtime's active schema throw exceptions into the
world.

**Player skill** = understanding substrate semantics *through* the skins; choosing the
right paradigm for the problem; the deepest players read the raw call underneath any
rival's casting.

**Mastery feels like** bilingual fluency, then enlightenment: you stop seeing the skin
and see the calls.

**Role in the final design:** the engine's actual data model. Consensus spells and Black
Ice exploits both compile to substrate calls. Late-game story door: the player discovers
this is diegetically true.

---

## Where the difficulty lives (design note)

- Sketch 1's skill is *rhetorical* — compose plausible arguments; partly AI-judged; softer.
- Sketch 2's skill is *computational* — deterministic puzzle graphs; hardest, most objective.
- Sketch 3 needs one semantics + N surface languages ≈ both engines unified; biggest build.

Pragmatic consequence: build 1 with 3's abstraction underneath; add 2 as the second skin;
keep the fusion reveal as a late-game door.
