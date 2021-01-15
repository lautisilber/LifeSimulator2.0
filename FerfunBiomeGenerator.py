  
import numpy as np
import random

def generate_biomes(size: tuple, min_rad: int, max_rad: int, biomes: list):
    assert 0 <= min_rad <= max_rad
    world = np.zeros(size, dtype=np.uint8)
    world.fill(-1)
    exists_empty = True
    while exists_empty:
        origin = (random.randint(0, size[0] - 1), random.randint(0, size[1] - 1))
        curr_biome = random.choice(biomes)
        radius = random.randint(min_rad, max_rad + 1)

def _mid_point_circle(origin: tuple, radius: int):
    x_c = origin[0]
    y_c = origin[1]

    x = radius
    y = 0
    perim = []

    perim.append((x + x_c, y + y_c))
    if radius > 0:
        perim.append((x + x_c, -y + y_c))
        perim.append((y + x_c, x + y_c))
        perim.append((-y + x_c, x + y_c))

    p = 1 - radius
    while x > y:
        y += 1

        if p <= 0:
            p = p + 2 * y + 1
        else:
            x -= 1
            p = p + 2 * y - 2 * x + 1

        if x < y:
            break

        perim.append((x + x_c, y + y_c))
        perim.append((-x + x_c, y + y_c))
        perim.append((x + x_c, -y + y_c))
        perim.append((-x + x_c, -y + y_c))        

        if x != y:
            perim.append((y + x_c, x + y_c))
            perim.append((-y + x_c, x + y_c))
            perim.append((y + x_c, -x + y_c))
            perim.append((-y + x_c, -x + y_c))
    
    return perim

def _mid_point_line(p1: tuple, p2: tuple):
    dy = p2[1] - p1[1]
    dx = p2[0] - p1[0]
    d = dy - (dx / 2)
    x = p1[0]
    y = p1[1]

    points = []

    points.append((x, y))
    while x < p2[0]:
        x += 1

        if d < 0:
            d += dy
        else:
            d += (dy - dx)
            y += 1
        points.append((x, y))

    return points       

def _fill_circle_from_perimeter(origin: tuple, perim_points: list):
    pass


if __name__ == "__main__":
    p = _mid_point_line((2, 2), (2, 4))
    print(p)