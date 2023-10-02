import pygame
from struc import *

class Project:
    def __init__(self):
        self.gridsize = pygame.Vector2(25,15) # size of rooms

        self.rooms = [
            Room((255,0,0))
        ]
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

        ref = Block(self)
        ref.room = 0
        self.map = [ # filled with either none or self.room index pointers 
        #    [None,  Block(self),      None,   None,None,None],
        #    [Block(self),     Block(self),      Block(self),Block(self),Block(self),      None],
        #    [Block(self),     None,   Block(self),Block(self),None,      None],
        #    [None,   Block(self),     Block(self),      None,None,Block(self)]
        #]
            [None, None, None, None, ref, None, None, None],
            [None, None, None, ref, ref, None, ref, None],
            [None, None, None, ref, None, ref, None, None],
            [None, None, None, ref, ref, ref, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]

        self.selectedBlock = pygame.Vector2(-1,-1)
        self.blocking = False
    
    def getSelected(self):
        return self.map[int(self.selectedBlock.y)][int(self.selectedBlock.x)]

    def getBoundingbox(self, rootSize, project):
        bSscaler = min(rootSize[0] * 0.04, 50)
        bS = pygame.Vector2(int((project.gridsize.x / project.gridsize.y) * bSscaler), bSscaler)
        return pygame.Vector2(
            len(self.map[0]) * bS.x,
            len(self.map) * bS.y
        )