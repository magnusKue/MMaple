import pygame
from struc import *
import definitions

class Project:
    def __init__(self):
        self.name = "template"
        self.gridsize = pygame.Vector2(25,15) # size of blocks

        self.rooms = []
        self.areas = []

        self.roomColorDefaults = [
            (45,91,107),
            (196,122,83),
            (143,71,49),
            (82,73,76),
            (123,125,42),
            (124,62,82),
            (28,82,83),
            (84,85,108),
            (17,93,118),
            (211,182,41),
            (136,75,75),
            (75,136,75),
            (136,136,75),
            (136,75,106),
            (75,75,136)
        ]

        self.furtherUsedCol = []


        self.map = [ [None]*8 for i in range(8)]

        self.selectedBlock = pygame.Vector2(-1,-1)
        self.blocking = False
        self.mode = definitions.MAPVIEW
        self.themePath = "src\\theme.json"
    
    def getSelected(self):
        return self.map[int(self.selectedBlock.y)][int(self.selectedBlock.x)]

    def getBoundingbox(self, rootSize, project):
        bSscaler = min(rootSize[0] * 0.04, 50)
        bS = pygame.Vector2(int((project.gridsize.x / project.gridsize.y) * bSscaler), bSscaler)
        return pygame.Vector2(
            len(self.map[0]) * bS.x,
            len(self.map) * bS.y
        )