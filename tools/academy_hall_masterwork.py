"""Final, room-specific stonework for the Hall of Elements.

The donor Hall's inhabited annulus and alternating thick/thin masonry courses
inform this new composition. All work is fitted to Frostward's existing tower,
teaching floor, gallery, stairs, stations and upper suite; no donor room is
transplanted. See the Fonta59 adaptation ledger for the bounded source region.
"""
from retro_game_shop import state


def craft_hall_masterwork(cells, put):
    def b(x, y, z, name, **props):
        put(x, y, z, state(name if ":" in name else "minecraft:" + name, **props))

    def old(x, y, z):
        return cells.get((x, y, z), ("minecraft:air",))[0]

    # Two high, unequal barrel bays rise through the existing teaching wells.
    # The four ribs are stepped in whole stone, shallow stair and slab courses;
    # dark coffer fields between them make their height legible from the floor.
    # Y38 gallery floors and Y50 private-suite floor remain untouched.
    for north, z_courses in ((True, (24, 28)), (False, (38, 42))):
        for z in z_courses:
            for x in range(59, 78):
                span = abs(x - 68)
                rise = max(0, 9 - span)
                y = 41 + min(7, (rise * 7) // 9)
                if span <= 7:
                    b(x, y, z, "chiseled_stone_bricks" if span in (0, 4, 7)
                      else "polished_tuff")
                    if span in (2, 5):
                        b(x, y - 1, z, "polished_tuff_stairs",
                          facing="east" if x < 68 else "west", half="top",
                          shape="straight", waterlogged="false")
                    if span in (1, 6):
                        b(x, y - 1, z, "deepslate_tile_slab", type="top",
                          waterlogged="false")
                elif span == 8:
                    b(x, 42, z, "tuff_bricks")
                    b(x, 43, z, "polished_tuff_stairs",
                      facing="east" if x < 68 else "west", half="top",
                      shape="straight", waterlogged="false")
                else:
                    b(x, 41, z, "chiseled_stone_bricks")
        z0, z1 = z_courses
        for z in range(z0 + 1, z1):
            for x in range(61, 76):
                if old(x, 50, z) == "minecraft:air":
                    continue
                b(x, 49, z, "dark_oak_planks" if x in (62, 68, 74)
                  else "deepslate_tiles" if (x + z) % 4
                  else "polished_tuff")
        # A bronze-edged lantern well is inset into each vault, not hung as a
        # bright cube below it. The gallery has a clear view past both bays.
        lamp_z = 26 if north else 40
        for x in (66, 70):
            b(x, 48, lamp_z, "waxed_cut_copper_slab", type="top",
              waterlogged="false")
            b(x, 47, lamp_z, "lantern", hanging="true", waterlogged="false")

    # Give the crossing bridge a layered underside. Its narrow timber spine
    # and paired stone brackets visually connect the ribs without closing the
    # tall wells or adding a low false ceiling over the central compass.
    for z in range(23, 44):
        if z in (32, 33, 34):
            continue
        for x in (66, 70):
            if old(x, 38, z) == "minecraft:air":
                continue
            b(x, 37, z, "dark_oak_planks")
            if z in (26, 30, 36, 40):
                b(x, 36, z, "polished_tuff_stairs", facing="north" if z < 33
                  else "south", half="top", shape="straight", waterlogged="false")

    # Four great piers gain three-dimensional capitals and bronze fillets.
    # Their shafts are grounded by the earlier pass; the new brackets lead the
    # eye up to the crossing gallery instead of repeating one stone texture.
    for x, z in ((57, 25), (79, 25), (57, 41), (79, 41)):
        inward = 1 if x < 68 else -1
        for y in (31, 36, 41):
            b(x + inward, y, z, "polished_tuff_stairs",
              facing="west" if inward > 0 else "east", half="top",
              shape="straight", waterlogged="false")
        for y in range(29, 36):
            b(x, y, z + (1 if z < 33 else -1),
              "dark_oak_planks" if y in (30, 34) else "polished_deepslate")
        b(x, 35, z + (1 if z < 33 else -1), "waxed_cut_copper_slab",
          type="top", waterlogged="false")

    # The upper north wall is an occupied academic screen around its original
    # window. The south-facing book court and unequal instrument recess were
    # built in the previous pass; stepped arches and dark horizontal ties now
    # bind them to the stone jambs. No block enters the Y39 walking ring.
    for x0, x1 in ((59, 63), (73, 77)):
        for x in range(x0, x1 + 1):
            edge = min(x - x0, x1 - x)
            y = 48 + edge // 2
            b(x, y, 19, "chiseled_stone_bricks" if x in (x0, x1)
              else "polished_tuff")
            if x not in (x0, x1):
                b(x, y - 1, 19, "polished_tuff_stairs", facing="south",
                  half="top", shape="straight", waterlogged="false")
        for y in (40, 44):
            b(x0, y, 19, "waxed_cut_copper_slab", type="top",
              waterlogged="false")
            b(x1, y, 19, "waxed_cut_copper_slab", type="top",
              waterlogged="false")
    for x in range(63, 74):
        if x in (67, 68, 69):
            continue  # blue clerestory and the north lecture sightline
        b(x, 45, 19, "dark_oak_planks")
        b(x, 46, 19, "polished_tuff_stairs", facing="south", half="top",
          shape="straight", waterlogged="false")

    # A four-block-deep rear teaching console makes the apse an institution's
    # working lectern rather than an empty altar. The enchanted table at
    # (68,26,20), center lectern, and side lecterns retain their exact cells.
    for x in range(64, 73):
        for z in (21, 22):
            if (x, z) in ((65, 21), (68, 21), (68, 22), (71, 21)):
                continue
            b(x, 27, z, "dark_oak_slab", type="top", waterlogged="false")
        if x in (64, 68, 72):
            b(x, 27, 21, "chiseled_stone_bricks")
            b(x, 28, 21, "waxed_cut_copper_slab", type="bottom",
              waterlogged="false")
    for x in (63, 73):
        for z in (21, 24):
            b(x, 26, z, "polished_tuff")
            b(x, 27, z, "dark_oak_trapdoor", facing="south", half="top",
              open="false", powered="false", waterlogged="false")
    for x, material in ((61, "amethyst_block"), (75, "waxed_cut_copper")):
        # Separate demonstration plinths flank the instructor but stay clear
        # of the two original Lampwright benches at (57/79,25,28).
        b(x, 25, 24, "chiseled_stone_bricks")
        b(x, 26, 24, material)
        b(x, 27, 24, "iron_bars", north="false", south="false",
          east="false", west="false", waterlogged="false")
        b(x, 28, 24, "lantern", hanging="false", waterlogged="false")

    # Distinct floor-level research pockets complement the eastern archive:
    # shallow walnut worktops, specimen plinths, and book returns. Their
    # footprints sit outside the five-wide central procession and stairways.
    for x0, side in ((60, -1), (76, 1)):
        for z in (30, 32):
            b(x0, 25, z, "dark_oak_planks")
            b(x0, 26, z, "dark_oak_slab", type="top", waterlogged="false")
        b(x0, 25, 31, "chiseled_stone_bricks")
        b(x0, 26, 31, "cartography_table" if side < 0 else "smithing_table")
        b(x0 + side, 25, 30, "bookshelf")
        b(x0 + side, 26, 30, "chiseled_bookshelf",
          facing="east" if side < 0 else "west")
        b(x0 + side, 27, 30, "polished_tuff_stairs",
          facing="east" if side < 0 else "west", half="top",
          shape="straight", waterlogged="false")

    # A selective south elevation treatment makes the tower's great frontage
    # look carved from several depths. Existing lower portal, amber windows,
    # roof relief and autumn foliage stay intact.
    for x in (61, 67, 69, 75):
        for y in range(45, 63):
            if old(x, y, 52) not in ("minecraft:stone_bricks",
                                     "minecraft:chiseled_stone_bricks",
                                     "minecraft:polished_andesite"):
                continue
            b(x, y, 53, "chiseled_stone_bricks" if y in (45, 50, 56, 62)
              else "polished_tuff" if y % 3 else "tuff_bricks")
    for x0, x1 in ((62, 66), (70, 74)):
        for x in range(x0, x1 + 1):
            if old(x, 51, 52) != "minecraft:air":
                b(x, 51, 53, "deepslate_tile_slab", type="bottom",
                  waterlogged="false")
        for x in range(x0 + 1, x1):
            for y in range(46, 51):
                if old(x, y, 52) == "minecraft:stone_bricks":
                    b(x, y, 52, "polished_deepslate" if y < 49
                      else "chiseled_stone_bricks")
