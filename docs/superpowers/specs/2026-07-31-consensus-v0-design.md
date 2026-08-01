# CONSENSUS — v0 Design Spec

*2026-07-31 · working title "Consensus" · status: approved design, first playable slice implemented*

## 1. What this is

A game where magic is hacking reality, and the skill of doing it belongs to the **player**,
not just the character. Inspired by Mage: The Ascension's premise (consensus reality,
Paradox, the Technocracy) and Neuromancer's craft (intrusion as competence), as original
IP — no White Wolf content.

**Core statement: reality is a system with bugs; magic is exploit research.** The engine
simulates a world running on hidden, generated-with-seeded-bugs rules. The player
discovers those rules by experiment, weaponizes the seams into reusable rotes, and adapts
when consensus patches what got loud. The character sheet gates *observation*; only the
player supplies *understanding*.

**Medium:** between a video game and an AI-GM hybrid — a deterministic Python engine
(sole authority over outcomes) plus an AI game master (sole authority over texture:
narration, NPCs, story). v0 is played inside Claude Code sessions; the same engine later
backs a browser client (v1) and, aspirationally, a full 3D game (the stated long-term
dream is GTA / Cyberpunk 2077-class visuals).

### 1.1 Architecture lineage (the three sketches)

- **Consensus** (Mage-style) — the game the player sees. This spec.
- **Root** (fusion) — the architecture: the engine is paradigm-neutral; magic and
  hacking are skins over the same substrate. Kept as a structural commitment (§8).
- **Black Ice** (Neuromancer) — the future second skin: network intrusion as the same
  probe/exploit/heat loop against corporate venues. Deferred past v0; seeds the
  late-game fusion reveal.

### 1.2 Rejected directions (design memory)

Two casting models were designed and rejected before this one; see
`notes/03-casting-rework.md`. Short form: any model where the rules of magic are *known*
and player skill is composition within them (a spell DSL; a correspondence-web
pathfinder) fails the founding requirement. A hacker's skill is epistemic — the rules
must be hidden, and the game is discovering them.

## 2. The core loop

1. **Notice** — an anomaly surfaces (instrumentation ping, or fiction shows a seam-shadow)
2. **Hypothesize** — the player records a suspicion in the grimoire
3. **Experiment** — staged acts in the fiction; the engine resolves them against the true
   rulebase; results confirm or kill hypotheses
4. **Compose** — confirmed seams are hardened into rotes
5. **Operate** — rotes are spent on story jobs, generating heat
6. **Adapt** — reality patches loud seams; the library decays; return to 1, smarter

The AI-GM's story layer (jobs, factions, deadlines) *consumes* exploits; the research
game *produces* them. Story gravity exists to force research into the field before it's
ready.

## 3. The world engine

### 3.1 World state

Entities with typed properties (position, mass, observed-by, lit, asleep, believed-dead,
…) inside a **venue**. Venues carry their own consensus profile (§3.2). All state is
serializable, human-readable YAML; the engine is a pure function of
`(state, action, seed)`.

### 3.2 Rulebase — three strata

- **Deep laws** — unpatchable bedrock (causality, conservation-ish). Never contain
  seams; they keep the game from dissolving.
- **Consensus laws** — enforced because believed: "falling people get hurt", "locked is
  locked", "the dead stay dead", "a witness's account settles what happened". Ordered
  condition→effect rules firing on ticks and events, each carrying scope, priority,
  exception list — and, sometimes, bugs. **All seams live here.**
- **Local ordinances** — venue-layered beliefs (a hospital runs extra death laws; a
  casino runs luck laws). Venues are different security configurations of the same OS.

### 3.3 Seams (the vulnerability taxonomy)

Seams are **typed**, mirroring real vuln classes — this is what makes generation feasible
and player skill transferable across campaigns:

| Seam type | Shape | Example |
|---|---|---|
| Ordering bug | law X resolves before law Y checks | damage settles before witness-consensus fixes the cause |
| Scope gap | a law's condition checks too narrow a class | "observed" checks *human* observers; lenses don't count |
| State confusion | one entity state read differently by two laws | a sleeping mind is "absent" for testimony, "present" for occupancy |
| Race window | ticks between event and consensus settling | outcomes are rewritable until the first account is given |

v0 hand-authors its seams; the future generator instantiates these types into fresh
law-sets (CTF-designer method). Difficulty = how many observations are needed to
distinguish the buggy law from its plausible non-buggy twin.

### 3.4 Actions

The player acts **only through the fiction**. A small mundane action vocabulary is the
engine's entire input surface — currently these thirteen: `move, place, conceal, drop,
open, close, take, utter, observe, wait, touch, give, time`. Extending the vocabulary is
a spec change, not an implementation convenience. `close` and `take` were added during
the first live playtest after ordinary player intent exposed their absence. The
AI-GM translates described acts into actions and **echoes the parse back for confirmation
before resolution** — auditable, cooperative, no hidden interpretation.

## 4. Instrumentation (the stat/skill contract)

The character sheet buys *resolution of feedback*, never understanding:

- **Arete 1** — anomaly sense: "something non-mundane just resolved here"
- **Arete 2** — attribution: *which* law fired (as a felt signature, named in the
  tradition's idiom)
- **Arete 3** — introspection: partial read of a fired law's conditions (stack trace,
  not source)
- **Arete 4** — stepping: freeze a small region for a beat; watch laws fire in order
- **Arete 5** — write access: brief, catastrophic, maximally vulgar (an alarm you cast)

v0 implements Arete 2 and 3 only (start at 2; one mid-arc Seeking to 3).

## 5. Rotes

A rote is a composed procedure over **roles**, not specific objects:

```
ROTE: "The Unwitnessed Fall"            (exploits seam S3: observer-scope gap)
  requires:  a MASS (>2kg), an ELEVATED PLACE, zero HUMAN observers,
             one RECORDING DEVICE (non-human observer)
  steps:     conceal MASS at ELEVATED PLACE → clear human witnesses →
             trigger the drop while only DEVICE observes → DEVICE is first witness
  effect:    the fall resolves by the device's frame — and a lens can be lied to
  footprint: low (2 heat) · setup: minutes · fragility: breaks if any human
             glances during the window
```

- **Dry-run** (in the study, free): the engine validates rote *logic* against confirmed
  seams — structure, not outcomes. Rotes built on unconfirmed hypotheses are legal, and
  gambling.
- **Casting** = binding roles to actual scene elements in the field; engine resolves.
- **Refinement** (craft skill): cut footprint, widen roles, shrink setup, add fallbacks.
- **Chaining** (master skill): rotes invoking rotes; multiple seams composed into one
  impossible outcome.
- The grimoire tracks every rote's **seam dependencies**; a patch visibly breaks
  dependent rotes.

## 6. Heat and the patch cycle

Every resolved anomaly emits heat ∝ witnesses × implausibility × repetition-of-signature,
pooled in three ledgers:

- **Local heat** (venue) — decays over time; thresholds spawn engine-triggered anomaly
  events (Paradox backlash, AI-narrated).
- **Signature heat** (per seam) — **never decays**. Threshold 1: *advisory* (fiction: a
  skeptic blogs, a safety notice appears — catchable warning). Threshold 2: **patch**
  ships; the seam closes; dependent rotes break visibly.
- **Personal heat** (player) — accrues when signatures correlate with your presence;
  summons the Technocracy: an incident-response team, diegetic threat *and* walking
  evidence (watching them work teaches you which laws they invoke).

Design consequence (intended): seams are finite wells priced in usage. Quiet variants
beat loud ones; hoarding beats spending; overpowered seams get used more and therefore
patch sooner — the economy self-balances without designer nerfs.

## 7. AI-GM constitution

**The AI never decides what happens; it decides what it's like.**

| Engine (sole authority) | AI-GM (sole authority) |
|---|---|
| Law resolution, experiment outcomes | Narration of engine results |
| Heat, patches, anomaly events | How a patch appears in fiction |
| Rote validation and binding | NPC dialogue, motives, factions, jobs |
| What instrumentation reveals | The texture/idiom of what it reveals |
| — | Fiction→action translation (echoed back, auditable) |

Codified in `PLAY.md` (the GM constitution), which any future Claude session reads to
pick up the campaign cold — including GM conduct rules: never leak seams, never override
engine output, always echo action parses.

## 8. Paradigm skins (the Root commitment)

The engine speaks neutral law-IDs and structured results. **Skins touch only
vocabulary**: a narration-layer mapping from law-IDs/seam-types to a tradition's idiom
(hermetic resonances, Virtual Adept race conditions, ecstatic intoxications). Black Ice
later = a venue pack whose entities are processes/hosts, whose ordinances are security
policies, whose heat is called *trace* — zero engine changes. If a skin ever needs an
engine change, the abstraction has been violated and the design revisited.

## 9. Progression

- **The grimoire is the progression.** Confirmed seams, refined rotes, venue-reads. It is
  a real artifact: human-readable files in the repo (auto-appended experiment log +
  hand-written hypotheses), Dropbox-synced, readable from a phone.
- **Arete advances by Seeking** — story-gated epiphanies triggered by breakthrough
  classes (first seam of a new type, first chained rote). No point-buy.
- **Campaign = venue + factions + clock.** v0: one venue, one faction conflict,
  3–5 sessions.

## 10. v0 scope

**Build:** Python engine (laws, actions, instrumentation filters, rotes, heat/patch
pipeline) · one hand-authored venue (a residential hotel: ~30 consensus laws, 5–6 seams
covering all 4 seam types) · CLI (JSON in/out) · PLAY.md · play-in-Claude-Code.

**Defer:** campaign generator, Black Ice skin, browser client, Arete 1/4/5, additional
venues, multiplayer anything.

**Known caveat:** with hand-authored campaigns the GM (Claude) rightly knows the seams,
but the player must not read `campaigns/` files — honor system in v0. The generator
dissolves this later.

**Success criteria (v0 done when all hold):**
1. The player forms an unprompted hypothesis before session 1 ends.
2. A seam confirmation lands as a genuine "aha" within two sessions.
3. A player-composed rote carries a story job.
4. A patch breaks a beloved rote and feels fair, not punitive.
5. Tuning a law or seam is a YAML edit — minutes, no code changes.

## 11. Architecture

```
consensus/
  engine/            # pure Python package — no I/O, deterministic given seed
    world.py         #   entities, typed properties, venues
    laws.py          #   law schema, resolution order, tick/event loop
    seams.py         #   seam types + metadata
    actions.py       #   mundane action vocabulary
    instruments.py   #   Arete-gated feedback filters
    rotes.py         #   rote schema, dry-run validation, role binding
    heat.py          #   three ledgers + patch pipeline
    session.py       #   THE public API: act() → structured result
  cli.py             # thin JSON-in/JSON-out wrapper for the GM
  campaigns/v0-hotel/  # laws.yaml, seams.yaml, scene.yaml — content is data
  grimoire/          # experiment log (auto) + hypotheses (hand-written)
  saves/             # serialized world state per session
  tests/             # pytest: resolution properties, golden experiment replays
  PLAY.md            # GM constitution
  notes/ docs/       # design memory
```

**Three load-bearing commitments:**
1. **Content is data.** Laws/venues/seams in YAML. This is the iteration loop now and the
   generator's output format later.
2. **The engine is a pure function** of (state, action, seed). Replayable, testable;
   every front-end — GM-Claude, browser, someday 3D — is just another caller of
   `session.act()`. No caller ever reaches around the API.
3. **Skins touch only vocabulary** (§8).

## 12. Testing

- Unit: law resolution order, condition evaluation, heat arithmetic, rote dry-run logic.
- Property: determinism (same state+action+seed ⇒ same result); serialization
  round-trips.
- Golden replays: scripted experiment sequences with frozen expected structured results —
  the regression net for law tuning.
- Playtest: the five success criteria in §10 are the real acceptance tests.

## 13. Risks

- **Fun risk (biggest):** hypothesis-testing gameplay lives or dies on cheap, fast, crisp
  experiment feedback. Mitigation: v0 exists precisely to tune this before any generator
  or UI investment; experiments resolve in seconds of table time.
- **Seam legibility:** too-subtle seams frustrate; too-obvious ones trivialize.
  Mitigation: difficulty = observations-to-distinguish (§3.3), tuned per seam in YAML.
- **AI boundary erosion:** GM improvising outcomes would corrupt the game's objectivity.
  Mitigation: PLAY.md constitution + the engine being the only source of outcome text
  structure.

## 14. First playable slice (implemented 2026-07-31)

The repository now contains a dependency-free deterministic engine, interactive shell,
GM constitution, and a deliberately tiny Hotel Limen scene. The slice has two seams:

- a scope gap in what the locked-door law counts as a witness;
- an ordering bug in which the first spoken account of a fall can settle before impact.

Both generate permanent signature heat, issue a diegetic advisory, and patch after loud
reuse. Seven automated checks cover the two control cases, the two exploits, patching,
Arete-gated feedback, immutability, and deterministic replay.

This is not yet evidence that the game is fun. It establishes that experiments can yield
stable, contrasting evidence without AI adjudication. The next acceptance test requires
a blind human playtest: the player must form a falsifiable hypothesis without reading the
campaign files. Avoid adding more laws until that test identifies whether feedback is too
obvious, too obscure, or genuinely satisfying.
- **Scope creep toward the 3D dream:** v0's only deliverable is a fun loop in text.
  Anything visual is v1+.
