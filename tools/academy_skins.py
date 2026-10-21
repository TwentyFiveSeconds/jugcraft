"""Arctus Vale: reuse Jugcraft's classic townsfolk UV and robe helper, never a new rig.

Library magic robe item textures and shady_wizard villager UV were inspected;
neither fits the existing classic player model. Original town helper supplies this skin.
"""
from town_skins import OUT, person, dress


def robes(skin, rng, tone, hair):
    ivory, blue, gold = (231, 226, 207), (56, 92, 158), (183, 147, 65)
    dress(ivory, gold)(skin, rng, tone, hair)
    for part in ("right_pants", "left_pants"):
        skin.fill(part, blue, sides=["front", "back", "left", "right"], rows=(8, 11))
        skin.fill(part, gold, sides=["front", "back", "left", "right"], rows=(11, 12))
    for part in ("right_arm", "left_arm"):
        skin.fill(part, blue, sides=["front", "back", "left", "right"], rows=(7, 9))
    for x in (2, 5):
        for y in range(1, 6):
            skin.dot("jacket", "front", x, y, blue)
    skin.dot("jacket", "front", 3, 3, gold)
    skin.dot("jacket", "front", 4, 3, gold)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    person(441, robes, clean=True).save(OUT / "academy_radiance.png")
