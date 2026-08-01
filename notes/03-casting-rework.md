# Casting Mechanic — Rework History (2026-07-31)

The core mechanic went through three versions during brainstorming. Recording all of them
because the *rejections* define the design space as much as the final choice.

## v1 — The Interpreter model (REJECTED)

English casting surface → AI compiles to a visible DSL (premise / leverage / cover) →
player may edit → engine scores deterministically. Mastery = sliding from English toward
raw DSL.

**Rejected because:**
- The "least charitable compilation / mishearing" felt punitive and gimmicky.
- The DSL read like pseudocode — magic felt like programming.
- The premise/leverage/cover anatomy was the wrong decomposition of a magical act.

## v2 — The Web of Correspondences (REJECTED)

The world's hidden structure is a weighted graph of sympathies (similarity, contagion,
name, opposition), with edge weights from universal lore + local consensus + personal
resonance. A spell = a path from an anchor you hold to a target, pushing a working down
the chain. Strain on weak edges = Paradox. New edges argued into the grimoire in downtime
(the one AI-adjudicated act).

**Rejected because (all of these):**
- Casting collapses into shortest-path lookup once the web is known — rote, no living skill.
- Too folk-magic; loses Mage's range and the "hacking reality" feel.
- Authoring burden: a pre-built graph feels finite, arbitrary, database-like.
- Chain-laying is an abstract mini-game floating above the fiction.
- User's own words: **"where's the skill of the player in learning to adapt/hack reality?"**

## v3 — Exploit Research ("Reality is a system with bugs") — CURRENT DIRECTION

The buried assumption v1/v2 shared: the rules of magic were KNOWN, and player skill was
composition within them. But a hacker's skill is *epistemic* — the system is opaque; the
craft is discovering its rules by probing, exploiting the seams, adapting when patched.

**The model:**
- The engine simulates reality as a rulebase of laws (condition/effect rules over world
  state) with **hidden internals**, generated per campaign with **seeded seams** — real,
  consistent, discoverable bugs (ordering conflicts, unhandled edge cases, scope
  confusions).
- Magic is not a language; it's research. The Awakened get *instrumentation*, not spells.
- **Character (Arete) = the debugger.** R1: feel a law fire (anomaly sense). R2: see which
  law. R3: read its conditions. R4: single-step a small region of reality. R5: brief,
  catastrophic write access (maximally vulgar).
- **Player = the scientist.** Observe anomalies → hypothesize → design experiments (acts
  in the fiction: drop the coin, close the curtain, no witnesses, say it twice) → engine
  resolves against the true hidden rulebase → build **exploits** (arrangements of scene
  elements that trigger a seam). Grimoire = lab notebook.
- **Consensus = self-patching immune system.** Overused/loud exploits get flagged; flags
  draw the patch (debunking headline, new regulation, men in gray). Paradox = detection
  heat. Technocracy = reality's security operations center. Exploit libraries decay; the
  durable skill is the METHOD (hypothesis-craft), not the answers.
- Traditions = research methodologies (skins on the same discovery): the Hermetic reads a
  seam as "a resonance of Mars," the Virtual Adept as a race condition, the Ecstatic finds
  it by getting the world's laws drunk.
- Progression = knowledge (Outer Wilds principle). Stats gate observation, never
  understanding — "stats buy a better oscilloscope, not the physics degree."

**How it answers the four v2 objections:**
1. Lookup → seams are hidden, per-campaign, and self-patch when overused.
2. Folk-magic → it's reverse-engineering the universe; traditions are methodologies.
3. Authoring → laws generated from templates with guaranteed seeded seams. (v0 honesty:
   hand-craft one venue's rulebase first to prove fun, then build the generator.)
4. Board-gamey → no abstract layer; experiments and exploits are acts in the fiction.

**Architecture bonus:** Black Ice becomes literally the same loop (probe opaque corporate
system, find seams, manage detection heat) at a smaller scale. Root's fusion reveal:
reality's SOC and the corps' SOCs are the same org chart. One engine, one loop, two scales.

**Status:** presented to user, awaiting approval.
