"""Original Winterhold-inspired college, using Jugcraft's existing magic stations.

Run: python tools/winterhold_academy.py [--check]
Uses the shared 26.3 NBT writer; no asset copies, dependencies or worldgen hooks.
The origin is the northwest bottom corner. Entry is (48, 9, 120), facing north.
"""
import argparse
import json
from math import isqrt
from pathlib import Path

from retro_game_shop import Byte, DATA_VERSION, nbt_bytes, state

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src/main/resources/data/jugcraft/structure/academy/winterhold.nbt"
SIZE = (97, 60, 121)
FLOOR = 8
ENTRY = (48, 9, 120)
# These public coordinates are shared by offline and in-game integration tests.
STATIONS = {
    "study_west": ((37, 9, 24), "jugcraft:lampwright_bench"),
    "study_east": ((59, 9, 24), "jugcraft:lampwright_bench"),
    "alchemy": ((22, 9, 54), "jugcraft:crucible"),
    "artifice": ((74, 9, 54), "jugcraft:artificer_bench"),
}
ROOMS = {
    "Hall of Elements": (48, 9, 29),
    "Arcanaeum": (48, 23, 29),
    "Archmage Study": (48, 35, 29),
    "Hall of Attainment": (18, 9, 61),
    "Hall of Countenance": (78, 9, 61),
    "Courtyard": (48, 9, 64),
    "Undercroft": (48, 1, 32),
}


def build():
    cells, metadata = {}, {}

    def put(x, y, z, block, **props):
        assert 0 <= x < SIZE[0] and 0 <= y < SIZE[1] and 0 <= z < SIZE[2], (x, y, z)
        cells[x, y, z] = state(block if ":" in block else "minecraft:" + block, **props)
        metadata.pop((x, y, z), None)

    def fill(x0, y0, z0, x1, y1, z1, block, **props):
        assert x0 <= x1 and y0 <= y1 and z0 <= z1
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                for z in range(z0, z1 + 1):
                    put(x, y, z, block, **props)

    def stone(x, y, z):
        # Coordinate-based wear, stable across Python versions; no random seed/global state.
        return "cracked_stone_bricks" if (13*x + 7*y + z) % 19 == 0 else "stone_bricks"

    def disk(x, z, cx, cz, r):
        return (x - cx)**2 + (z - cz)**2 <= r*r

    def edge(x, z, cx, cz, r):
        return disk(x, z, cx, cz, r) and any(not disk(x+dx, z+dz, cx, cz, r)
                                           for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)))

    def sign(x, y, z, *lines, facing="south"):
        put(x, y, z, "spruce_wall_sign", facing=facing, waterlogged=False)
        metadata[x, y, z] = {
            "id": "minecraft:sign", "is_waxed": Byte(1),
            "front_text": {"messages": list(lines) + [""] * (4-len(lines)),
                           "color": "black", "has_glowing_text": Byte(0)},
            "back_text": {"messages": [""]*4, "color": "black", "has_glowing_text": Byte(0)},
        }

    def lamp(x, y, z):
        put(x, y, z, "lantern", hanging=False, waterlogged=False)

    def bed(x, y, z):
        put(x, y, z, "blue_bed", facing="north", part="foot", occupied=False)
        put(x, y, z-1, "blue_bed", facing="north", part="head", occupied=False)

    # Raised, tapered stone footing. No surrounding air cube: terrain outside it is untouched.
    for y in range(9):
        inset = max(0, 6-y)
        for x in range(7+inset, 90-inset):
            for z in range(7+inset, 83-inset):
                if (x < 14 or x > 82) and (z < 14 or z > 75):
                    continue
                put(x, y, z, "polished_andesite" if y == FLOOR else stone(x, y, z))

    # Accessible undercroft, deliberately empty: no boss, loot farm or progression bypass.
    fill(38, 1, 18, 58, 6, 40, "air")
    for x in (39, 57):
        for z in (19, 39):
            fill(x, 1, z, x, 5, z, "chiseled_stone_bricks")
            lamp(x, 6, z)
    # Courtyard parapet, with a five-block bridge entrance to the south.
    for x in range(8, 89):
        for z in (8, 81):
            if z == 81 and 45 <= x <= 51:
                continue
            fill(x, 9, z, x, 10, z, "stone_bricks")
            if x % 3 != 0:
                put(x, 11, z, "stone_brick_slab", type="bottom", waterlogged=False)
    for z in range(9, 81):
        for x in (8, 88):
            fill(x, 9, z, x, 10, z, "stone_bricks")
            if z % 3 != 0:
                put(x, 11, z, "stone_brick_slab", type="bottom", waterlogged=False)

    # Narrow stone bridge with three arches and solid railings, wider at the gate.
    for z in range(82, 121):
        for x in range(44, 53):
            put(x, 8, z, "stone_bricks" if x in (44, 52) else "polished_andesite")
            fill(x, 9, z, x, 12, z, "air")
        for x in (44, 52):
            put(x, 9, z, "stone_bricks")
            if z % 6 == 0:
                put(x, 10, z, "chiseled_stone_bricks")
                lamp(x, 11, z)
        for x in range(44, 53):
            # Pillars and stepped arch undersides leave large openings underneath.
            d = min(abs(z-p) for p in (83, 95, 107, 119))
            bottom = min(7, d + 1)
            fill(x, bottom, z, x, 7, z, "stone_bricks")

    # Main circular hall; doors open into the courtyard to its south.
    cx, cz, radius = 48, 29, 18
    for x in range(30, 67):
        for z in range(11, 48):
            if not disk(x, z, cx, cz, radius):
                continue
            for y in range(9, 47):
                put(x, y, z, stone(x, y, z) if edge(x, z, cx, cz, radius) else "air")
            for y in (8, 22, 34, 46):
                put(x, y, z, "polished_andesite" if y == 8 else
                    "stone_bricks" if edge(x, z, cx, cz, radius) else "spruce_planks")
            if edge(x, z, cx, cz, radius):
                for y in (21, 33, 46):
                    put(x, y, z, "chiseled_stone_bricks")
    # Tall window groups on the cardinal walls, beyond the broad entry aisle.
    for y0 in (12, 25, 37):
        for y in range(y0, y0+5):
            for t in range(-2, 3):
                reach = isqrt(radius*radius-t*t)
                put(cx+t, y, cz-reach, "light_blue_stained_glass")
                put(cx-reach, y, cz+t, "light_blue_stained_glass")
                put(cx+reach, y, cz+t, "light_blue_stained_glass")
    fill(45, 9, 45, 51, 14, 48, "air")
    fill(45, 15, 46, 51, 15, 47, "stone_bricks")
    for x in (44, 52):
        fill(x, 9, 47, x, 15, 47, "chiseled_stone_bricks")
        lamp(x, 16, 47)
    sign(48, 16, 48, "Frostward", "College", "Hall of Elements")
    # Stepped gray dome, closed above the archmage study (not an observatory).
    for y, r in enumerate((19, 19, 18, 17, 15, 13, 10, 7, 3, 1), 47):
        for x in range(cx-r, cx+r+1):
            for z in range(cz-r, cz+r+1):
                if disk(x, z, cx, cz, r):
                    put(x, y, z, "stone_bricks" if edge(x, z, cx, cz, r) else "stone_brick_slab",
                        **({} if edge(x, z, cx, cz, r) else {"type": "bottom", "waterlogged": False}))
    # Buttresses frame the hall and reach past the cornice.
    for dx, dz in ((-13, -13), (-13, 13), (13, -13), (13, 13)):
        for y in range(9, 49):
            put(cx+dx, y, cz+dz, "polished_andesite")
        put(cx+dx, 49, cz+dz, "chiseled_stone_bricks")

    # Two independent switchback stairwells; every floor has a landing and 3-block clearance.
    for x0 in (33, 61):
        for base, rise in ((8, 14), (22, 12), (34, 12)):
            for n in range(rise//2):
                z = 22+n
                for x in (x0, x0+1):
                    fill(x, base+n+2, z, x, base+n+4, z, "air")
                    put(x, base+n+1, z, "spruce_stairs", facing="south")
                z = 22+rise//2-1-n
                for x in (x0+3, x0+4):
                    fill(x, base+rise//2+n+2, z, x, base+rise//2+n+4, z, "air")
                    put(x, base+rise//2+n+1, z, "spruce_stairs", facing="north")
            landing = 22+rise//2
            fill(x0, base+rise//2, landing, x0+4, base+rise//2, landing+1, "spruce_planks")
            fill(x0, base+rise//2+1, landing, x0+4, base+rise//2+3, landing+1, "air")
            fill(x0+3, base+rise, 20, x0+4, base+rise, 21, "spruce_planks")
            fill(x0+3, base+rise+1, 20, x0+4, base+rise+3, 21, "air")
    # Teaching floor: a clear central practice ring; desks do not give research for free.
    for x in range(40, 57):
        for z in range(23, 40):
            if 46 <= (x-cx)**2 + (z-31)**2 <= 64:
                put(x, 8, z, "blue_terracotta")
    for x in (41, 55):
        for z in (35, 39):
            put(x, 9, z, "spruce_stairs", facing="north")
    for name in ("study_west", "study_east"):
        pos, block = STATIONS[name]
        put(*pos, block, facing="south", working=False)
    put(48, 9, 18, "lectern", facing="south", has_book=False, powered=False)
    fill(45, 9, 17, 45, 10, 17, "chiseled_stone_bricks")
    sign(45, 10, 18, "Study specimens", "at the benches", "Bring your own", "Journal: J")
    # Arcanaeum shelving around the perimeter, with a clear ring and access to both stairs.
    for y in (23, 24, 25):
        for x in range(40, 57):
            put(x, y, 15, "bookshelf")
        for z in range(18, 43):
            for x in (32, 64):
                if not 20 <= z <= 31:
                    put(x, y, z, "bookshelf")
    for x in (43, 53):
        fill(x, 23, 25, x, 23, 34, "spruce_slab", type="top", waterlogged=False)
        for z in (26, 30, 34):
            put(x-1 if x < 48 else x+1, 23, z, "spruce_stairs", facing="east" if x < 48 else "west")
    # Archmage study: furnishing only, no free equipment or advanced unlock.
    bed(52, 35, 36)
    fill(43, 35, 16, 53, 37, 16, "bookshelf")
    fill(46, 35, 27, 50, 35, 28, "spruce_slab", type="top", waterlogged=False)
    put(48, 35, 26, "spruce_stairs", facing="south")
    put(56, 35, 35, "barrel", facing="up", open=False)
    for y in (9, 23, 35):
        for x, z in ((40, 19), (56, 19), (41, 41), (55, 41)):
            put(x, y, z, "chiseled_stone_bricks")
            lamp(x, y+1, z)

    # Twin residential/workshop towers, connected at ground level to the courtyard.
    for tcx, name in ((18, "Hall of Attainment"), (78, "Hall of Countenance")):
        tcz, r = 61, 10
        for x in range(tcx-r, tcx+r+1):
            for z in range(tcz-r, tcz+r+1):
                if not disk(x, z, tcx, tcz, r):
                    continue
                for y in range(9, 29):
                    put(x, y, z, stone(x, y, z) if edge(x, z, tcx, tcz, r) else "air")
                for y in (8, 17, 26):
                    put(x, y, z, "stone_bricks" if edge(x, z, tcx, tcz, r) else "spruce_planks")
                if edge(x, z, tcx, tcz, r):
                    put(x, 27, z, "chiseled_stone_bricks")
                    if (x+z) % 3:
                        put(x, 29, z, "stone_brick_slab", type="bottom", waterlogged=False)
        # Door faces the middle of the courtyard. A second outer door is unnecessary.
        doorx = tcx+9 if tcx < 48 else tcx-10
        fill(doorx, 9, 59, doorx+1, 12, 63, "air")
        sign(tcx, 13, 72, name, "Workshops below", "Dormitories above")
        put(tcx, 13, 71, "stone_bricks")
        # Broad nine-rise stair, then a landing open onto the dormitory.
        for n in range(9):
            z = 56+n
            for x in range(tcx-6, tcx-3):
                put(x, 9+n, z, "spruce_stairs", facing="south")
                fill(x, 10+n, z, x, 12+n, z, "air")
        fill(tcx-6, 17, 65, tcx-4, 17, 66, "spruce_planks")
        fill(tcx-6, 18, 65, tcx-4, 20, 66, "air")
        for dx in (-2, 2, 6):
            bed(tcx+dx, 18, 58)
            put(tcx+dx, 18, 64, "barrel", facing="up", open=False)
        for y in (11, 20):
            for dy in range(4):
                for dx in (-2, -1, 0, 1, 2):
                    put(tcx+dx, y+dy, tcz-isqrt(r*r-dx*dx), "light_blue_stained_glass")
        for y in (9, 18):
            for dx in (-2, 3):
                put(tcx+dx, y, 68, "chiseled_stone_bricks")
                lamp(tcx+dx, y+1, 68)
        # Guarded flat roofs are architectural only; no false promise of a working observatory.
        put(tcx, 27, tcz, "chiseled_stone_bricks")
        lamp(tcx, 28, tcz)
    for name in ("alchemy", "artifice"):
        pos, block = STATIONS[name]
        put(*pos, block)
    put(20, 9, 54, "water_cauldron", level=3)
    put(76, 9, 54, "crafting_table")
    for x in (20, 76):
        put(x, 9, 56, "barrel", facing="up", open=False)

    # Courtyard paths, a small crystal focal point and lantern pillars. No active ritual fixture.
    for x in range(29, 68):
        for z in range(58, 65):
            put(x, 8, z, "stone_bricks")
    for x in range(45, 52):
        for z in range(48, 82):
            put(x, 8, z, "stone_bricks")
    for x, z in ((40, 69), (56, 69), (40, 53), (56, 53)):
        fill(x, 9, z, x, 11, z, "chiseled_stone_bricks")
        lamp(x, 12, z)
    fill(46, 9, 72, 50, 9, 76, "polished_andesite")
    fill(47, 10, 73, 49, 10, 75, "chiseled_stone_bricks")
    put(48, 11, 74, "amethyst_block")
    put(48, 12, 74, "amethyst_cluster", facing="up", waterlogged=False)

    # Cut this flight last: the hall's floor must not seal the headroom halfway down.
    for n in range(8):
        fill(44, n+2, 41+n, 46, n+4, 41+n, "air")
        fill(44, n+1, 41+n, 46, n+1, 41+n, "stone_brick_stairs", facing="south")

    palette = sorted(set(cells.values()))
    indices = {s: i for i, s in enumerate(palette)}
    blocks = []
    for pos, block in sorted(cells.items()):
        entry = {"pos": list(pos), "state": indices[block]}
        if pos in metadata:
            entry["nbt"] = metadata[pos]
        blocks.append(entry)
    return {
        "DataVersion": DATA_VERSION, "size": list(SIZE),
        "palette": [{"id": name, **({"properties": dict(props)} if props else {})} for name, props in palette],
        "blocks": blocks, "entities": [],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the committed NBT is stale")
    parser.add_argument("--layout-json", type=Path, help="optional scratch voxel export for preview tools")
    args = parser.parse_args()
    template = build()
    packed = nbt_bytes(template)
    if args.check:
        if not OUT.exists() or OUT.read_bytes() != packed:
            raise SystemExit("Academy template is stale; run python tools/winterhold_academy.py")
    else:
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_bytes(packed)
    if args.layout_json:
        args.layout_json.parent.mkdir(parents=True, exist_ok=True)
        args.layout_json.write_text(json.dumps(template), encoding="utf-8")
    print(f"Academy: {len(template['blocks'])} blocks, {len(template['palette'])} states, {len(packed)} bytes")


if __name__ == "__main__":
    main()

