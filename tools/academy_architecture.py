"""The gate and scholarly cross-wing joining the existing Winterhold rooms.

These passes extend the one authored template after the recovered rooms are copied.
They deliberately leave occupied Midden cells below the new wing untouched.
"""
from retro_game_shop import state


def connect_academic_cluster(cells, put, spec):
    x0, z0, x1, z1 = spec["bounds"]
    assert (x0, z0, x1, z1) == (83, 20, 97, 48)

    def block(x, y, z, name, **props):
        put(x, y, z, state("minecraft:" + name, **props))

    # Continue the rock island beneath the transverse teaching wing, without
    # filling existing rooms or corridors in the undercroft.
    for x in range(x0, x1 + 1):
        for z in range(z0, z1 + 1):
            for y in range(24):
                if (x, y, z) not in cells:
                    block(x, y, z, "tuff" if y < 16 else "stone_bricks")
            block(x, 24, z, "polished_diorite")
            for y in range(25, 36):
                block(x, y, z, "air")

    # Long masonry walls and a flat, walkable stone roof make the library and
    # Hall read as one academic complex from the bridge. Three broad arches
    # maintain the existing lower hall-to-library route.
    for x in range(x0, x1 + 1):
        for z in (z0, z1):
            for y in range(25, 36):
                block(x, y, z, "stone_bricks")
        for z in range(z0, z1 + 1):
            block(x, 36, z, "stone_bricks")
    for z in range(z0, z1 + 1):
        for x in (x0, x1):
            for y in range(25, 36):
                block(x, y, z, "stone_bricks")
    for z in range(31, 38):
        for x in (x0, x1):
            for y in range(25, 32):
                block(x, y, z, "air")

    # Two teaching/study rooms flank the central processional passage. Each
    # has a wide opening, not a door that could obstruct NPC navigation.
    for z in (29, 39):
        for x in range(x0 + 1, x1):
            for y in range(25, 34):
                block(x, y, z, "stone_bricks")
        for x in range(88, 93):
            for y in range(25, 29):
                block(x, y, z, "air")
        for x in (87, 93):
            for y in range(25, 34):
                block(x, y, z, "chiseled_stone_bricks")

    for x in (85, 89, 93, 95):
        for z in (z0, z1):
            for y in range(25, 36):
                block(x, y, z, "chiseled_stone_bricks")
    # Glazed slots are confined to this new study wing; library stacks remain
    # windowless. Lanterns make the two rooms usable at night.
    for x in (86, 90, 92):
        for z in (z0, z1):
            for y in range(28, 31):
                block(x, y, z, "glass_pane")
    for x in (86, 94):
        for z in (24, 44):
            for y in range(25, 28):
                block(x, y, z, "bookshelf")
    for z in (25, 44):
        block(90, 25, z, "quartz_pillar")
        block(90, 26, z, "smooth_quartz_slab", type="top", waterlogged="false")
        block(90, 35, z, "sea_lantern")
    # Raised roof ribs and corner piers break the former low straight connector.
    for x in (83, 89, 97):
        for z in range(z0, z1 + 1):
            block(x, 37, z, "stone_brick_slab", type="bottom", waterlogged="false")
    for x in (x0, x1):
        for z in (z0, z1):
            for y in range(37, 40):
                block(x, y, z, "chiseled_stone_bricks")


def build_arcanaeum_reading_wing(cells, put, spec):
    """Broaden the Arcanaeum eastward with a usable hall and upper archive."""
    cx, cz = spec["center"]
    rx, rz = spec["radii"]
    assert (cx, cz, rx, rz) == (147, 34, 22, 23)

    def block(x, y, z, name, **props):
        put(x, y, z, state("minecraft:" + name, **props))

    def inside(x, z, inset=0):
        return ((x - cx) / (rx - inset)) ** 2 + ((z - cz) / (rz - inset)) ** 2 <= 1

    # The old round stacks meet an eastern half-oval. Its straight west wall
    # becomes a long indoor threshold, rather than another detached drum.
    for x in range(135, cx + rx + 1):
        for z in range(cz - rz, cz + rz + 1):
            if not inside(x, z):
                continue
            for y in range(24):
                if (x, y, z) not in cells:
                    block(x, y, z, "tuff" if y < 16 else "stone_bricks")
            block(x, 24, z, "polished_diorite" if (x + z) % 7 else "polished_deepslate")
            rim = not inside(x + 1, z) or not inside(x - 1, z) or not inside(x, z + 1) or not inside(x, z - 1)
            if x == 135 or rim:
                for y in range(25, 44):
                    block(x, y, z, "chiseled_stone_bricks" if y in (25, 35, 43) else "stone_bricks")
            # A stepped solid crown has no inaccessible interior void.
            block(x, 44, z, "stone_bricks")
            if inside(x, z, 3):
                block(x, 45, z, "stone_brick_slab", type="bottom", waterlogged="false")
            if inside(x, z, 9):
                block(x, 46, z, "stone_brick_slab", type="bottom", waterlogged="false")
            if inside(x, z, 16):
                block(x, 47, z, "stone_bricks")

    # Seven-wide sheltered link through the old Arcanaeum perimeter. Carving
    # this after the walls preserves the original stacks away from the route.
    for x in range(127, 139):
        for z in range(31, 38):
            block(x, 24, z, "polished_diorite")
            for y in range(25, 33):
                block(x, y, z, "air")
    for x in range(131, 140):
        for z in (30, 38):
            for y in range(25, 34):
                block(x, y, z, "stone_bricks")
        for z in range(30, 39):
            block(x, 34, z, "stone_bricks")

    # A taller rectangular knuckle ties both curved library volumes together
    # in elevation as well as in plan. It spans the lower original roof and
    # gives the bridge view one continuous academic silhouette.
    for x in range(124, 141):
        for z in range(25, 44):
            block(x, 44, z, "stone_bricks")
        for z in (25, 43):
            for y in range(36, 44):
                block(x, y, z, "stone_bricks")
    for x in range(124, 135):
        for z in range(25, 44):
            for y in (42, 43):
                block(x, y, z, "stone_bricks")
    for x in (126, 133, 140):
        for z in (25, 43):
            for y in range(36, 48):
                block(x, y, z, "chiseled_stone_bricks")
    for x in range(125, 140):
        for z in (25, 43):
            block(x, 45, z, "stone_brick_slab", type="bottom", waterlogged="false")

    # The main reading floor has two shelf courts, open central tables and
    # supported lighting. The rooms remain free of undocumented loot/grants.
    for x in (145, 153, 161):
        for z in (20, 48):
            if inside(x, z, 2):
                for y in range(25, 30):
                    block(x, y, z, "bookshelf")
                block(x, 30, z, "chiseled_quartz_block")
    for x in (146, 154, 162):
        for z in (27, 41):
            if inside(x, z, 3):
                block(x, 25, z, "quartz_pillar")
                block(x, 26, z, "smooth_quartz_slab", type="top", waterlogged="false")
    for x, z in ((142, 25), (142, 43), (162, 25), (162, 43)):
        for y in range(25, 37):
            block(x, y, z, "quartz_pillar")
        block(x, 37, z, "sea_lantern")

    # An upper ring overlooks a central open reading hall. The straight stair
    # starts on the east side of the lower hall and lands on this gallery.
    for x in range(148, 165):
        for z in range(22, 47):
            if inside(x, z, 2) and not (151 <= x <= 159 and 29 <= z <= 39):
                block(x, 36, z, "polished_diorite")
    for step in range(12):
        x, y, z = 137 + step, 25 + step, 41
        for support in range(25, y):
            block(x, support, z, "stone_bricks")
        block(x, y, z, "stone_brick_stairs", facing="east", half="bottom",
              shape="straight", waterlogged="false")
        for head in (y + 1, y + 2, y + 3):
            block(x, head, z, "air")
        block(x, y, z + 1, "stone_brick_wall", up="true")
    for x in range(150, 161):
        for z in (28, 40):
            if (x, 36, z) in cells:
                block(x, 37, z, "stone_brick_wall", up="true")
    for z in range(29, 40):
        for x in (150, 160):
            if (x, 36, z) in cells:
                block(x, 37, z, "stone_brick_wall", up="true")
    for x in (152, 157, 162):
        for z in (24, 44):
            if inside(x, z, 3):
                for y in range(37, 40):
                    block(x, y, z, "bookshelf")
    for x, z in ((150, 26), (162, 42)):
        block(x, 43, z, "sea_lantern")


def build_gatehouse(cells, put, spec):
    x0, z0, x1, z1 = spec["bounds"]
    assert (x0, z0, x1, z1) == (60, 114, 76, 126)

    def block(x, y, z, name, **props):
        put(x, y, z, state("minecraft:" + name, **props))

    for x in range(x0, x1 + 1):
        for z in range(z0, z1 + 1):
            for y in range(24):
                if (x, y, z) not in cells:
                    block(x, y, z, "tuff" if y < 16 else "stone_bricks")
            block(x, 24, z, "stone_bricks")
            for y in range(25, 35):
                block(x, y, z, "air")
    for x in range(x0, x1 + 1):
        for z in (z0, z1):
            for y in range(25, 34):
                block(x, y, z, "stone_bricks")
    for z in range(z0, z1 + 1):
        for x in (x0, x1):
            for y in range(25, 34):
                block(x, y, z, "stone_bricks")
    for x in range(x0, x1 + 1):
        for z in range(z0, z1 + 1):
            block(x, 33, z, "stone_bricks")
    for z in (z0, z1):
        for x in range(65, 72):
            for y in range(25, 33):
                block(x, y, z, "air")
    # Open reception bays connect to the vaulted through-route. Their benches
    # are decoration; the existing ward remains the authoritative interaction.
    for x in (64, 72):
        for y in range(25, 29):
            block(x, y, 120, "air")
    for x in (62, 74):
        for z in (116, 123):
            for y in range(25, 42):
                block(x, y, z, "chiseled_stone_bricks")
            block(x, 42, z, "lantern", hanging="false", waterlogged="false")
    for x in (61, 75):
        for z in (118, 122):
            block(x, 25, z, "polished_diorite_stairs", facing="east" if x == 61 else "west",
                  half="bottom", shape="straight", waterlogged="false")
    for z in (114, 126):
        for x in range(60, 77):
            block(x, 34, z, "stone_brick_wall", up="true")


def open_cloister_stairs(cells, put):
    """Return access to both roof walks after narrowing the court ring."""
    def block(x, y, z, name, **props):
        put(x, y, z, state("minecraft:" + name, **props))

    for x in (41, 95):
        for step in range(8):
            z, y = 87 + step, 25 + step
            block(x, y, z, "stone_brick_stairs", facing="south", half="bottom",
                  shape="straight", waterlogged="false")
            for head in (y + 1, y + 2, y + 3):
                block(x, head, z, "air")
            # One-block stair flights have a solid guard on each side.
            for side in (x - 1, x + 1):
                block(side, y, z, "stone_bricks")
                block(side, y + 1, z, "stone_brick_wall", up="true")


def build_archmage_annex(cells, put, spec):
    """Give the existing upper quarters a distinct court-facing western mass."""
    cx, cz = spec["center"]
    radius = spec["radius"]
    assert (cx, cz, radius) == (43, 33, 12)

    def block(x, y, z, name, **props):
        put(x, y, z, state("minecraft:" + name, **props))

    def disk(x, z, r):
        return (x - cx) ** 2 + (z - cz) ** 2 <= r ** 2

    # The existing lower west drum supports this chamber. Keep its lower rooms,
    # balcony and Midden intact; the new occupied level starts at Y=51.
    for x in range(cx - radius, cx + radius + 1):
        for z in range(cz - radius, cz + radius + 1):
            if not disk(x, z, radius):
                continue
            if disk(x, z, radius - 1):
                block(x, 50, z, "polished_diorite")
                for y in range(51, 60):
                    block(x, y, z, "air")
            else:
                for y in range(42, 60):
                    block(x, y, z, "stone_bricks")
            if disk(x, z, radius + 1):
                block(x, 60, z, "stone_bricks")
    for r, y in ((13, 60), (12, 61), (10, 62), (7, 63), (3, 64)):
        for x in range(cx - r, cx + r + 1):
            for z in range(cz - r, cz + r + 1):
                if disk(x, z, r):
                    block(x, y, z, "stone_bricks" if y == 60 else "stone_brick_slab",
                          **({} if y == 60 else {"type": "bottom", "waterlogged": "false"}))

    # A guarded enclosed gallery directly joins the existing upper study.
    for x in range(52, 63):
        for z in range(30, 37):
            block(x, 50, z, "polished_diorite")
            block(x, 55, z, "stone_bricks")
            for y in range(51, 55):
                block(x, y, z, "stone_bricks" if z in (30, 36) else "air")
    for x in (54, 60):
        for z in (30, 36):
            for y in range(52, 54):
                block(x, y, z, "glass_pane")

    # The first occupied room has a desk, individual shelves and warm lighting.
    # It remains part of the existing Arch-Mage suite, with no new magic grant.
    for z in (28, 29, 37, 38):
        for y in range(51, 54):
            block(37, y, z, "bookshelf")
    block(42, 51, 30, "quartz_pillar")
    block(42, 52, 30, "smooth_quartz_slab", type="top", waterlogged="false")
    block(39, 51, 37, "blue_bed", facing="north", part="foot", occupied="false")
    block(39, 51, 36, "blue_bed", facing="north", part="head", occupied="false")
    block(46, 51, 37, "barrel", facing="up", open="false")
    for x, z in ((35, 33), (43, 23), (43, 43)):
        block(x, 59, z, "lantern", hanging="true", waterlogged="false")
    for x, z in ((31, 33), (43, 21), (43, 45)):
        for y in range(53, 57):
            block(x, y, z, "glass_pane")


def add_autumn(cells, put):
    """Replace authored snowcaps with restrained year-round court foliage."""
    air = state("minecraft:air")
    for (x, y, z), old in list(cells.items()):
        if old[0] == "minecraft:snow":
            put(x, y, z, air)

    colours = ("red", "orange", "yellow")
    for x in range(40, 97):
        for z in range(57, 114):
            d2 = (x - 68) ** 2 + (z - 85) ** 2
            if not 16 ** 2 <= d2 <= 22 ** 2 or (x * 11 + z * 7) % 17:
                continue
            if abs(x - 68) <= 4 or abs(z - 85) <= 4:
                continue  # Keep the formal radial paths and ward clear.
            if cells.get((x, 25, z), air)[0] != "minecraft:air":
                continue
            if cells.get((x, 24, z), air)[0] == "minecraft:air":
                continue
            colour = colours[(x + 2 * z) % 3]
            put(x, 25, z, state("jugcraft:" + colour + "_leaf_pile", layers=1))

    for x, z, facing in ((51, 99, "north"), (85, 99, "north"),
                         (53, 71, "south"), (83, 71, "south")):
        if cells.get((x, 25, z), air)[0] == "minecraft:air" and cells.get((x, 24, z), air)[0] != "minecraft:air":
            put(x, 25, z, state("minecraft:carved_pumpkin", facing=facing))
