"""Hand-fitted architectural and autumn detail for Frostward's three public rooms.

Fonta59's permission-cleared Hall and court supplied the *sectional grammar*:
several stepped slab/stair cornices, thick piers framing recessed bays, a high
annular gallery, and bookshelves that climb to the next occupied level. These
features are redrawn around Frostward's original rooms, routes and stations.
See docs/features/frostward-fonta59-adaptations.md for source bounds.
"""
from math import hypot

from retro_game_shop import state


def _put(put, x, y, z, name, **props):
    put(x, y, z, state(name if ":" in name else "minecraft:" + name, **props))


def craft_elements_hall(cells, put):
    """A high teaching theatre with carved supports, layered roof and dais."""
    def b(x, y, z, name, **props):
        _put(put, x, y, z, name, **props)

    # The source Hall repeatedly changes section at Y118/130/132/135/141.
    # Frostward translates that rhythm to Y25/30/34/37/43, with deliberately
    # unequal north and south bays. Restrict changes to occupied masonry: the
    # existing windows, side stairs, exterior passages and magic benches stay.
    for z, width in ((16, 7), (48, 5)):
        for x in range(54, 83):
            if abs(x - 68) > width and (x - 68) % 7 in (-3, 3):
                for y in range(26, 35):
                    old = cells.get((x, y, z), ("minecraft:air",))[0]
                    if old in ("minecraft:stone_bricks", "minecraft:chiseled_stone_bricks"):
                        b(x, y, z, "polished_andesite" if y in (30, 34) else "cracked_stone_bricks")
        for x in range(56, 81):
            if abs(x - 68) <= width:
                continue
            old = cells.get((x, 35, z), ("minecraft:air",))[0]
            if old.startswith("minecraft:stone"):
                b(x, 35, z, "stone_brick_stairs", facing="south" if z < 33 else "north",
                  half="top", shape="straight", waterlogged="false")

    # Monumental columns are thick in plan and have bases, shafts, corbels and
    # capitals. The original four quartz sticks are recut into Nordic stone.
    for x in (54, 82):
        for z in (24, 43):
            for y in range(25, 36):
                b(x, y, z, "chiseled_stone_bricks" if y in (25, 26, 30, 34, 35)
                  else "polished_andesite")
            for dx, dz in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                for y in (26, 34):
                    b(x + dx, y, z + dz, "stone_brick_stairs",
                      facing="east" if dx < 0 else "west" if dx > 0 else "south" if dz < 0 else "north",
                      half="top" if y == 34 else "bottom", shape="straight", waterlogged="false")
            b(x, 36, z, "sea_lantern")

    # A nested, dark timber and stone octagon breaks the flat underside of the
    # old gallery. Lanterns hang in the coffers, while the central bridges
    # remain supported at Y38 and the teaching wells stay open.
    for x in range(57, 80):
        for z in range(22, 45):
            d = max(abs(x - 68), abs(z - 33))
            if d in (6, 11):
                b(x, 35 if d == 11 else 36, z, "polished_andesite" if (x + z) % 3 else "chiseled_stone_bricks")
            elif d == 10 and (x + z) % 4 == 0:
                b(x, 36, z, "dark_oak_planks")
    for x, z in ((61, 26), (75, 26), (61, 40), (75, 40),
                 (68, 22), (68, 44)):
        b(x, 35, z, "lantern", hanging="true", waterlogged="false")

    # The north teaching end gets a broad, shallow stone dais and a stepped
    # focus. The middle floor, two Lampwright benches and Arctus remain free.
    for x in range(63, 74):
        for z in range(18, 25):
            if abs(x - 68) + abs(z - 21) <= 8:
                b(x, 25, z, "polished_deepslate" if z in (18, 24) or x in (63, 73)
                  else "polished_andesite")
    for x in range(65, 72):
        b(x, 25, 25, "polished_andesite_stairs", facing="south", half="bottom",
          shape="straight", waterlogged="false")
    for x in (64, 72):
        for z in (20, 23):
            b(x, 26, z, "chiseled_stone_bricks")
            b(x, 27, z, "lantern", hanging="false", waterlogged="false")
    for x in (65, 71):
        for y in range(26, 31):
            b(x, y, 17, "chiseled_stone_bricks" if y in (26, 30) else "polished_andesite")
    for x in range(66, 71):
        b(x, 30, 17, "polished_andesite")
    b(68, 26, 20, "enchanting_table")
    for x, z in ((59, 20), (77, 20), (59, 46), (77, 46)):
        b(x, 25, z, "dark_oak_trapdoor", facing="north", half="top", open="false", powered="false", waterlogged="false")

    # Three distinct exterior belts interrupt the sheer Hall drum. Restrict
    # these to cardinal frontages so the round wall does not gain a uniform
    # procedural stripe. South portal shoulders project into the court.
    for z in (51, 52, 53):
        for x in list(range(58, 63)) + list(range(74, 79)):
            if (x + z) % 2 == 0:
                b(x, 34, z, "stone_brick_stairs", facing="south", half="top",
                  shape="straight", waterlogged="false")
    for x in (59, 77):
        for z in (50, 51, 52, 53):
            for y in range(25, 46):
                b(x, y, z, "chiseled_stone_bricks" if y in (25, 30, 37, 44)
                  else "polished_andesite" if y % 5 == 0 else "stone_bricks")
            b(x, 46, z, "stone_brick_slab", type="bottom", waterlogged="false")
    for x in range(60, 77):
        for y in (37, 44, 52):
            if cells.get((x, y, 52), ("minecraft:air",))[0] != "minecraft:air":
                b(x, y, 52, "polished_andesite" if x % 3 else "chiseled_stone_bricks")

    # A slate roof surface replaces the unbroken light-gray cap, while the
    # donor-derived andesite relief remains visible as its pale embroidery.
    for x in range(50, 87):
        for z in range(15, 52):
            r = hypot(x - 68, z - 33)
            if not 6 < r < 18:
                continue
            for y in range(86, 70, -1):
                if cells.get((x, y, z), ("minecraft:air",))[0] == "minecraft:stone_bricks":
                    if cells.get((x, y + 1, z), ("minecraft:air",))[0] == "minecraft:air":
                        b(x, y, z, "deepslate_tiles" if int(r) % 5 else "polished_andesite")
                    break


def craft_arcanaeum(cells, put):
    """Multi-storey shelf courts, framed reading desks and a carved crown."""
    def b(x, y, z, name, **props):
        _put(put, x, y, z, name, **props)

    def inside(x, z, inset=0):
        return ((x - 147) / (22 - inset)) ** 2 + ((z - 34) / (23 - inset)) ** 2 <= 1

    # The original round library also receives a crafted central nave and
    # tall side archives. Its Conclave lectern and broad east-west aisle stay.
    for x in (100, 101, 123, 124):
        for z in range(25, 44):
            if z in range(29, 32) or z in range(38, 41):
                continue
            for y in range(25, 32):
                b(x, y, z, "bookshelf" if y not in (29, 31) else
                  "dark_oak_planks" if y == 29 else "chiseled_stone_bricks")
    for z in (25, 34, 43):
        for x in (105, 119):
            for y in range(25, 32):
                b(x, y, z, "chiseled_stone_bricks" if y in (25, 29, 31)
                  else "polished_andesite")
        for x in range(106, 119):
            b(x, 32, z, "dark_oak_planks" if x % 4 else "chiseled_stone_bricks")
    for x in range(106, 119):
        for z in range(25, 44):
            if x in (107, 112, 117) or z in (25, 34, 43):
                b(x, 33, z, "dark_oak_planks" if (x + z) % 4 else "polished_andesite")
    for x, z in ((107, 26), (117, 26), (107, 42), (117, 42)):
        b(x, 31, z, "lantern", hanging="true", waterlogged="false")
    for x, z in ((110, 26), (114, 42)):
        b(x, 25, z, "chiseled_bookshelf", facing="south" if z < 34 else "north")
        b(x, 26, z, "amethyst_block")

    # Fonta59's x31..54/Z-188..-165 archive groups books in tall returns.
    # Refit separate north and south runs into Frostward's larger half oval.
    # Every third bay is a warm niche or carved support, not another shelf.
    for x in range(150, 165):
        for z in (22, 23, 45, 46):
            if not inside(x, z, 3):
                continue
            if (x - 150) % 5 == 0:
                for y in range(25, 35):
                    b(x, y, z, "chiseled_stone_bricks" if y in (25, 29, 34)
                      else "polished_andesite")
                b(x, 30, z - 1 if z < 34 else z + 1, "lantern", hanging="false", waterlogged="false")
            else:
                for y in range(25, 34):
                    b(x, y, z, "bookshelf" if y not in (29, 33)
                      else "dark_oak_planks" if y == 29 else "stone_brick_slab")
                b(x, 34, z, "stone_brick_stairs", facing="south" if z < 34 else "north",
                  half="top", shape="straight", waterlogged="false")

    # A continuous occupied upper gallery already exists at Y36. Give it
    # readable stacks, shelf returns, dark timber handrails and hanging lamps.
    for x in range(151, 165):
        for z in (24, 44):
            if inside(x, z, 2) and (x - 151) % 4 != 0:
                for y in range(37, 42):
                    b(x, y, z, "bookshelf" if y != 40 else "dark_oak_planks")
                b(x, 42, z, "chiseled_stone_bricks")
    for x in range(151, 164):
        if x in (153, 158, 163):
            continue
        for z in (29, 39):
            if cells.get((x, 36, z), ("minecraft:air",))[0] != "minecraft:air":
                b(x, 37, z, "dark_oak_fence")
    for x in (153, 159, 164):
        for z in (26, 42):
            if inside(x, z, 2):
                b(x, 41, z, "lantern", hanging="true", waterlogged="false")

    # Pairs of square-column arches break the vast gray internal wall and
    # support stepped coffers beneath the Y44 roof. The central opening remains
    # high and the established eastern stair at Z41 is untouched.
    for x in (150, 158, 165):
        for z in (26, 42):
            if inside(x, z, 2):
                for y in range(25, 36):
                    b(x, y, z, "chiseled_stone_bricks" if y in (25, 29, 34, 35)
                      else "polished_andesite")
                for dz in (-1, 1):
                    b(x, 34, z + dz, "stone_brick_stairs", facing="north" if dz > 0 else "south",
                      half="top", shape="straight", waterlogged="false")
    for x in range(151, 165):
        for z in range(25, 44):
            if inside(x, z, 2) and (x in (151, 158, 164) or z in (25, 43)):
                b(x, 42, z, "dark_oak_planks" if (x + z) % 4 else "chiseled_stone_bricks")

    # Two wide, distinctly furnished work islands. They leave the door,
    # central room anchor and stair approach clear.
    for cx, cz in ((151, 31), (160, 37)):
        for x in range(cx - 2, cx + 3):
            for z in range(cz - 1, cz + 2):
                b(x, 24, z, "dark_oak_planks")
                if z == cz and abs(x - cx) <= 1:
                    b(x, 25, z, "dark_oak_slab", type="top", waterlogged="false")
        b(cx, 25, cz - 1, "lectern", facing="south", has_book="false", powered="false")
        for x in (cx - 2, cx + 2):
            b(x, 25, cz + 1, "spruce_stairs", facing="north", half="bottom",
              shape="straight", waterlogged="false")
        b(cx, 26, cz, "lantern", hanging="false", waterlogged="false")

    # Carved exterior spandrels and a dark stepped crown give the reading wing
    # its own skyline; source sectional rhythm is adapted, not copied.
    for x in range(145, 167):
        for z in (12, 56):
            if not inside(x, z, -1):
                continue
            for y in (30, 35, 42):
                if cells.get((x, y, z), ("minecraft:air",))[0] == "minecraft:stone_bricks":
                    b(x, y, z, "chiseled_stone_bricks" if y == 35 else "polished_andesite")
    for x in range(142, 165):
        for z in range(15, 54):
            if inside(x, z, 7) and not inside(x, z, 11):
                b(x, 46, z, "deepslate_tile_slab", type="bottom", waterlogged="false")


def landscape_autumn_court(cells, put):
    """Planted quadrants, irregular maples, leaf drift and warm Halloween light."""
    def b(x, y, z, name, **props):
        _put(put, x, y, z, name, **props)

    # Four old isolated maples become centers of unequal, raised garden beds.
    # The garden outlines are deliberately noncircular; all four radial walks
    # and the S01 ward's central approach remain at their original level.
    gardens = ((52, 75, 5, 4, "red"), (84, 75, 6, 4, "orange"),
               (52, 96, 5, 5, "yellow"), (83, 96, 6, 5, "red"))
    for cx, cz, rx, rz, colour in gardens:
        for x in range(cx - rx, cx + rx + 1):
            for z in range(cz - rz, cz + rz + 1):
                dx, dz = abs(x - cx), abs(z - cz)
                if dx + dz // 2 > rx + 1 or dz + dx // 3 > rz + 1:
                    continue
                if abs(x - 68) <= 5 or abs(z - 85) <= 5 or hypot(x - 68, z - 85) > 22:
                    continue
                if cells.get((x, 25, z), ("minecraft:air",))[0] == "minecraft:carved_pumpkin":
                    continue
                edge = dx + dz // 2 >= rx or dz + dx // 3 >= rz
                b(x, 24, z, "mossy_stone_bricks" if edge else "coarse_dirt" if (x + z) % 3 else "moss_block")
                if edge:
                    b(x, 25, z, "mossy_stone_brick_slab", type="bottom", waterlogged="false")
                elif (x * 7 + z * 3) % 5 == 0 and (x, z) != (cx, cz):
                    b(x, 25, z, "jugcraft:" + colour + "_leaf_pile", layers=1)

    # Varied tree heights, fork directions and asymmetric canopies prevent a
    # repeated four-tree postcard silhouette. No trunk is on the formal paths.
    trees = ((58, 72, "yellow", 5, 2), (76, 73, "red", 7, 3),
             (56, 100, "orange", 6, 2), (79, 101, "yellow", 5, 2),
             (48, 89, "orange", 4, 2), (87, 89, "red", 4, 2))
    for tx, tz, colour, height, radius in trees:
        if hypot(tx - 68, tz - 85) > 22 or abs(tx - 68) <= 5 or abs(tz - 85) <= 2:
            continue
        b(tx, 24, tz, "coarse_dirt")
        for y in range(25, 25 + height):
            b(tx, y, tz, "jugcraft:ecology_maple_log", axis="y")
        for dx in (-1, 1):
            b(tx + dx, 27 + height - 5, tz, "jugcraft:ecology_maple_log", axis="x")
        for y, rr in ((23 + height, radius - 1), (24 + height, radius),
                      (25 + height, radius + 1), (26 + height, radius),
                      (27 + height, radius - 1)):
            for x in range(tx - rr, tx + rr + 1):
                for z in range(tz - rr, tz + rr + 1):
                    if (x - tx) ** 2 + (z - tz) ** 2 <= rr * rr and (x + 2 * z + y) % 7 != 0:
                        b(x, y, z, "jugcraft:ecology_" + colour + "_maple_leaves")

    # Pumpkin groupings and garden lanterns make the scene celebratory by day
    # and eerie at night. These are at the beds, away from the ward/rune paths.
    for x, z, facing in ((55, 78, "south"), (49, 76, "east"),
                         (82, 79, "south"), (88, 75, "west"),
                         (55, 98, "north"), (48, 96, "east"),
                         (81, 98, "north"), (87, 96, "west")):
        b(x, 25, z, "jack_o_lantern", facing=facing)
        b(x + (1 if x < 68 else -1), 25, z, "pumpkin")
    for x, z in ((59, 77), (77, 77), (58, 97), (78, 98)):
        b(x, 25, z, "mossy_stone_bricks")
        b(x, 26, z, "lantern", hanging="false", waterlogged="false")

    # Leaf garlands are carried by the existing eight arcade frames, kept well
    # above eye level. Narrow amber/green highlights enrich the covered walk.
    for x, z in ((48, 74), (48, 96), (88, 74), (88, 96),
                 (52, 65), (84, 65), (52, 105), (84, 105)):
        for dx in range(-2, 3):
            if cells.get((x + dx, 31, z), ("minecraft:air",))[0] != "minecraft:air":
                b(x + dx, 30, z, "jugcraft:ecology_" + ("red" if dx < 0 else "orange") + "_maple_leaves")
