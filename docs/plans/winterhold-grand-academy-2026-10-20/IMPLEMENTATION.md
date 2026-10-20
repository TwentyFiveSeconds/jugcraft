# Grand Academy implementation ledger

The contributor supplied this planning package on 20 October 2026. It is design intent; proposed rooms and mechanics are not implementation claims.

The saved circular-campus prototype is commit e03c341 on feature/frostward-academy, draft PR #441. Continue that branch rather than discarding recovered work. Current upstream main c27afcd adds drilling/Chima; open factory/economy PRs are not academy dependencies.

M0 next slice: localized client snow/mist, one persistent Radiance instructor using the existing townsfolk model, the existing Concordance journal/benches, and courtyard secret S01 with per-player lore credit. Reuse the saved geometry and update its runtime layout data for actual anchor/controls. No extra rooms, progression engine, global weather change or natural generation in this slice.

The runtime layout remains tools/winterhold_layout.json: 145 x 76 x 161, origin northwest bottom, courtyard walking Y=25, monument X/Z=68/85. Proposed sizes/room graph in data/layout.json are long-term targets, not placed dimensions. The first-stage climate geometry must match the runtime footprint.

Room mapping: EXT-01 bridge; EXT-02 gate frame (full vestibule pending); EXT-03 courtyard/cloister; ELM-01 main teaching floor. Existing additional rooms remain prototypes, not completed M1-M5 milestones.

AI assistance: OpenAI Codex (GPT-6); the existing PR records the model-policy exception for maintainer review.
