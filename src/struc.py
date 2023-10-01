import pygame
from definitions import *

class Tiletype:
    def __init__(self) -> None:
        self.image = ""

class Tilemanager:
    def __init__(self):
        self.types = {
            "default" : Tiletype()
        }

class Tilemap:
    def __init__(self, gridSize) -> None:
        map = [ # Tiles stored as IDs, accessed through the tile manager
            ["default","default","default"],
            ["default","default","default"],
            ["default","default","default"],
            ["default","default","default"]
        ]

class ShapeRect:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.shape = pygame.Rect(x1, y1, x2, y2)
        

class Collisionmanager: # stores all types of collisionshapes
    def __init__(self):
        self.types = {
            "full" : ShapeRect(0,0,1,1)
        }

class Collisionmap:
    def __init__(self) -> None:
        map = [ # shapes stored as IDs, accessed through the collision manager
            ["full","full","full","full"],
            ["full","full","full","full"],
            ["full","full","full","full"],
            ["full","full","full","full"]
        ]

class Room:
    def __init__(self):
        self.area = "none"


class Block:
    def __init__(self, project):
        self.gridsize = project.gridsize

        self.room = None

        self.layers = [
            Tilemap(self.gridsize), 
            Collisionmap()
        ]

        self.doors = {
            UP : False, 
            DOWN : False,   
            LEFT : False,   
            RIGHT : False   
        }
