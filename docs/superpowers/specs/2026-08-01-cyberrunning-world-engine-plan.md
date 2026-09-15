# CONSENSUS — Cyberrunning World Engine Plan

*2026-08-01 · status: proposed architecture and build plan · written after the Hotel
Limen text playtest and review of the 3D design · intended to amend, not discard, the
2026-08-01 3D spec*

## 1. The central model

A cyberrun is not a scripted mission and hacking is not a separate minigame. It is the
player moving through four connected graphs:

1. **Physical graph** — rooms, doors, vents, rooftops, people, carried objects.
2. **Network graph** — devices, hosts, links, sessions, daemons, data and trust edges.
3. **Authority graph** — identities, roles, credentials, permissions and institutional
   claims about what is allowed or true.
4. **Evidence graph** — sight, cameras, microphones, logs, documents and testimony.

Every useful runner action changes more than one graph. Stealing a badge is physical;
presenting it changes authority; a camera records the presentation as evidence; using
the badge creates a network log. Cutting power changes physical affordances, network
reachability, surveillance and therefore consensus enforcement.

**The unifying design statement is: cyberrunning means manipulating claims and the
evidence that makes systems accept them. Magic does the same thing at reality's level.**

This is the Root architecture in playable form. Mundane security, cyberspace intrusion
and reality hacking share concepts without becoming identical activities.

## 2. Authority boundary — revised after the text playtest

The pure reality kernel must not decide every mundane outcome. The Hotel Limen session
showed why: ordinary intentions such as taking a key, closing a door, moving an NPC and
using a telephone repeatedly exceeded a fixed action vocabulary. A real-time immersive
sim would multiply this failure.

| Layer | Owns | Must not own |
|---|---|---|
| **Godot simulation** | Movement, collision, forces, projectiles, animation, spatial raycasts, audio propagation, immediate controls | Consensus rules, heat, patches |
| **Cyberrunning world model** | Entities, inventory, doors, devices, network state, credentials, schedules, evidence, alerts, job predicates | Frame-by-frame character physics, metaphysical outcomes |
| **Consensus kernel** | Consensus claims, law ordering, seams, instrumentation, anomaly resolution, heat, advisories, patches | Geometry, AI navigation, ordinary container logic |
| **Narrative layer** | Dialogue, motives, job framing, authored text and presentation | Mechanical success, law results |

The runtime exchange is:

```text
player input
  → Godot proposes a physical/social/network event
  → world model supplies authority, network and witness context
  → consensus kernel intervenes only when a law subscribes to that event
  → final discrete state changes are committed
  → Godot renders them and observers create evidence
  → security, trace and heat react
```

Godot is authoritative about where a ray hits. The consensus kernel is authoritative
about whether the resulting account becomes reality. These are different questions.

## 3. Claims and evidence — the shared substrate

### 3.1 Claims

A claim is a structured assertion made by a person, device or institution:

```json
{
  "id": "claim-184",
  "subject": "service-door",
  "predicate": "access_state",
  "value": "locked",
  "source": "door-controller",
  "authority_domain": "hotel-security",
  "evidence": ["obs-991", "log-204"],
  "valid_from": 8821,
  "valid_until": null,
  "priority": 40
}
```

Examples include “this badge holder is staff,” “this door is locked,” “Nadia occupies
Room 404,” “the camera saw the player enter,” and “this process is trusted.” Mundane
systems and consensus laws may accept different sources for the same claim.

### 3.2 Evidence

Evidence records how a claim became supportable:

```json
{
  "id": "obs-991",
  "event_id": "event-552",
  "observer": "lobby-camera",
  "modality": "optical_record",
  "account": {"actor": "player", "action": "opened", "target": "service-door"},
  "latency": 0.2,
  "persistence": "recorded",
  "tamperability": "networked",
  "scope": "hotel-security"
}
```

Modalities are data, not flavor: direct sight, remembered testimony, optical record,
audio record, biometric reading, network log and institutional document. Each has
deterministic latency, persistence and tamperability.

Security consumes evidence to raise suspicion and alerts. Reality consumes evidence to
settle consensus claims. Hacking attacks evidence production and delivery; magic attacks
the rules by which reality accepts it.

## 4. Discrete event lifecycle

Important actions pass through explicit phases:

1. **INTENT** — actor, verb, target and tool are declared.
2. **CONTEXT** — Godot snapshots relevant spatial facts; the world model adds credentials,
   network reachability, observers and active claims.
3. **PROPOSE** — mundane systems propose outcomes and state deltas.
4. **ADJUDICATE** — subscribed consensus laws accept, reject, delay or replace deltas.
5. **COMMIT** — final state changes become authoritative.
6. **OBSERVE** — sensors and people produce modality-specific evidence.
7. **REACT** — NPC suspicion, facility alert, network trace and heat update.
8. **SETTLE** — delayed accounts and race windows close.

The existing seam taxonomy maps directly to this lifecycle:

- **Scope gap:** CONTEXT queries the wrong observer, identity or entity class.
- **Ordering bug:** two ADJUDICATE or SETTLE processors run in the wrong order.
- **State confusion:** different processors read incompatible views of one entity.
- **Race window:** COMMIT and SETTLE leave a usable interval.

The lifecycle, not a fixed list of player verbs, is the kernel contract. New mundane
interactions can produce existing event shapes without requiring a metaphysical spec
change.

## 5. The four graphs

### 5.1 Physical graph

Godot owns continuous geometry. The world model stores only discrete relationships that
matter to simulation: `inside`, `connected_by`, `carried_by`, `mounted_on`, `powered_by`
and `controls`.

Rooms and outdoor areas are zones; doors, vents and climbable transitions are portals.
Godot reports line of sight and acoustic reach at the moment an event needs them. The
kernel never performs raycasts.

### 5.2 Network graph

Nodes are actual world devices and hosts, not arbitrary puzzle geometry. Edges have
medium, direction, trust, bandwidth and current reachability. A camera is simultaneously
a physical sensor, network endpoint, evidence producer and authority source.

Initial network operations:

- **probe** — reveal exposed properties and services;
- **authenticate** — present a credential or session claim;
- **spoof** — make a target accept a false identity or source;
- **pivot** — move execution context along a trust edge;
- **splice** — reroute a live signal or relationship;
- **suppress** — delay or prevent evidence delivery without erasing its source;
- **extract** — copy a data asset;
- **disconnect** — sever the runner's session.

There is no generic `hack` command. Programs package operations, but player mastery is
reading topology, trust and consequences. ICE consists of daemons subscribed to network
events; it traces, isolates, lies, counter-probes and attacks the runner's session.
Trace is accumulated evidence, not an enemy health bar.

The eventual Neuromancer-like cyberspace is a renderer of this graph. It must never be a
different simulation with decorative links to the physical world.

### 5.3 Authority graph

Authority answers “which claims does this system accept from whom?” It includes access
control, employment roles, social cover, device trust and institutional jurisdiction.

A credential is not a colored key. It is a portable claim with issuer, subject, scope,
expiry and revocation state. A stolen badge may open a door while failing a face check;
a spoofed maintenance ticket may persuade a porter while leaving a suspicious network
log. Multiple partial truths create runner improvisation.

### 5.4 Evidence graph

Observers create evidence; communication edges deliver it; repositories preserve it.
There is no instantaneous global alert. A guard must see, infer and report. A camera must
record and reach a controller. A controller must classify and notify responders.

This makes stealth, social manipulation and hacking systemic:

- block the sightline;
- impersonate someone the guard expects;
- splice the camera feed;
- suppress the alert message;
- alter the shift report;
- exploit a consensus law that ignores that modality.

## 6. Cyberrunning world state

The discrete state should remain serializable and inspectable:

```text
WorldState
  clock / event_sequence / seed
  entities
    actors, items, portals, devices, hosts, data assets
  relations
    physical, network, authority, evidence
  claims / observations / active sessions
  security
    suspicion per actor, alert per zone, trace per network session
  consensus
    active laws, seams, heat, advisories, patches
  jobs
    objective and constraint predicates
```

Godot nodes carry stable entity IDs. They are views/controllers for model entities, not
independent copies of important state.

Use component-shaped data, but do not build a general-purpose ECS before the first run.
Only extract a component when two concrete entity types need it.

## 7. Security and failure

Security is local and evidence-driven:

```text
routine → curious → investigate → contain → hunt
```

Suspicion belongs to an observer; alert belongs to a zone or organization; trace belongs
to a network session. They communicate with latency. Destroying one camera does not give
every guard psychic knowledge of the player.

Combat emits loud evidence: sound, injury, missing check-ins, ballistic traces and
network alarms. It is a legitimate solution, but it creates more evidence and therefore
more routes for security and consensus to react.

Failure should normally transform the run: a route closes, cover is burned, evidence
strengthens, reinforcements arrive or the objective moves. Death/reload remains available
for terminal combat failure, but ordinary discovery should not be erased.

## 8. Jobs are predicates, not scripts

A job defines desired world facts and optional constraints:

```json
{
  "complete_when": ["player possesses municipal-packet", "player is outside hotel"],
  "bonuses": ["no civilian injured", "packet access unlogged"],
  "fail_when": ["packet destroyed"]
}
```

The mission may author factions, dialogue and spaces, but not a required solution
sequence. Physical, social, network, combat and consensus approaches all operate on the
same state until an objective predicate becomes true.

## 9. Reality integration

Only events tagged by subscribed laws enter consensus adjudication. A footstep is not a
kernel call unless a local ordinance cares about footsteps. An access-controlled door,
a witnessed injury or a contested identity probably is.

The Lens visualizes event-local information:

- base glint: a consensus processor fired here;
- attribution: which law family fired;
- introspection: which supplied context facts it read;
- stepping: processor order and proposed deltas.

The Lens must not become a passive room scanner. Holding it reveals recent or active
signals, not unexecuted rules or omniscient “consensus status.”

Rotes store successful procedures over roles and event conditions. The game never asks
the player to state the hidden source rule correctly. A procedure becomes **proven**
after reproducible success; the workbench validates bindings and observed dependencies,
not prose reasoning.

Vulgar forcing is not automatically meaningful for every seam. Each authored seam must
define a specific forceable delta, cost and visual expression. If a seam cannot support
probe, rote, field use and patch behavior, it does not belong in the vertical slice.

## 10. First playable cyberrun — Hotel Limen

Reuse the strongest fiction from the text test, but rebuild it as a systemic run.

**Job:** obtain a Municipal Continuity packet from Hotel Limen and leave the block.

**Space:** one compact building rather than a city block: lobby, alley, service corridor,
records office, stairwell, two guest rooms and a roof transition.

**Actors:** porter, security guard, food runner and one guest. Four routines, not twelve.

**Devices:** two cameras, two access-controlled doors, records terminal, switchboard and
one exposed maintenance port.

**Mundane approaches:** steal a credential; persuade the porter; climb through the roof;
probe and spoof the door controller; fight and escape.

**First seam:** the threshold-stability law accepts direct human sight but not optical
records. Cameras still generate mundane security evidence, so exploiting reality does
not automatically defeat hotel security.

**Learning sequence:**

1. A witnessed door resists and produces a localized glint.
2. The player can change human and camera sightlines independently.
3. A clean camera-only attempt discriminates the scope gap.
4. Reproducing it records a proven procedure.
5. The procedure provides an elegant route to the packet.
6. Repetition raises signature heat; an advisory changes camera policy before a later
   patch makes optical records valid consensus witnesses.

The job must remain completable after the patch by every mundane approach.

## 11. Build plan — gates, not one giant Stage 1

### Gate 0 — Contracts

- Define entity IDs, event phases, claims, evidence and state-delta schemas.
- Refactor the Python kernel to accept event context rather than own all mundane actions.
- Freeze five golden fixtures for the threshold seam.

**Pass when:** a door event can be resolved from a supplied human/camera witness snapshot
without any geometry or narrative code in Python.

### Gate 1 — Feel lab

- Create the Godot project.
- Implement walk, run, one mantle and object interaction.
- Add Lens pulse, one localized glint and its audio motif.
- Use one grey room and one door; no jobs, AI, combat or journal.

**Pass when:** moving, interacting and locating a glint is pleasant for five minutes with
all progression systems absent.

### Gate 2 — Mundane cyberrun lab

- Build the compact hotel shell.
- Add portals, inventory, credentials, two cameras and two simple NPC routines.
- Implement local suspicion, delayed reporting and zone alert.
- Add the minimal network graph with `probe`, `authenticate`, `spoof` and `suppress`.
- Implement the packet job as state predicates.

**Pass when:** the packet can be obtained by physical, credential and network routes with
the consensus kernel disabled.

### Gate 3 — Reality lab

- Port only the threshold seam and supporting laws to GDScript.
- Query witness facts from Godot at event time.
- Add glint, attribution and raw experiment log; no Arete 3 yet.
- Run the same golden fixtures against Python and GDScript.

**Pass when:** a blind tester notices the anomaly and constructs the camera-only
comparison without being asked to state a hypothesis.

### Gate 4 — Procedure and consequence

- Turn a reproducibly successful setup into a role-bound procedure.
- Add field binding assistance without revealing unfound conditions.
- Add local/signature/personal heat, a local advisory and one visible patch.
- Ensure all consequence information obeys spatial and sensory locality.

**Pass when:** the tester deliberately reuses the procedure, anticipates the risk, sees
the patch and completes the job another way.

### Gate 5 — Combat lab

- Add one pistol, one enemy archetype and one takedown.
- Make sound, injury and missing status checks produce evidence.
- Define one explicit vulgar application of the threshold seam, or reject the seam as a
  combat seam if no coherent application exists.
- Add accessibility controls immediately, not after tuning.

**Pass when:** combat is viable, evidence-loud and meaningfully altered by knowledge,
without being required for the packet job.

### Gate 6 — Integrated vertical slice

- Add the second seam only now.
- Add Arete 3 traces, the workbench, one gadget and a lightweight response team.
- Expand the single run into the three-beat onboarding/job arc only if earlier gates pass.
- Improve lighting and audio without increasing geographic scope.

This is the point corresponding to the old document's “Stage 1.” It is a milestone, not
the first implementation task.

## 12. Explicit deferrals

- Full block and twelve NPC schedules
- Belief field and infrastructure simulation
- Separate full-3D cyberspace traversal
- Full Python/GDScript feature parity
- Multiple weapons, augments and advanced enemy AI
- Suits organizational adaptation
- Generator, Black Ice campaign and paradigm skins
- AI narrative director

The network semantics must be correct from Gate 2, but Neuromancer-style visualization
waits until those semantics are fun in a plain interface. Rendering a weak graph in 3D
would make it expensive, not deep.

## 13. Decisions this plan proposes

1. Claims and evidence, not verbs, are the common substrate.
2. Godot owns ordinary physical outcomes; the kernel owns consensus intervention.
3. The witness graph is a supplied event snapshot backed by Godot geometry.
4. Cybersecurity and consensus both consume the evidence graph under different rules.
5. Network intrusion is concurrent with the physical world and affects real devices.
6. Rotes are proven procedures, not graded answers.
7. The first test venue is one building, not one block.
8. The existing Stage 1 becomes Gate 6 after five smaller go/no-go tests.

These decisions should be reviewed before changing the canonical 3D spec or beginning
the Godot project.

