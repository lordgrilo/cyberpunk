# CONSENSUS 3D — Vision: cyberrunners in a city whose reality has bugs

*2026-08-01 · the wrap: the reality-hacking core (see v0 spec) redesigned as a full 3D
game, derived from notes/04-game-design-principles.md. Numbers in [brackets] cite the
principles doc.*

## 0. One-paragraph pitch

A dense neon district. You're a **runner** — jobs, fixers, factions, the usual hustle —
until the night you *see it*: the CCTV feed resolving what happened before it happened.
Reality here runs on old, patched consensus code, and you've started perceiving the
seams. Now every job is also an experiment, every impossible escape a proof, and the
city's gray-suited incident-response teams are closing on the anomaly that is you.
**GTA's streets, Dishonored's freedom, Outer Wilds' progression: the only thing that
levels up is what you understand.**

## 1. Target aesthetics [1]

Ranked, and every mechanic must serve one: **discovery > expression > challenge >
fantasy**. Non-goals: fellowship (single-player), submission (no grind loops).

## 2. Design pillars

- **P1 — The city is the lab** [5]: all content is interacting simulations; seams live
  in system *intersections*; nothing is a one-answer puzzle [6].
- **P2 — Hide the model, never the signal** [3,9]: every law-firing casts a visible
  shadow; instrumentation upgrades interpretation, not existence, of signals.
- **P3 — Many doors** [6,4]: every job completable mundanely; magic multiplies options,
  never gates the path.
- **P4 — Knowledge is the only power** [7,2]: grimoire = progression; stats = perception
  bandwidth; understanding is never purchasable.
- **P5 — Reality fights back** [13,2]: heat → advisory → patch; the world re-explains,
  then rewrites. The economy, not the designer, balances power.
- **P6 — The mechanic is the message** [12]: the theme (who defines the real, what
  dissent costs) is said in rules, not cutscenes.

## 3. The loop budget [8]

| Timescale | Loop | Must feel like |
|---|---|---|
| 2 s | run/vault/slide + **Lens** pulse; anomaly glints in the world | fluid parkour-lite + a photographer's eye |
| 30 s | probe: place/conceal/utter/time a micro-experiment; read the trace | setting a tiny trap for physics |
| 5 min | the run: infiltrate/extract/flip using mundane play + equipped rotes; manage witnesses & heat | a heist beat you improvised |
| Session | job → fallout → research at the hideout → compose/refine rotes → next job | a lab notebook turning into a toolkit |
| Campaign | seam portfolio vs. patch pressure; faction arcs; Seekings (Arete tiers); district's consensus visibly shifts | an arms race you're losing slowly and winning cleverly |

The 2-second loop is new debt the 3D pivot takes on and must pay: traversal and Lens
have to be *inherently* pleasurable before any meta exists [8,9].

## 4. The 3D translation of the core mechanics

### 4.1 The simulated city (the substrate made visible) [5]

One district — **the Ward** — running interacting simulations:

- **Witness graph** (the star system): who/what observes whom, moment to moment —
  NPClines of sight, CCTV, phones, mirrors, sleeping/waking states. Diegetically:
  *consensus enforcement is witnessing*. Stealth is re-motivated as metaphysics: you
  don't hide from guards, you hide from reality's jury. [P6]
- **Belief field**: consensus density varies by block/time/crowd (church at mass ≈
  hardened runtime; casino at 4am ≈ permissive debug build). Visible in Lens as
  weather-like gradients.
- **Schedules & crowds**: NPC routines, densities, flows (jobs depend on them; witnesses
  come from them).
- **Infrastructure**: power, CCTV networks, traffic, weather — physical systems the
  consensus laws bind together.

Consensus laws govern *interactions between* these systems ("what the first witness
account says, happened"; "cameras' records settle disputes"; "the dead stay dead —
checks pulse, not brain"). Seams are typed as before (ordering, scope, state-confusion,
race) and live in the intersections. The v0 spec's rulebase design (strata, typed seams,
heat ledgers) survives intact as the **reality kernel**; the text engine remains our
balance testbed.

### 4.2 Perception: the Lens (Arete as instrumentation) [P2, 7]

- **Naked eye (pre-Awakening / Arete 0-1):** anomalies still *glint* — a shimmer, a
  sound motif, a frame-stutter localized in the world. You can always say "that was
  weird."
- **Arete 2 — Attribution:** Lens mode overlays glyphs at law-firings: *which* law, in
  your tradition's iconography.
- **Arete 3 — Introspection:** traces: ghostly light-paths showing what conditions the
  law checked (it looked at *him*, at *the camera*, not at *the mirror*…).
- **Arete 4 — Stepping:** the show-stopper power: freeze a small bubble of reality for a
  beat and watch the laws fire in order as slow light. (Debugger as spectacle.)
- **Arete 5 — Write:** brief, catastrophic, alarm-everything raw edits. Endgame, vulgar,
  priced accordingly.

Seekings (story-gated epiphanies) grant tiers; no XP anywhere. [P4]

### 4.3 Experiments: staging, not menus [6,10]

The eleven kernel verbs become physical play: pick up, place, conceal, drop, open,
utter (voice lines with content choices), observe, wait, touch, give, time. A
**hypothesis journal** auto-correlates what you saw with what you did (the grimoire's 3D
face). Designing a clean experiment = arranging the scene so only one explanation can
survive — the game never grades your reasoning, reality just answers. [P1, P2]

### 4.4 Rotes: heist-planning as spellcraft

At the hideout **workbench**, confirmed seams compose into rotes (role-based procedures,
as in the v0 spec). In the field, an equipped rote projects **AR ghost-outlines** of its
role bindings onto the world — *place a MASS here · no human sightlines · a recording
device there* — conditions light up as they're satisfied; trigger when green. Casting is
spatial choreography, not a menu. Misbindings misfire. Chained rotes = multi-stage
setups across a whole scene (the masterwork feel: a Rube Goldberg machine made of law).
**Vulgar fallback:** any confirmed seam can be *forced* raw — instant, dramatic, huge
heat spike. The coincidental/vulgar dial from Mage, expressed spatially. [P3, P5]

### 4.5 Consequence: heat, patches, and the Suits [P5, 13]

Three ledgers as designed (local / signature / personal). In 3D they're *world-visible*:

- Local heat: the district re-explains — news crawls, street rumors, NPCs repeating the
  cover story consensus invented. (Reactivity spent exactly where the fantasy needs it
  [11].)
- Advisory: skeptic blogs, safety notices, a van parked where you work. Readable
  warnings for the watchful.
- Patch: the seam closes *visibly* — new signage, new procedures, a firmware rollout —
  and dependent rotes break in the journal. The neighborhood is literally rewritten. [P6]
- Personal heat: **the Suits** (Technocracy incident-response). Organizational memory —
  they profile your *methods* and field counters (design around the WB nemesis patent:
  the org adapts, not named rivals) [13]. Encounters are systemic cat-and-mouse, not
  boss fights; watching them work teaches you laws you haven't found.

### 4.6 Combat stance [7,14]

Avoidance-first immersive sim: light non-lethal toolkit, execution skill never the wall.
Failure escalates (heat, patches, Suit attention), it doesn't game-over. The one dread:
grimoire compromise — a rival or the Suits *stealing understanding* — always story-fuel,
never deletion. [14]

### 4.7 The mundane game (the floor everything stands on) [P3, 10]

Before any magic: a complete, small, honest runner game — traversal, social
infiltration, gadgets, fixers, jobs. Hour one is entirely this, with one planted glint
[10]. The Awakening is the inciting incident *and* the tutorial's graduation. If the
mundane floor isn't fun, no seam will save it.

## 5. Structure & scope staging (honest ladder)

- **Stage 0 — Kernel testbed (exists):** the Python reality-kernel + text play for
  law/seam/heat tuning. Cheap iteration lab; stays alive permanently.
- **Stage 1 — Grey-box vertical slice:** ONE city block, witness graph + belief field +
  schedules, 2 seams, full pipeline (glint → hypothesis → experiment → rote → patch),
  Lens 2-3, parkour-lite, one job line. Grey-box art, neon-minimal lighting. *The go/no-go
  artifact.*
- **Stage 2 — The Ward:** full district, 5-6 seams across all types, factions, Suits,
  advisory/patch fiction, hideout/workbench, 6-10 hr campaign.
- **Stage 3 — The dream:** art pass toward the C77 look, generator for reseeded
  campaigns, Black Ice skin (corporate subsystem runs — same loop, 'trace' skin),
  the fusion reveal.

Scope truth, said once: C77 cost ~500 person-years. The design above is built so that
**density substitutes for acreage** [11] and **systems substitute for content** [5] —
the two known levers that let small teams ship immersive sims. Stage 1 is
solo-plus-Claude feasible; Stage 2 is a long solo campaign or a small team; Stage 3 is
funding-or-years. Every stage is a complete, playable, honest thing.

## 6. Open forks (to resolve before spec rewrite)

1. **Perspective:** first-person (Lens-native, immersive-sim lineage, no protagonist
   animation burden) vs third-person (character fantasy, GTA-feel, costlier). Lean: FP.
2. **Engine:** Godot 4 (free, light, GDScript≈Python, great for grey-box; C# optional)
   vs Unity (asset ecosystem, heavier) vs Unreal (the C77 look someday, heaviest now).
   Lean: Godot for Stages 0-1, revisit at Stage 3.
3. **Combat stance:** confirm avoidance-first (4.6) vs a more action-forward mix.
   Lean: avoidance-first.

## 7. What survives from the v0 spec

The reality kernel design survives whole: law strata, typed seams, heat ledgers,
rote schema, AI-GM constitution (which becomes the NPC/narrative director's constitution
in 3D), grimoire-as-progression. What the pivot replaces: the *client* (text → 3D), the
delivery of experiments (described acts → physical staging), and the delivery of
perception (JSON → Lens VFX). The spec gets rewritten as TWO docs: kernel spec (mostly
done) + 3D game spec (this doc, hardened after forks resolve).
