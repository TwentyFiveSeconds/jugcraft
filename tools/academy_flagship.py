"""Room-specific craft for Frostward's library, autumn court and private suite.

The permitted Fonta59 world supplies the sectional idea of deep shelf returns,
stone-framed openings and occupied perimeter bays. These are newly composed
around Frostward's existing rooms, stations, stairs and named routes.
"""
from math import hypot

from retro_game_shop import state


def craft_flagship_rooms(cells, put):
    def b(x, y, z, name, **props):
        put(x, y, z, state(name if ":" in name else "minecraft:" + name, **props))

    def old(x, y, z):
        return cells.get((x, y, z), ("minecraft:air",))[0]

    # LIBRARY: replace the original low ceiling over the reading nave with
    # a raised, enclosed lantern vault. The side stacks and the Conclave at
    # (112,25,23) are outside this cut. Its stepped ribs grow from the shelf
    # piers; glazed clerestory bays light the books without a glass roof.
    for x in range(107, 118):
        for z in range(27, 42):
            for y in range(32, 43):
                b(x, y, z, "air")
            b(x, 44, z, "deepslate_tiles" if (x + z) % 7 else "polished_deepslate")
    for z in (28, 34, 40):
        for x in range(106, 119):
            dx = abs(x - 112)
            y = 43 - (dx * 2 // 3)
            b(x, y, z, "chiseled_stone_bricks" if dx in (0, 6) else "polished_tuff")
            if dx < 5:
                b(x, y - 1, z, "polished_tuff_stairs", facing="east" if x < 112 else "west",
                  half="top", shape="straight", waterlogged="false")
    for x in (107, 117):
        for z in range(27, 42):
            for y in range(37, 44):
                b(x, y, z, "chiseled_stone_bricks" if z in (27, 34, 41) or y in (37, 43)
                  else "orange_stained_glass" if z % 4 in (1, 2) and y in (39, 40)
                  else "polished_deepslate")
    for z in (27, 41):
        for x in range(108, 117):
            for y in range(37, 44):
                b(x, y, z, "chiseled_stone_bricks" if x in (108, 112, 116) or y in (37, 43)
                  else "orange_stained_glass" if y in (39, 40)
                  else "polished_deepslate")
    for z in (29, 39):
        for x in (109, 115):
            b(x, 40, z, "iron_chain", axis="y", waterlogged="false")
            b(x, 39, z, "lantern", hanging="true", waterlogged="false")
    # High archive fronts are separated by dark oak bands and deep stone
    # returns. Four deliberately different research bays flank the clear
    # central aisle instead of repeating one bench down the room.
    for x in (101, 123):
        for z in range(25, 44):
            if z in (29, 30, 38, 39):
                continue
            for y in range(25, 32):
                b(x, y, z, "chiseled_stone_bricks" if z % 5 == 0 and y in (25, 29, 31)
                  else "dark_oak_planks" if y == 29 else "bookshelf")
        for z in (27, 35, 42):
            b(x + (1 if x < 112 else -1), 31, z, "lantern", hanging="true", waterlogged="false")
    for cx, cz, material in ((106, 30, "dark_oak_planks"), (118, 30, "spruce_planks"),
                             (106, 39, "spruce_planks"), (118, 39, "dark_oak_planks")):
        for x in range(cx - 1, cx + 2):
            b(x, 25, cz, material)
            b(x, 26, cz, "dark_oak_slab", type="top", waterlogged="false")
        b(cx, 26, cz - 1, "lectern", facing="south", has_book="false", powered="false")
        b(cx - 1, 25, cz + 2, "spruce_stairs", facing="north", half="bottom",
          shape="straight", waterlogged="false")
        b(cx + 1, 25, cz + 2, "spruce_stairs", facing="north", half="bottom",
          shape="straight", waterlogged="false")
        b(cx + 2 if cx < 112 else cx - 2, 25, cz, "chiseled_bookshelf",
          facing="west" if cx < 112 else "east")
    # A single charting instrument under the nave, not a row of identical
    # white electric fixtures. Its bright center is softened by amber glass.
    for x in range(109, 116):
        for z in range(32, 37):
            if old(x, 31, z) in ("minecraft:sea_lantern", "minecraft:smooth_quartz"):
                b(x, 31, z, "air")
    for x, z in ((110, 34), (114, 34), (112, 32), (112, 36)):
        b(x, 41, z, "waxed_cut_copper")
    b(112, 41, 34, "sea_lantern")
    b(112, 40, 34, "orange_stained_glass")

    # COURT: the planted ground now meets the Nordic arcade in a continuous
    # irregular herbaceous verge. Formal five-wide radial walks, S01 runes and
    # portals stay at the original grade; the verge gives maples a landscape
    # instead of four isolated patches on bare paving.
    for x in range(44, 93):
        for z in range(61, 110):
            r = hypot(x - 68, z - 85)
            if not 15 <= r <= 22 or abs(x - 68) <= 5 or abs(z - 85) <= 5:
                continue
            if old(x, 24, z) == "minecraft:air" or old(x, 25, z) not in (
                    "minecraft:air", "minecraft:mossy_stone_brick_slab"):
                continue
            if (x * 7 + z * 11) % 11 < 3:
                b(x, 24, z, "moss_block" if (x + z) % 3 else "coarse_dirt")
            else:
                b(x, 24, z, "mossy_stone_bricks" if (x + z) % 3 else "cracked_stone_bricks")
            if (x * 17 + z * 13) % 8 == 0:
                colour = ("red", "orange", "yellow")[(x + z) % 3]
                b(x, 25, z, "jugcraft:" + colour + "_leaf_pile", layers=1)
            elif (x * 5 + z * 3) % 19 == 0:
                b(x, 25, z, "jugcraft:" + ("purple" if x % 4 else "orange") + "_mum")
    # Interlock maple branches with the arcade's planted plinths. These low
    # balconies of foliage frame the institution without filling its paths.
    for x, z, colour in ((49, 71, "red"), (87, 71, "yellow"),
                         (48, 98, "orange"), (88, 98, "red")):
        for dx in range(-2, 3):
            for dz in range(-1, 2):
                if abs(dx) + abs(dz) > 3:
                    continue
                b(x + dx, 30, z + dz, "jugcraft:ecology_" + colour + "_maple_leaves")
        b(x, 27, z, "jack_o_lantern", facing="south" if z < 85 else "north")
    for x, z in ((53, 83), (83, 83), (53, 88), (83, 88)):
        b(x, 24, z, "mossy_stone_bricks")
        b(x, 25, z, "chiseled_stone_bricks")
        b(x, 26, z, "lantern", hanging="false", waterlogged="false")

    # ARCH-MAGE: the upper public study gains a carved ceiling, a pair of
    # working scholarly desks, botanical cabinets and a dark reading hearth.
    # Keep room anchors at (68,51,33) and (73,51,36) clear.
    for x in range(56, 81):
        for z in range(22, 45):
            if hypot(x - 68, z - 33) > 11:
                continue
            if (x - 68) % 6 == 0 or (z - 33) % 6 == 0:
                if old(x, 62, z) != "minecraft:air":
                    b(x, 61, z, "dark_oak_planks" if (x + z) % 4 else "chiseled_stone_bricks")
    for x, z in ((58, 27), (78, 27), (58, 39), (78, 39)):
        for y in range(51, 59):
            b(x, y, z, "polished_tuff" if y not in (51, 54, 58) else "chiseled_stone_bricks")
        b(x, 59, z, "dark_oak_planks")
    for cx, cz in ((61, 29), (76, 30)):
        for x in range(cx - 2, cx + 3):
            b(x, 51, cz, "dark_oak_planks")
            b(x, 52, cz, "dark_oak_slab", type="top", waterlogged="false")
        b(cx, 52, cz - 1, "lectern", facing="south", has_book="false", powered="false")
        for x in (cx - 2, cx + 2):
            b(x, 51, cz + 2, "spruce_stairs", facing="north", half="bottom",
              shape="straight", waterlogged="false")
        b(cx, 53, cz, "lantern", hanging="false", waterlogged="false")
    for x in range(63, 74):
        for y in range(52, 58):
            if x in (63, 68, 73):
                b(x, y, 22, "chiseled_stone_bricks")
            else:
                b(x, y, 22, "bookshelf" if y not in (54, 57) else "dark_oak_planks")
    for x in (64, 72):
        b(x, 58, 23, "lantern", hanging="true", waterlogged="false")

    # The annex is a private collection with real wall-scale shelves and a
    # framed, existing bed. Wood ceiling coffers and copper lights add warmth;
    # its room and bedroom anchors remain walkable beside the furniture.
    for x in range(34, 53):
        for z in range(25, 42):
            if hypot(x - 43, z - 33) > 9:
                continue
            if (x - 43) % 5 == 0 or (z - 33) % 5 == 0:
                b(x, 59, z, "dark_oak_planks" if (x + z) % 4 else "chiseled_stone_bricks")
    for x in (34, 35, 50, 51):
        for z in range(29, 38):
            if z in (32, 33):
                continue
            for y in range(51, 58):
                if old(x, y, z) in ("minecraft:air", "minecraft:bookshelf"):
                    b(x, y, z, "dark_oak_planks" if y in (54, 57) else "bookshelf")
    for x, z in ((36, 30), (49, 30), (36, 39), (49, 39)):
        b(x, 51, z, "chiseled_quartz_block")
        b(x, 52, z, "lantern", hanging="false", waterlogged="false")
    for x in (38, 41):
        for z in (35, 39):
            for y in range(51, 55):
                b(x, y, z, "dark_oak_log", axis="y")
            b(x, 55, z, "dark_oak_planks")
    for x in range(38, 42):
        for z in (35, 39):
            b(x, 55, z, "dark_oak_planks")
    for z in range(36, 39):
        for x in (38, 41):
            b(x, 55, z, "dark_oak_planks")
    b(39, 51, 36, "blue_bed", facing="north", part="head", occupied="false")
    b(39, 51, 37, "blue_bed", facing="north", part="foot", occupied="false")
    for x in range(44, 49):
        b(x, 51, 37, "dark_oak_planks")
        b(x, 52, 37, "dark_oak_slab", type="top", waterlogged="false")
    b(46, 52, 36, "lectern", facing="south", has_book="false", powered="false")
    b(47, 53, 37, "lantern", hanging="false", waterlogged="false")
