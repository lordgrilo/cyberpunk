# Game Design Principles — the fished canon

*2026-08-01 · the foundation pass requested before the 3D redesign. Each principle:
what it says, where it comes from, the exemplar games that prove it, and — the part that
matters — what it **demands of our game**.*

---

## 1. MDA: design the feeling, derive the rules

**Mechanics → Dynamics → Aesthetics** (Hunicke, LeBlanc & Zubek, 2004). Designers author
mechanics; players experience aesthetics (the feelings); dynamics are the runtime behavior
that emerges between. Players consume the stack in the opposite direction from how
designers build it — so design *backwards from the target feeling*. MDA's "8 kinds of
fun": sensation, fantasy, narrative, challenge, fellowship, discovery, expression,
submission.

**Demands of us:** declare target aesthetics FIRST and reject mechanics that don't serve
them. Ours (ranked): **discovery** (the world hides real structure), **expression** (my
solution is mine), **challenge** (competence under pressure), **fantasy** (being the one
who sees the code of the world). Fellowship/submission are non-goals.

## 2. Koster: fun is learning; games die when the pattern is exhausted

*A Theory of Fun* (Koster, 2004). The brain enjoys grokking patterns; fun is the dopamine
of successful pattern acquisition. Corollary: a game is dead the moment its pattern is
fully learned — "grinding" is what remains. Most games fight this with content volume
(expensive) or randomization (cheap but shallow).

**Demands of us:** our core loop must *manufacture new patterns* structurally. The
patch/heat economy (exploits decay when used loudly; reality re-seeds) is our answer —
learning is not just the reward, it's the consumable resource. This is our single biggest
theoretical asset: a game whose content IS learning has Koster's problem as its engine
rather than its doom.

## 3. Flow: challenge must track skill, with clear goals and immediate feedback

Csikszentmihalyi's flow channel, imported into games everywhere (notably Chen's *flOw*
and Schell's *Art of Game Design*). Anxiety above, boredom below; the channel requires
(a) clear goals, (b) immediate feedback, (c) challenge ≈ skill.

**Demands of us:** hidden rules are in *tension* with clear goals and immediate feedback
— this is our central design risk. Resolution: the *rules* are hidden but the *feedback*
is instant and honest (every probe visibly does something), and goals are always concrete
(the job, the hypothesis to test). Mystery in the model, never in the interface.

## 4. Self-Determination Theory: competence, autonomy, relatedness

Ryan & Deci's SDT, applied to games by Rigby & Ryan (*Glued to Games*, 2011) — the best
empirical account of why games satisfy. **Competence**: felt growth of ability.
**Autonomy**: acting from volition, meaningful choice of approach. **Relatedness**:
mattering to others (including NPCs).

**Demands of us:** competence = the knowledge arc (I understand what I didn't) must be
*visible* — the grimoire as a trophy room of understanding. Autonomy = never one intended
solution (see 6). Relatedness = factions and NPCs who remember, and who *need* what only
your research can do.

## 5. Second-order design: author the system, not the situations

The systemic-design school: the designer's product is a *possibility space*, and gameplay
is what the space affords (LeBlanc's "emergence"; Smith & Worch's environmental/systemic
talks; canonically demonstrated by *Breath of the Wild*'s GDC 2017 "multiplicative
gameplay" — a small chemistry of elements × a large set of objects = combinatorial
situations no one authored; also *Dwarf Fortress*, *Rain World*, *Shadows of Doubt*).
Rule of thumb: N systems that all interact beat 10×N scripted encounters.

**Demands of us:** the city must run on a small set of REAL interacting simulations
(observation, belief, schedules, power, traffic…), and the consensus laws must govern
*interactions between systems* — because that's where our seams live. We never author
"the puzzle"; we author laws whose intersections contain puzzles. This is also our scope
weapon: systems are cheap relative to content.

## 6. The immersive-sim creed: problems, not puzzles

Looking Glass → Ion Storm → Arkane lineage (*Ultima Underworld*, *Thief*, *Deus Ex*,
*Dishonored*, *Prey*). Spector's formulation: present *problems* with multiple systemic
solutions, never *puzzles* with one authored answer. Tenets: a consistent, simulated
world that honors its own rules everywhere; player intention and improvisation beat
designer scripts; if the simulation says it should work, it works; levels are dense
possibility spaces, not corridors. (Also the honest warning from this school's history:
these games are expensive per square meter — they choose density over acreage.)

**Demands of us:** every run completable by mundane play (stealth, social, tech); magic
*multiplies* options and never gates the critical path. And the creed gives us our
identity twist: in every immersive sim the world-rules are consistent — in ours,
*investigating that consistency is the gameplay*. The genre's contract becomes the
content.

## 7. Player skill taxonomy: choose where mastery lives

Skill in games decomposes into **execution** (mechanical dexterity), **strategy**
(decision quality under constraints), **knowledge** (knowing the world/system), and
**social** reads. Games are defined by their mix (fighting games: execution; roguelikes:
strategy+knowledge; souls games: execution+knowledge). The purest knowledge-progression
games (*Outer Wilds*, *La-Mulana*, *Tunic*, *The Witness*, *Fez*) gate progress by
*understanding alone* — Outer Wilds' design (Beachum's "curiosity-driven exploration")
proves a whole game can run on it.

**Demands of us:** declared mix — **knowledge primary, strategy secondary, execution
tertiary** (light, accessible, never the wall). Character stats gate *perception
bandwidth*, never understanding. This was already our stat/skill contract; the taxonomy
says it out loud so combat/traversal tuning never drifts into execution-gating.

## 8. Loops at every timescale

Standard loop analysis: a game must be satisfying at second-to-second (feel),
30-second (tactic), 5-minute (encounter/errand), session (arc), and campaign
(meta-progression) scales — each loop feeding the one above. Where a scale is hollow,
players churn (many systemic games fail at the 2-second scale; many action games at the
session scale).

**Demands of us:** we must be honest that our old text-v0 had *no* second-to-second loop
— in 3D we owe one: movement + perception (Lens toggling, anomaly glints) must feel good
*in the hands*, independent of the research meta. Explicit loop budget in the vision doc.

## 9. Game feel and legibility: juice is information

Swink's *Game Feel*: real-time control + polish that communicates state. Nintendo's
visual-language discipline; "juice" done right is *feedback*, not decoration. For system
games: **a system the player can't read is a system that doesn't exist** (BOTW
telegraphs everything: green stamina, red heat shimmer, metal sparks before lightning).

**Demands of us:** the hidden-rulebase premise survives ONLY with fanatical feedback
discipline: every law-firing casts a *visible shadow* (shimmer, sound motif, glyph) even
before you can interpret it; instrumentation tiers change *interpretation*, not
*existence*, of signals. Fair-mystery rule: the player must always be able to say "THAT
was weird" — figuring out *why* is the game.

## 10. Bushnell's law and teaching through play

"Easy to learn, hard to master." The best onboarding is level design (Nintendo's
kishōtenketsu structure; Half-Life 2's silent tutorials; *Plants vs Zombies*' drip-feed).
Depth must be layered so the first hour needs none of it.

**Demands of us:** the first hour is a *mundane* cyberrunner job that works entirely on
traversal/stealth/social — and one anomaly glint planted in it. Awakening (the Lens) is
earned in play, and the first seam is confirmed inside a designed "teaching venue" whose
law-shadow is loud. Research depth (hypothesis journal, rote workbench, chaining)
unlocks strictly on demonstrated use, not menus.

## 11. Open-world lessons: reactivity is the currency, density beats acreage

The GTA lineage is a *theme park* — broad, gorgeous, mostly non-reactive with systemic
toys. Cyberpunk 2077's launch taught the negative lesson: promising a systemic city and
shipping a scripted one destroys trust; its later redemption came from focusing
reactivity where the player actually is. BOTW's triangle-rule landmark wayfinding;
Deus Ex/Dishonored hub density as the immersive-sim alternative to sprawl.

**Demands of us:** ONE district, dense and deeply reactive, not a city wide and dead.
Reactivity budget spent where our fantasy needs it: the world visibly *re-explains*
anomalies (consensus doing its work) and visibly *changes* after patches. A block that
remembers beats a skyline that doesn't.

## 12. Ludonarrative harmony: the mechanic is the message

Hocking's "ludonarrative dissonance" critique; Romero's *Train* ("the mechanic is the
message"); the strongest games say their theme *in rules* (Papers Please: complicity by
paperwork; Outer Wilds: acceptance by cosmology).

**Demands of us:** our theme — *who gets to define what's real, and what it costs to
dissent* — must be said by the rules: consensus literally overwrites deviant events
(witness mechanics), patches literally rewrite the neighborhood (world mechanics), and
the Technocracy is literally an incident-response bureaucracy (antagonist mechanics).
No cutscene should carry what a law can.

## 13. Economy design: sources, sinks, and self-balancing pressure

Virtual-economy fundamentals (Castronova; Simpson's classic sources/sinks analyses) plus
consequence systems as economies (*Dishonored*'s chaos; nemesis-style escalation — note:
WB's Nemesis-system patent (US 10,926,179, expires 2036) means we design escalation
around *organizational memory*, not resurrecting named rivals).

**Demands of us:** already designed and it survives the pivot intact — the three heat
ledgers with non-decaying signature heat. The principle to hold: **never balance by
designer nerf what the economy can balance by price.** Overpowered seams get overused,
therefore patched soonest. Keep it.

## 14. Difficulty, failure, and fairness

Failure must teach (roguelite school: death as information; *Celeste*'s assist-mode
philosophy: challenge is the point, walls are not). Juul's "paradox of failure": players
seek games that make them fail *creditably*.

**Demands of us:** failed experiments are never wasted — a disconfirmed hypothesis
updates the journal (visible progress). Failed runs raise heat, not game-overs; the
Technocracy escalates rather than kills. The one true loss is *grimoire compromise* —
losing knowledge, the only currency — and even that should be theft-by-rival (story
fuel), not deletion.

---

## The tensions (where principles fight, and our rulings)

1. **Hidden rules (2,7) vs. clear feedback (3,9).** Ruling: hide the *model*, never the
   *signal*. Every law-firing is perceivable; only its meaning is earned.
2. **Systemic openness (5,6) vs. teaching (10).** Ruling: hand-authored teaching venues
   with loud seams early; the open district after the player owns the method.
3. **Open-world fantasy (GTA/C77 dream) vs. density economics (6,11).** Ruling: one
   dense district now; acreage is a sequel problem. The dream is the *feel* of a living
   neon city, which density delivers and acreage doesn't.
4. **Knowledge progression (7) vs. replayability.** Ruling: campaign reseeding (the
   generator) — the method transfers, the answers don't. Accepted cost: first campaign
   is the deepest; that's true of Outer Wilds too and it's fine.
5. **Player expression (1,4) vs. balance.** Ruling: the heat economy prices expression
   instead of forbidding it. Broken combos are *expensive*, not blocked.

## Reading/watching list (for remote evenings)

- Hunicke, LeBlanc, Zubek — *MDA: A Formal Approach to Game Design* (2004 paper, free PDF)
- Koster — *A Theory of Fun for Game Design*
- Schell — *The Art of Game Design: A Book of Lenses* (esp. lenses on curiosity, skill, visible progress)
- Rigby & Ryan — *Glued to Games*
- Swink — *Game Feel*
- GDC 2017: *Breaking Conventions with The Legend of Zelda: BOTW* (the multiplicative-design talk)
- GDC 2015: Alex Beachum — outer Wilds' curiosity-driven structure (*Death, Curiosity, and the Quantum Moon* / his USC thesis "Outer Wilds: A Game of Curiosity-Driven Space Exploration")
- GDC talks by Harvey Smith & Randy Smith on Thief/Deus Ex/Dishonored systemic design
- Juul — *The Art of Failure*
- Sylvester — *Designing Games* (loops & skill ceilings, very practical)
