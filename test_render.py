import pygame
import random

resolution = (900, 600)
tile_size = (30, 30)
grid_shape = (900//30, 600//30)

data_shape = (30, 20, 3)
data = []
for row in range(data_shape[0]):
    data.append([])
    for col in range(data_shape[1]):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        data[-1].append(pygame.Color(r, g, b))

pygame.init()
screen = pygame.display.set_mode(resolution)

def draw_quad(pos, col):
    raw_pos = (pos[0] * tile_size[0], pos[1] * tile_size[1])
    rect = pygame.Rect(raw_pos[0], raw_pos[1], tile_size[0], tile_size[1])
    pygame.draw.rect(screen, col, rect)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for row in range(grid_shape[0]):
        for col in range(grid_shape[1]):
            draw_quad((row, col), data[row][col])

    pygame.display.update()

pygame.quit()