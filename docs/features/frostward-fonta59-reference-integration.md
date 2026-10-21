# Frostward College: architectural enrichment informed by Fonta59's Winterhold

> Owner direction, 21 October 2026: Treat the current Frostward College as the **skeleton**, add architectural strength and individualized detail as the **muscle and skin**, and keep **enchanted autumn / Halloween** as its unmistakable identity. This is an implementation specification for draft [PR #448](https://github.com/jimbozoomer-byte/jugcraft/pull/448), not a replacement college.

## Sources and permission boundary

- Fonta59's public [Winterhold (Skyrim TES) with interior](https://www.planetminecraft.com/project/winterhold-skyrim-tes-with-interior/) is a useful example of recognizable Minecraft-scale Winterhold construction, courtyard proportions, connected masses and an inhabited setting. Credit Fonta59 and link to the original project when discussing this inspiration.
- The user's controlling images remain the numbered original Winterhold floorplan and two Minecraft recreation screenshots in the Codex handoff. These govern landmark relationships and the entrance silhouette.
- Fonta59's [published conditions](https://www.planetminecraft.com/member/fonta/about/) forbid reusing map content in other packs, modifying or redistributing its content without explicit permission. **Do not import this world, its chunks, NBT/region data, exact block assembly, furnishings or textures into Jugcraft, nor mechanically translate or trace them.** A Minecraft world recreation inspired by Skyrim is useful as a comparative visual reference; author all actual Jugcraft geometry, decoration and code independently using Jugcraft's permitted assets. If Fonta59 provides explicit permission for selected direct reuse, record it and its scope in provenance **before** direct importing.
- Do not include the uploaded RAR, raw extracts, chunk images containing creator-generated map data, block schematics or converted world files in a PR or shipped artifacts. Credit sources when showing externally derived screenshots.

## Live starting point to preserve

At review, draft [#448](https://github.com/jimbozoomer-byte/jugcraft/pull/448) head was `b7b90bc588d0f252db26a40a5a4022a5bd7f6765`. Recheck the live branch before changing code.

The authoritative `jugcraft:academy/winterhold` template now measures **176 × 76 × 161**; the main court remains around (68,85), residences remain distinct, the Hall is north of the court, Hall and Arcanaeum connect via an academic cross-wing, eastern grand reading hall/upper archive are reachable, and the Arch-Mage has a westward annex. Existing stations, Arctus Vale, four-rune S01 and the Midden remain intact. Client-local falling leaves, mist, restrained supported leaf piles and pumpkins have begun replacing authored snow. These are **not finished** architecture, landscaping, NPC or gameplay milestones.

Keep the new changes on the same PR/branch and single generator/template. No duplicate college or new PR.

## Design test: a complete skeleton beneath the detail

The desired result is **a substantially larger and more magnificent Nordic magical university** that reads as Winterhold from the bridge and overhead, not an exact copy, generic Gothic cathedral, or collection of plain cylinders.

1. **Compare first**: place (a) the user's seven-landmark Winterhold reference, (b) Frostward's generated measured plan, and (c) the current actual Minecraft bridge/courtyard views side by side. Assess scale, axes, entrance-relative left/right, massing and connected routes. Use Fonta's photos as comparative visual examples only.
2. **Keep proven routes**: bridge → vaulted gatehouse → open round court; left/west Hall of Attainment, right/east Hall of Countenance; Hall of Elements as dominant north academic mass; connected Arch-Mage/Arcanaeum ensemble beyond it. Maintain every working doorway, staircase, anchor and profession station.
3. **Repair weak elevations**: the last PR #448 client evidence notes the Hall looks squat from the bridge. Rework its vertical massing, cornice/roof articulation and adjacent height hierarchy before adding surface props. The College should be magnificent with leaves and particles off.
4. **Enrich by authorship, not copying**: implement original buttress rhythms, projecting supported galleries, stone reveals, carved panels, parapet variation, layered arches and believable entrances, with varied material detailing and functional interiors. Use different architectural treatments for each hall, not clone one radial pattern.

## Area-by-area enrichment pass

| Frostward area | Current concern to check | Original, implementable enrichment | Autumn/Halloween rule |
| --- | --- | --- | --- |
| Bridge and gatehouse | First impression, gate pier proportions and distant Hall silhouette | Multi-span supported arches, layered parapet, relief-carved entrance, recessed gateway, credible roof supports, dignified reception bays. Do not widen to a highway or obstruct route. | Amber lanterns, scattered pumpkins at thresholds; thin leaf drift and thick fog **below** bridge; keep walking deck safe. |
| Circular courtyard | Repeated annular geometry and little landscaping | Segmented arcade façade with deep bays, radial approaches, decorated columns, distinctive portals, fountain/ward center, benches and seating, multi-level cloister arcades; preserve S01 runes and entrances. | Primary enchanted-autumn showcase: maple/aspen framing trees, orange/red/gold foliage, leaf piles, locally falling leaves, carved pumpkins in composed clusters, lanternlight and ground-hugging mist. |
| Hall of Elements | Ground-level bridge silhouette still squat; room too bare in older captures | Taller supported teaching tower / roof silhouette, imposing entry stairs, vaulted/tiered ceiling, structural ribs, carved piers, upper gallery, tiered lecture seating, teaching circles, research alcoves; workstations remain reachable. | Warm scholarly interiors, nearly no pumpkin clutter; blue/violet runes as restrained accents; leaves suppressed indoors. |
| Attainment | Beds accessible but simple copied bedrooms | Distinct residential floors, common room/hearth, study nooks, interlinked stair landings, private rooms differentiated by size/arrangement, masonry recesses, furniture with real function. | Autumn wreaths at entrances, occasional harvest table, warm windows, very light decoration. |
| Countenance | Faculty tower similar to student one | Dissimilar façades/roof and interior layout, personalized faculty suites, studies, meeting room, archives, specimen alcoves, practical labs, credible vertical circulation. | Dignified, aged autumn accents; rooms remain scholarly rather than festive. |
| Hall–Arcanaeum academic cross-wing | Link exists but needs architectural identity | Make it feel like a truly inhabited institution: transept-like Nordic connector, deep arch bays, research exhibits, gallery transitions, supported ceilings, scholarly signage and safe NPC routes. | Warm lantern interiors, view of exterior drifting foliage through selectively small windows. |
| Arcanaeum / eastern reading wing | Reading hall, shelving and upper archive implemented but visually repetitive and previously dim | Grand sectional design with clerestory-height (not necessarily glazed) vault, multi-height shelves, balconies and stairs, bookcases in recessed bays, varied reading clusters, curator's desk, maps and manuscripts, genuine archive function, sufficient readable lighting. Mostly windowless. | No random pumpkins among stacks. Restrained candles, antique copper accents and perhaps a single autumn botanical specimen. |
| Arch-Mage annex / upper rooms | Has bed, storage, connected wing but lacks prestige | Truly individual receiving hall, private study, book collection, luxurious bed chamber, ritual and enchanting stations, enclosed botanical conservatory, astronomical room and safe terrace. | Unique magical autumn conservatory: glow flora, rich copper/gold leaves, light fog in controlled garden only. |
| Midden / undercroft | Mostly prototype and placeholders | Ancient structural supports, collapsed yet traversable passages, differentiated ritual chambers, credible abandoned laboratory, actual clue routes and exits. Retain passage accessibility and server-authoritative secrets. | Eerie cold desaturated mist, sparse spectral lights, roots/moss; **no festive pumpkin overload** underground. |

## Material and detail density

Avoid a wall-to-wall mono-material `stone_bricks` look and long featureless corridors. Integrate permitted Jugcraft block variants and existing player-owned architectural/decor sets after verifying registry names and authored asset provenance. Stone should visibly bear weight, arches should spring from columns, roof projections should have supports, decorative features should not obstruct doors, pathing or contraptions.

Define each flagship room in multiple zones: **structural form**, **useful fixtures**, **furnishing clusters**, **lighting**, **lived-in clutter**, **secret or point of interest**. At least one intentional visual focal point and one credible purpose per room. Avoid adding 100 shelves to a tiny space and calling it a grand library.

## Halloween atmosphere is mandatory and takes priority over the reference's snow

Fonta59's build depicts the snowy Skyrim College; **do not bring snow over**. Continue PR #448's permanent local enchanted-autumn identity. No snowcaps, snow particles, snowy conifers or icy-blue grading as the default campus treatment. Preserve gray Nordic stone and replace environmental appearance with red/orange/gold leaves, autumn foliage, deliberate pumpkin clusters, warm candle/lantern illumination, local tumbling leaf particles and restrained creepy ground fog. Keep pale teal or icy runes only for specifically magical/forbidden rooms.

This aesthetic must persist through all server seasons without changing neighboring biome or actual world weather. Reuse existing Jugcraft leaf piles, pumpkin carvings, string lights, garlands, autumn trees and FogParticle where appropriate. Respect `academyfx off/low/normal`, particle settings, bounded client performance, indoor suppression and cleanup on world/dimension exit. Don't let ambiance hide navigational landmarks or make the campus into a Halloween carnival.

## Practical milestones on PR #448

**Pass A: structural rehabilitation.** Prioritize bridge-view Hall height, coherent attached exterior masses, credible buttresses/arches/cornices, and distinct Hall entrances. Generate top-down, bridge, court, afternoon/nighttime exterior previews, then actual Minecraft screenshots. Rework if the silhouette still lacks Winterhold's recognizable hierarchy.

**Pass B: high-density bespoke interiors.** Hall of Elements and Arcanaeum first; upper Arch-Mage, residences and cross-wing next. Author furniture/useful zones individually, preserving stations, stairways, bed supports, archive access, staff routes and documented 45-point room ledger. Ensure lighting works in a client screenshot, not only palette validation.

**Pass C: autumn landscape as a designed environment.** Concentrate original landscaping and pumpkins in court/gate/bridge thresholds, drifting leaves camera-locally, fog below bridge, more mysterious night presentation. Do a day/night compare with effects off/normal to show that architecture itself holds up.

**Pass D: faculty, secrets and validation.** Follow existing College S01–S12 plan in accessible playable slices. Run focused structure tests during iteration, final Build/Foundation/selected server and client GameTests, completed JAR and mixin audit, two-client/performance/hot-biome tests when possible. Never claim incomplete tests as passes.

At every checkpoint, keep `docs/features/frostward-rebuild-progress.md` and `frostward-room-ledger.csv` current with implementation, actual screenshot review, gameplay verification and blocked work. Save coherent commits on this branch. Never duplicate the College, PR, workstations or player progression.

## Definition of done

A player crossing the bridge immediately recognizes a **monumental expanded Winterhold-shaped** academy. It has believable structure, distinct building masses and richly varied academic interiors. The existing gameplay still works. The entire exterior feels enchanted by **autumn and Halloween** in daylight and at night: falling scarlet and gold leaves, tasteful pumpkins, amber light, spectral fog, without snow or global biome alterations. The independently authored improvements are much richer than the current starter structures, with no unauthorized use of Fonta59's world content.
