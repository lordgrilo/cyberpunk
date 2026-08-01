# CONSENSUS 3D — Design Spec

*2026-08-01 · status: approved direction, forks resolved · supersedes the client/scope
sections of the 2026-07-31 v0 spec; the v0 spec's reality-kernel design (law strata,
typed seams, heat ledgers, rote schema) remains canonical and is referenced, not
repeated. Derivations from first principles: notes/04-game-design-principles.md.
Narrative vision: notes/05-3d-vision.md.*

## 1. Product statement

A first-person 3D immersive sim, built in Godot 4, about cyberrunners in a dense neon
district whose reality runs on buggy consensus code. The player's *own* understanding —
not the character sheet — is the progression: discover reality's seams by experiment,
weaponize them as rotes, spend them on runs, and adapt as reality patches back.

- **Target aesthetics (ranked):** discovery, expression, challenge, fantasy.
- **Skill mix:** knowledge primary, strategy secondary, execution a real but never
  exclusive lane (action-forward combat is a first-class path with accessibility
  options).
- **Reference constellation:** Deus Ex (action-forward immersive sim), Dishonored
  (consequence economy), Outer Wilds (knowledge progression), BOTW (systemic
  legibility), Shadowrun (fiction register: runners + magic), C77 (aesthetic dream,
  Stage 3).

## 2. Resolved platform decisions

| Decision | Resolution | Rationale |
|---|---|---|
| Perspective | First-person | Lens-native; immersive-sim lineage; no protagonist animation burden |
| Engine (Stages 0–1) | Godot 4.x | GDScript≈Python; fastest grey-box iteration; plain-text project fully AI-collaborable; free |
| Engine (Stage 3) | Revisit (Unreal candidate) | C77-class art; kernel and content stay portable by construction |
| Combat | Action-forward mix | Giovanni's call; Deus Ex proves the pattern |
| Dev platform | macOS (Apple Silicon) | Giovanni's machine; Godot exports cover Win/Linux later |

## 3. Architecture

```
cyberpunk/ (repo)
  engine/            # Python reality kernel — THE BALANCE TESTBED (exists, stays)
  campaigns/         # law/seam/venue content — shared data format (JSON-subset)
  game/              # Godot 4 project (Stage 1+)
    kernel/          #   GDScript port of the reality kernel (pure logic, no nodes)
    systems/         #   witness graph, belief field, schedules, infrastructure sims
    player/          #   FP controller, Lens, interaction, combat
    ui/              #   hypothesis journal, workbench, heat/advisory surfaces
    world/           #   the block/district scenes (grey-box Stage 1)
  tests/
    golden/          #   JSON fixtures: state+action → expected resolution
                     #   RUN AGAINST BOTH kernels (Python & GDScript) — lockstep guarantee
  notes/ docs/       # design memory
```

**Load-bearing commitments (carried from v0, restated for 3D):**
1. **The kernel is pure logic** — no Godot nodes, no I/O; a GDScript class the scene
   tree *calls*. Same public surface as Python `session.act()`: action in → structured
   resolution out. The 3D world *renders* resolutions; it never invents outcomes.
2. **Content is data.** Laws/seams/venues in the shared campaign format, consumed by
   both kernels. Balance tuning happens in the Python testbed at text speed; the Godot
   game consumes the tuned content.
3. **Golden fixtures keep the twins honest.** Any kernel behavior change lands as a
   fixture first; both implementations must pass. Drift = CI failure, not discovery.
4. **Skins touch only vocabulary** (Root commitment; Black Ice at Stage 3).

## 4. Player-facing systems (Stage 1 scope marked ▸)

### 4.1 ▸ Movement & the 2-second loop
FP controller with parkour-lite: run, slide, vault, mantle; deliberately Mirror's
Edge-lite, not a shooter-strafe feel. The Lens pulse (tap = one-shot ping, hold =
sustained overlay) must feel good *idle* — the photographer's-eye fantasy. This loop is
the pivot's new debt and gets tuned before anything else.

### 4.2 ▸ The Lens (Arete = perception bandwidth)
- ▸ Arete 1 glints: localized shimmer + sound motif at every consensus-law firing —
  perceivable pre-interpretation (fair-mystery rule: you can always say "that was
  weird"). In Stage 1 the slice *opens* here: job 1 is mundane, job 2 is glint bait,
  and the Awakening to Arete 2 is the first Seeking.
- ▸ Arete 2 attribution: glyphs identify *which* law fired (tradition iconography).
- ▸ Arete 3 introspection: condition traces — ghost light-paths showing what the law
  checked (him, the camera, not the mirror).
- Arete 4 stepping (Stage 2): freeze a small bubble; laws fire as slow light.
- Arete 5 write (Stage 3): brief catastrophic raw edits.
Advancement by Seeking (story-gated epiphany), never points.

### 4.3 ▸ Experiments = physical staging
Kernel verbs as world interactions: take, place, conceal, drop, open, close, utter
(line choices), observe, wait, touch, give, time. (`move` is subsumed by the FP
controller in 3D; the kernel keeps it for testbed parity.) The **hypothesis journal** (grimoire's
3D face) auto-logs staged acts ↔ observed resolutions and lets the player pin
hypotheses. The game never grades reasoning; reality answers.

### 4.4 ▸ Rotes = spatial choreography
Workbench (hideout): compose confirmed seams into role-based procedures (v0 schema).
Field: equipped rote projects AR ghost-outlines of role bindings; conditions light as
satisfied; trigger on green. Misbinding misfires. Chaining at Stage 2.
**▸ Vulgar forcing:** any confirmed seam forced raw — instant, spectacular, heat spike.

### 4.5 ▸ Combat (action-forward)
- Mundane lane: one pistol-class weapon + one gadget at Stage 1; melee takedown;
  execution depth grows Stage 2 (cyber-light augments, more weapons).
- Magic in combat = vulgar forcing + pre-staged rotes (the prepared-battlefield
  fantasy). Knowledge multiplies combat; never purchasable damage.
- Witness pressure: vulgar acts before witnesses multiply heat — firefights are where
  the witness graph screams. Suits patch forced seams *live* in encounters (Stage 2;
  Stage 1 Suits are a patrol/response archetype only).
- Accessibility: aim assist / difficulty toggles so execution is never the only wall.

### 4.6 ▸ Consequence surfaces
Heat ledgers per v0 kernel. World-visible: local heat → NPC rumor/news re-explanations;
advisory → readable warnings (skeptic blog, notice, parked van); patch → visible world
change + journal breakage of dependent rotes. Personal heat → Suits response tier.

### 4.7 The Ward's simulations (Stage 1: one block)
▸ **Witness graph** (star system): NPC sightlines, CCTV, phones, sleep states —
consensus enforcement IS witnessing; stealth = hiding from reality's jury.
▸ **Schedules**: a dozen NPCs with routines on the block.
**Belief field** (Stage 2): block/time-varying consensus density.
**Infrastructure** (Stage 2): power, traffic, weather bound by ordinances.

## 5. Stage 1 — the grey-box vertical slice (the build target)

**One city block. Two seams. The full loop, floor to ceiling.**

Contents: FP controller + parkour-lite; Lens (Arete 2→3 via one Seeking); witness graph
+ NPC schedules; 2 seams (one scope-gap: camera-as-witness; one race-window) embedded in
~12 consensus laws; hypothesis journal; workbench with rote compose/equip/cast + vulgar
forcing; 1 weapon + 1 gadget combat v1; Suits response archetype; heat/advisory/patch
full pipeline; one job line (fixer, 3 jobs: pure-mundane teach → glint bait → a job a
rote trivially solves); grey-box art + neon-minimal lighting + sound motifs for glints.

**Explicitly out:** belief field, infrastructure sims, chaining, Arete 4–5, generator,
Black Ice, story beyond the one fixer, any art beyond grey-box.

**Stage 1 success criteria (all must hold, human-playtested):**
1. Traversal + Lens feel good with all meta systems switched off (2-second loop pays).
2. A blind playtester forms an unprompted hypothesis inside 30 minutes.
3. First seam confirmation lands as an *aha* (verbalized, unprompted).
4. A player-composed rote carries job 3; vulgar forcing gets used under pressure and
   its heat consequence is *felt*.
5. The patch of an overused seam reads as fair and produces visible adaptation.
6. Law/seam tuning happens in the Python testbed and lands in Godot by data copy, no
   code edit.

## 6. Production reality

- Solo-plus-Claude cadence: kernel port + FP controller + witness graph are the long
  poles; grey-box keeps art near zero; audio = motif library + free SFX initially.
- The Python testbed stays the *design* iteration surface (minutes per experiment);
  Godot is the *feel* iteration surface. Never tune balance in Godot.
- Nemesis-patent constraint: Suits adapt as an *organization* (method profiling,
  counter-deployment), never as resurrecting named rivals.
- IP hygiene: Mage/Shadowrun are inspiration registers; all terminology in-game is
  original (Lens, Seams, Suits, the Ward, Seeking is renamed by Stage 2).

## 7. Risks (delta from v0 list)

- **The 2-second loop** is now the biggest risk surface (we're entering feel-craft,
  not just systems-craft). Mitigation: criterion 1 gates everything; steal proven FP
  controller tuning openly.
- **Two kernels drifting.** Mitigation: golden fixtures in CI from day one.
- **Combat scope creep** (action-forward invites arms-race content). Mitigation:
  Stage 1 combat is deliberately one-weapon thin; depth is a Stage 2 line item.
- **Witness-graph performance** (many observers × many events). Mitigation: block-scale
  first; event-driven checks, not per-frame raycasts everywhere.
