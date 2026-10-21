# Frostward College rebuild progress

Updated 21 October 2026. Continuation branch: `feature/frostward-college-rebuild`, from upstream `main` at `38f1f809001d5d1415f7e77524be94320d469350`. PR #447 is merged; #441 is closed and historical. This file is the one session continuity ledger. AI assistance: OpenAI Codex (GPT-6).

## Reference-to-template decision

The supplied numbered Winterhold floorplan controls the seven-landmark connection hierarchy. The two supplied Minecraft images control the recognizable bridge-facing hall and curved court silhouette. [The labeled comparison](../images/frostward-footprint-comparison.svg) places those interpreted relationships beside the measured merged template and this branch's template. The comparison's first panel is qualitative because the reference has no Minecraft coordinate scale; its other two panels use `tools/winterhold_layout.json` coordinates. The [generated plan](../images/frostward-academy-revised-plan.png), [bridge projection](../images/frostward-academy-revised-bridge.png), and [overview](../images/frostward-academy-revised-overview.png) are from the actual NBT cells, not game screenshots.

Entrance-relative orientation is defined looking north from the bridge: Attainment is left/west; Countenance is right/east. The bridge reaches the circular court. The Hall dominates the north axis. Arcanaeum joins on the Hall's right/east through a widened two-room academic cross-wing. Arch-Mage upper quarters now extend as a separate western annex linked by an enclosed gallery. This follows landmark relationships without tracing the reference image's compass angles.

| Landmark | Merged template | Current branch |
| --- | --- | --- |
| Bridge 1 | narrow approach ending directly at court | approach retained; gatehouse at X60–76, Z114–126, Y24–42 |
| Court 2 | center (68,85), outer radius 33, open inner radius 25 | center retained; outer radius 30, inner radius 23, two accessible roof stairs |
| Attainment 3 | center (27,76), radius 14 | distinct west residence retained, door and roof access tested offline |
| Countenance 4 | center (109,92), radius 14 | distinct east residence retained, door and roof access tested offline |
| Elements 5 | center (68,33), existing tall mass | tall mass retained; academic cross-wing now joins Hall to library |
| Arch-Mage 6 | rooms above Elements | upper study/garden retained; west annex centered (43,33), radius 12, one furnished bed and storage |
| Arcanaeum 7 | center (112,34), radius 22, narrow link | existing stacks retained; cross-wing X83–97, Z20–48 adds north/south study rooms and broad arches |

The template remains **145 × 76 × 161**, with **286,061 cells and 72 palette states**. This is the first corrected shell, not the completed large College. Its outer bounds and much of the original room volume have not yet grown. The floorplan and Minecraft view must be reassessed in game before deciding the next proportion changes; the present code projection still shows repeated round masses and a court that can read too broad.

## Implemented and verified status

| Slice | Implemented | Visually reviewed | Gameplay verified |
| --- | --- | --- | --- |
| Gatehouse and two reception bays | generator and NBT | generated plan and bridge projection inspected; current Minecraft capture pending | offline two-block navigation passed; new GameTest added, runtime pending |
| Court, residences and guarded cloister roof stairs | radius revision, roof stair flights, original beds/doors/stations retained | generated plan inspected; current Minecraft capture pending | offline two-block navigation passed; physical collision/walk pending |
| Hall–Arcanaeum academic cross-wing | enclosed roof, two rooms, six broad connections, stone detail and furnishings | generated plan/bridge projection inspected; interior Minecraft capture pending | offline route passed; new GameTest added, runtime pending |
| Arch-Mage west annex | connected upper gallery, shelves, desk, usable bed, barrel and windows | generated bridge projection inspected; interior Minecraft capture pending | offline route and bed-pair checks passed; sleep/storage in game pending |
| Permanent local autumn slice | zero snow blocks; 28 supported leaf piles; four pumpkins; continuous camera-local leaf fragments and existing mist | generated plan inspected; actual particle/lighting capture pending | Python palette/support passed; client off/low/minimal, boundaries, two-client and frame cost pending |
| Arctus Vale, S01 and Concordance | merged implementation preserved, no new progression grants | historical Minecraft views only | historical PR #447 tests passed; new branch runtime pending |

[The 43-point room and anchor ledger](frostward-room-ledger.csv) records coordinates, connected route, purpose, working interaction or placeholder, persistence/reset, NPC use, and current evidence for every named point in the layout. `tools/winterhold_layout.json` is the coordinate authority. A route passing the offline voxel walker does not certify Minecraft collision, NPC pathfinding or a player's actual traversal.

## Checks on this branch

- `python tools/winterhold_academy.py` regenerated the committed NBT; `--check` is the freshness gate.
- `python -m unittest discover -s tools -p test_winterhold_academy.py -v`: **10/10 passed**. Covers deterministic NBT, bounds, stations, bed/door support, snow removal, groundcover support and 43 room/anchor routes.
- `node tools/preview_winterhold_layout.mjs`: **passed** with 13,934 reachable standing positions, eight doors, 16 bed halves, eight signs, zero snow blocks and 43 room/anchor points.
- `compileJava compileClientJava compileGametestJava` against the pinned Minecraft 26.3/Fabric toolchain: **passed**. The follow-up incremental `compileGametestJava` after new runtime assertions also **passed**. Existing deprecation warnings remain.
- Current Minecraft client capture, full Build/Foundation, server GameTests, completed JAR/mixin audit, two-client acceptance and performance measurements: **pending**. Historical PR #447 passes do not certify this geometry or autumn code.

## Open defects and next concrete action

1. Run the selected `AcademyClientGameTests` on this template, inspect and save actual bridge, court, cross-wing and annex screenshots; revise any weak silhouette or obstructed stair/door before calling the shell visually reviewed.
2. Run the new server academy GameTest and the full Build/Foundation gates. Validate every palette state against the actual 26.3 registry, especially new leaf piles, barrel and stone details. Complete the JAR and `tools/check_mixin_jar.py`.
3. Expand and differentiate the Hall, Arcanaeum, both residences, quarters and services as accessible furnished rooms, then implement additional faculty and clue-led secrets. Do not label planned lessons or Augur content as implemented.
4. Replace the preliminary leaf-fragment look with a dedicated leaf sprite if actual game footage shows it does not read as falling leaves. Check off/low/minimal, hot biome, edge exit, reconnect, two separate clients and measured client frame cost.
5. Reassess total size and proportions against the three controlling images. This branch has begun correcting the shape; substantial expansion and human gameplay review remain before the College can be considered complete.
