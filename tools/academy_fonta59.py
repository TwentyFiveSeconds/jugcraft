"""Selective Fonta59 Hall roof relief, rebuilt on Frostward's existing campus.

Only the small, documented upper roof motif in fonta59_hall_roof_motif.json
comes from the owner's permission-cleared world. The supporting drum, façade
and autumn landscaping are original Frostward construction.
"""
import json
from math import hypot
from pathlib import Path

from retro_game_shop import state


MOTIF = json.loads((Path(__file__).with_name("fonta59_hall_roof_motif.json")).read_text(encoding="utf-8"))["rows"]


def enrich_hall_and_campus(cells, put):
    def block(x, y, z, name, **props):
        put(x, y, z, state(("minecraft:" if ":" not in name else "") + name, **props))

    cx, cz = 68, 33

    # The 45-block donor Hall is visibly loftier than Frostward's old smooth
    # dome. Retain every original occupied level through Y64 and raise a
    # supported clerestory and stepped roof above it. The roof relief's north
    # half is mirrored and resized, so no complete donor building is pasted.
    for x in range(48, 89):
        for z in range(13, 54):
            r = hypot(x - cx, z - cz)
            if r > 20:
                continue
            for y in range(65, 73):
                block(x, y, z, "air")
            if r <= 19:
                for y in range(65, 71):
                    if r >= 17.5:
                        block(x, y, z, "stone_bricks" if y % 4 else "chiseled_stone_bricks")
                if r > 18.8:
                    block(x, 71, z, "stone_bricks")
                if r <= 18.8:
                    top = 71 + max(0, 13 - int(r * .72))
                    for y in range(71, top + 1):
                        block(x, y, z, "stone_bricks")
                    sx = 14 + round((x - cx) * 14 / 18)
                    sz = 14 - round(abs(z - cz) * 14 / 18)
                    if 0 <= sx < 29 and 0 <= sz < len(MOTIF) and MOTIF[sz][sx] == "#":
                        block(x, min(top + 1, 86), z, "polished_andesite")
                    elif r <= 17:
                        block(x, min(top + 1, 86), z, "stone_brick_slab", type="bottom", waterlogged="false")

    # Narrow amber clerestory slots sit between load-bearing masonry piers.
    # They are above the player's circulation and the original upper rooms.
    for x, z in ((68, 14), (68, 52), (49, 33), (87, 33)):
        for y in range(66, 69):
            block(x, y, z, "orange_stained_glass")
        block(x, 69, z, "chiseled_stone_bricks")
    for y in range(84, 87):
        block(68, y, 33, "chiseled_stone_bricks")
    block(68, 87, 33, "lantern", hanging="false", waterlogged="false")

    # Every buttress has a full-height load path. The eastern pair starts above
    # the Hall-to-library link so the academic passage stays seven wide.
    piers = ((-13, -13), (-13, 13), (13, -13), (13, 13),
             (-17, -6), (-17, 6), (17, -6), (17, 6))
    for dx, dz in piers:
        x, z = cx + dx, cz + dz
        base = 37 if dx > 0 and abs(dz) == 6 else 24
        for y in range(base, 72):
            block(x, y, z, "polished_andesite" if y in (37, 50, 63, 70) else "stone_bricks")
        block(x, 72, z, "chiseled_stone_bricks")
        if dx < 0 or abs(dz) == 13:
            for y in range(24, 32):
                block(x + (-1 if dx < 0 else 1), y, z + (-1 if dz < 0 else 1), "stone_bricks")

    # A layered, supported portal emphasizes the seven-wide south entrance.
    for x in (62, 74):
        for z in (49, 50, 51):
            for y in range(25, 45):
                block(x, y, z, "chiseled_stone_bricks" if y % 6 == 0 else "stone_bricks")
    for x in range(62, 75):
        for z in (49, 50, 51):
            block(x, 45, z, "stone_bricks")
            block(x, 46, z, "stone_brick_slab", type="bottom", waterlogged="false")
    for x in (64, 72):
        for y in range(24, 32):
            block(x, y, 52, "chiseled_stone_bricks" if y in (24, 31) else "stone_bricks")
        block(x, 32, 52, "lantern", hanging="false", waterlogged="false")

    # A pitched arcade roof and external pier rhythm articulate the inhabited
    # Hall–Arcanaeum wing. Its original room openings remain untouched.
    for x in range(83, 98):
        rise = max(0, 4 - abs(x - 90) // 2)
        for z in range(20, 49):
            if x <= 90 and 31 <= z <= 37:
                block(x, 37, z, "stone_bricks")
                block(x, 38, z, "stone_bricks")
                continue  # Keep the existing east balcony's Y39 walking lane.
            for y in range(37, 37 + rise):
                block(x, y, z, "stone_bricks")
            block(x, 37 + rise, z, "stone_brick_slab", type="bottom", waterlogged="false")
    for x in (83, 89, 97):
        for z in (19, 49):
            for y in range(25, 41):
                block(x, y, z, "chiseled_stone_bricks" if y in (25, 36, 40) else "stone_bricks")
            block(x, 41, z, "stone_brick_wall", up="true")

    # Reading-wing flying piers interrupt the blank oval wall but do not touch
    # its west link, eastern daylight slots, balcony or lower shelves.
    for x, z in ((153, 12), (161, 17), (166, 23),
                 (153, 56), (161, 51), (166, 45)):
        for y in range(24, 45):
            block(x, y, z, "stone_bricks" if y % 7 else "chiseled_stone_bricks")
        for y in range(45, 49):
            block(x, y, z, "chiseled_stone_bricks")
        block(x, 49, z, "stone_brick_wall", up="true")


def furnish_academic_crosswing(cells, put):
    def block(x, y, z, name, **props):
        put(x, y, z, state("minecraft:" + name, **props))

    # Two deliberately different scholarly rooms flank the broad processional
    # corridor. All furniture is on the existing Y24 floor and away from doors.
    for z in (23, 25, 43, 45):
        for y in range(25, 28):
            block(85, y, z, "bookshelf")
            block(95, y, z, "bookshelf")
    for x, z in ((88, 25), (91, 25), (88, 43), (92, 43)):
        block(x, 25, z, "spruce_fence")
        block(x, 26, z, "spruce_slab", type="top", waterlogged="false")
    block(90, 25, 23, "lectern", facing="south", has_book="false", powered="false")
    block(90, 25, 45, "cartography_table")
    block(94, 25, 43, "barrel", facing="up", open="false")
    for x, z in ((87, 26), (93, 26), (87, 42), (93, 42)):
        block(x, 35, z, "lantern", hanging="true", waterlogged="false")


def furnish_reading_wing_from_donor(cells, put):
    """Remodel one small diagonal donor bookcase return into two archive bays.

    The seven-block plan comes from Fonta59 world x=31..34, z=-168..-165,
    y=133..136. It is translated, paired and rehoused in Frostward's own
    much larger reading wing; no donor room or world chunk is copied.
    """
    def block(x, y, z, name, **props):
        put(x, y, z, state("minecraft:" + name, **props))

    return_plan = ((0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3))
    for z0, direction in ((19, 1), (49, -1)):
        for dx, dz in return_plan:
            x, z = 151 + dx, z0 + direction * dz
            for y in range(25, 29):
                block(x, y, z, "bookshelf")
            block(x, 29, z, "chiseled_stone_bricks")
        block(158, 25, z0 + direction * 4, "spruce_fence")
        block(158, 26, z0 + direction * 4, "spruce_slab", type="top", waterlogged="false")
        block(157, 25, z0 + direction * 5, "spruce_stairs", facing="east" if direction == 1 else "west",
              half="bottom", shape="straight", waterlogged="false")
        block(154, 30, z0 + direction * 3, "lantern", hanging="false", waterlogged="false")


def plant_autumn_court(cells, put):
    def block(x, y, z, name, **props):
        put(x, y, z, state("jugcraft:" + name, **props))

    # The trunks are set off the four formal approaches and the S01 runes.
    # Canopies begin four blocks over the paving, preserving head clearance.
    for tx, tz, colour in ((52, 75, "red"), (84, 75, "orange"),
                           (52, 95, "yellow"), (84, 95, "red")):
        for y in range(25, 31):
            block(tx, y, tz, "ecology_maple_log", axis="y")
        for y, radius in ((29, 2), (30, 3), (31, 3), (32, 2), (33, 1)):
            for x in range(tx - radius, tx + radius + 1):
                for z in range(tz - radius, tz + radius + 1):
                    if (x - tx) ** 2 + (z - tz) ** 2 <= radius ** 2 and (x, z) != (tx, tz):
                        block(x, y, z, "ecology_" + colour + "_maple_leaves")
