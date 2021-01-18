import numpy as np
import random

def generate_biomes(size: tuple, min_rad: int, max_rad: int, biomes: list):
    assert 0 <= min_rad <= max_rad
    world = np.zeros(size, dtype=np.int8)
    world.fill(-1)
    exists_empty = True
    while exists_empty:
        origin = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
        curr_biome = random.choice(biomes)
        radius = random.randint(min_rad, max_rad + 1)
        for coord in filled_circle(origin, radius):
            if (0 <= coord[0] < size[0]) and (0 <= coord[1] < size[1]):
                world[coord[0]][coord[1]] = curr_biome
        if not -1 in world:
            exists_empty = False
    return world

def filled_circle(origin: tuple, radius: int):
    points = []
    size = radius * 2 + 1
    for x in range(-radius, size):
        for y in range(-radius, size):
            if round(np.sqrt(x**2 + y**2)) < radius:
                points.append((x+origin[0], y+origin[1]))
    return points


if __name__ == "__main__":
    bio = generate_biomes((14, 14), 2, 5, [0, 22, 100])
    print(bio)