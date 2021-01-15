import pygame
import numpy as np
from Environment import World, Biome

SIZES = [
    (12, 8),
    (24, 16),
    (48, 32),
    (96, 64),
    (192, 128)
]

class Simulation:
    resolution = (960, 640)

    def __init__(self, size_index: int, fps: int, simSpeed: float, world_randomizer=True):
        pygame.init()

        self.fps = fps
        self.simSpeed = simSpeed

        self.deltaTime = 0

        self.size = SIZES[size_index]
        self.screen = pygame.display.set_mode(Simulation.resolution)
        self.clock = pygame.time.Clock()

        self.running = True

        self.world = World(self.size)
        self.tile_size = np.array([Simulation.resolution[0]//self.size[0], Simulation.resolution[1]//self.size[1]], dtype=np.uint16)

    def world_init(self):
        self.world.generate_world()

    def draw_world(self):
        for r in range(self.size[0]):
            for c in range(self.size[1]):
                self.draw_quad(Biome.GetColourFromIndex(self.world.biomes[r][c]), (r, c))


    def draw_quad(self, col, coords, scale=1):
        upleft = (coords[1] * self.tile_size[0], coords[0] * self.tile_size[1])
        if scale == 1:            
            self.draw_rect(upleft, self.tile_size, col)
        else:
            offset = (1 - scale) * 0.5
            self.draw_rect((round(upleft[0] + offset * self.tile_size[0]), round(upleft[1] + offset * self.tile_size[1])), (round(self.tile_size[0] * scale), round(self.tile_size[1] * scale)), col)      

    def draw_rect(self, upleft, widthheight, col):
        pygame.draw.rect(self.screen, col, (upleft[0], upleft[1], widthheight[0], widthheight[1]))

    def window_title(self):
        pygame.display.set_caption('Lyber Engine 2.0 - {:.2f}'.format(self.clock.get_fps()))

    def loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.window_title()
            self.screen.fill((0, 0, 0))

            self.draw_world()

            self.deltaTime = self.clock.tick(self.fps)
            pygame.display.update()
        pygame.quit()

def main():
    sim = Simulation(0, 30, 1)
    sim.world_init()

    sim.loop()

if __name__ == '__main__':
    main()