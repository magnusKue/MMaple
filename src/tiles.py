import pygame

class TileInstance:
    def __init__(self):
        self.tiletype = None

class Tiletype:
    def __init__(self, img) -> None:
        self.image = img

class Tiletypemanager:
    def __init__(self) -> None:
        self.types = {}

    def importNew(self, name, path) -> bool:
        try:
            self.types[name] = Tiletype(pygame.image.load(path).convert_alpha())
            return True
        except:
            return False

class Tilemap:
    def __init__(self) -> None:
        self.map = []
        