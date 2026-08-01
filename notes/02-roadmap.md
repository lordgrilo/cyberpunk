# Roadmap — SUPERSEDED 2026-08-01

> **This staging is superseded by the 3D pivot.** Current staging lives in
> notes/05-3d-vision.md §5 (Stage 0 kernel testbed → Stage 1 grey-box slice →
> Stage 2 the Ward → Stage 3 the dream). Kept below for history: the "engine stays
> headless, visuals are a client" principle carried over unchanged.

# (old) Roadmap — easiest first, without closing the 3D door

Principle: the *system* is the product right now. Visuals are a client. The engine must
stay headless (a pure library with a clean API + serializable state) so any front-end —
chat, browser, eventually a 3D world — can drive it.

## v0 — The engine + play-in-Claude-Code (NOW)

- Headless engine: substrate call model, Consensus spell language (parse → score →
  resolve), Paradox accounting, venue/consensus profiles, world state as plain data.
- Playtest harness: play sessions inside Claude Code. Claude is the GM (narration, NPCs,
  coincidence-wrapper adjudication); the engine adjudicates structure, scoring, Paradox.
- Success criteria: the spell language is *fun to think in*. A playtester gets visibly
  better across sessions (player skill is real). Iterating on the language costs minutes.

## v1 — Browser client + Claude API

- Thin web UI: spell composition editor (with the sigil/argument structure visible),
  world/venue display, Paradox meter, session log.
- Claude API supplies the GM layer. Engine runs client-side or in a small server.
- Second paradigm skin lands here or late v0: Black Ice exploit language over the same
  substrate calls.

## vFuture — Real game

- Long-term stated dream: GTA / Cyberpunk 2077-class visual world.
- The engine is the magic system inside that game; substrate calls become the gameplay
  API that the 3D world implements (a "lock opens" call has a mesh + animation there,
  a sentence of narration here).
- Nothing in v0/v1 should assume text — effects are structured data, narration is a
  *rendering* of them.
