import numpy as np

class World:
    #biomeNames = ['empty', 'grassland', 'forest', 'jungle', 'savanna', 'desert', 'wetland', 'tundra', 'artic', 'reef', 'marine', 'ocean']
    def __init__(self, size):
        assert len(size) == 2
        self.size = size

        self.biomes = np.array(self.size, dtype=np.uint8)
        self.biome_debris = np.array(self.biomes.shape, dtype=np.uint16)

        self.population = []

    def generate_world(self, circle=True):
        from FerfunBiomeGenerator import FerfunBiomeGen
        if circle:
            self.biomes = FerfunBiomeGen.BiomeGeneratorCircle(self.size, Biome.lenght - 1, 2, 6)
        else:
            self.biomes = FerfunBiomeGen.BiomeGeneratorDiamond(self.size, Biome.lenght - 1, 3, 10)

class Biome:
    names = ['empty', 'grassland', 'forest', 'jungle', 'savanna', 'desert', 'wetland', 'tundra', 'artic', 'reef', 'marine', 'ocean']

    lenght = 12

    namesDict = {
            'empty' : 0,
            'grassland' : 1,
            'forest' : 2,
            'jungle' : 3,
            'savanna' : 4,
            'desert' : 5,
            'wetland' : 6,
            'tundra' : 7,
            'artic' : 8,
            'reef' : 9,
            'marine' : 10,
            'ocean' : 11
        }

    colours = np.array([
        [192, 192, 192],
        [0, 255, 0],
        [0, 135, 0],
        [153, 255, 102],
        [255, 153, 0],
        [255, 255, 0],
        [0, 153, 153],
        [204, 255, 255],
        [255, 255, 255],
        [153, 255, 255],
        [0, 255, 255],
        [0, 102, 204]
    ])

    # Light level is 0 - 100
    lights = np.array([0, 70, 60, 80, 90, 100, 50, 40, 20, 80, 50, 10])

    # Temperature level is 0 - 100    
    temperature = np.array([0, 40, 50, 80, 90, 100, 50, 10, 5, 70, 30, 15])

    # Humidity level is 0 - 100
    humidity = np.array([0, 50, 60, 95, 35, 5, 85, 25, 5, 100, 100, 100])

    @staticmethod
    def GetColourFromIndex(index: int):
        return Biome.colours[index]

    @staticmethod
    def GetLightFromIndex(index: int):
        return Biome.lights[index]

    @staticmethod
    def GetTempFromIndex(index: int):
        return Biome.temperature[index]

    @staticmethod
    def GetHumFromIndex(index: int):
        return Biome.humidity[index]

    @staticmethod
    def GetColourFromName(name: str):        
        return Biome.colours[Biome.names[name]]

    @staticmethod 
    def GetLightFromName(name: str):
        return Biome.lights[Biome.names[name]]

    @staticmethod 
    def GetTempFromName(name: str):
        return Biome.temperature[Biome.names[name]]

    @staticmethod 
    def GetHumFromName(name: str):  
        return Biome.humidity[Biome.names[name]]