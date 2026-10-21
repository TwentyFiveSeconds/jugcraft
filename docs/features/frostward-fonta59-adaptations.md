# Fonta59 architectural adaptations in Frostward College

Fonta59 created [Winterhold (Skyrim TES) with interior](https://www.planetminecraft.com/project/winterhold-skyrim-tes-with-interior/). The Jugcraft owner reports direct permission to selectively reuse and modify portions of his Minecraft world, provided the entire map is not simply copied and pasted. The owner-supplied `Winterhold_by_fonta59.rar` was inspected locally; neither the archive nor its unmodified world is part of this repository or mod distribution.

This checkpoint keeps Frostward's existing **176 × 161** campus footprint, seven-landmark arrangement, 45 room/anchor points, academy stations, Arctus Vale, S01 runes and Midden. The generated structure has grown from **76 to 88 blocks high** for the Hall's stronger bridge silhouette. The single source remains `tools/winterhold_layout.json` and its Python generator passes.

| Donor region in the 1.12.2 world | Selected part | Frostward destination and transformation |
| --- | --- | --- |
| Main Hall upper roof, world X 28–56, Z −193 to −179, Y 165–176 | 96 relief positions on the north half of the stone/stair roof, recorded in `tools/fonta59_hall_roof_motif.json` | Mirrored and scaled from radius 14 to radius 18, mapped to 26.3 polished andesite over an **original**, taller supported Hall drum and stepped roof at Frostward center (68, 33). No donor roof volume or enclosing room is copied. |
| Curved library bay, world X 31–34, Z −168 to −165, Y 133–136 | Seven-block diagonal bookshelf return | Translated and mirrored into two four-high recessed shelf bays in Frostward's existing eastern reading wing; original stone crowns, lights and reading seats complete the bays. |

The original Frostward work in this checkpoint includes Hall buttresses and portal, cross-wing pitched arcade, reading-wing exterior piers and furnished research rooms. Four court maples use Jugcraft's existing red, orange and yellow foliage. Existing red/orange/yellow leaf piles, pumpkins, camera-local falling leaves and fog remain; the generated palette still contains **zero snow**. Source-white roof detailing was remapped into gray Nordic masonry rather than a snowy environment.

## Current evidence and limits

The regenerated template has **338,992 cells, 87 palette states and size 176 × 88 × 161**. Focused Python structure tests pass **13/13**; the Node template verifier passes **45/45 named points**, eight doors, 16 bed halves, eight signs and zero snow, with 16,688 reachable standing positions. The regenerated plan, bridge projection and overview in `docs/images/` are computed from actual NBT cells. These are geometry previews. Actual Minecraft bridge, court and interior screenshots for this checkpoint, Java/client GameTests, two-client autumn controls and performance checks remain to be recorded in the progress ledger after the branch runs.

The donor world's courtyard arcade, stair cores, additional chambers and furnishings have been cataloged only at a coarse level. Further reuse needs bounded extraction, conversion and gameplay review. No complete donor building or map region has been committed. This project also preserves the three owner-supplied Skyrim/Minecraft references as the controlling landmark and scale references.
