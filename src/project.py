import pygame
from struc import *

class Project:
    def __init__(self):
        self.gridsize = pygame.Vector2(25,15) # size of rooms

        self.rooms = [
            None,
            None,
            None,
            None
        ]
        self.map = [ # filled with either none or self.room index pointers 
        #    [None,  Block(self),      None,   None,None,None],
        #    [Block(self),     Block(self),      Block(self),Block(self),Block(self),      None],
        #    [Block(self),     None,   Block(self),Block(self),None,      None],
        #    [None,   Block(self),     Block(self),      None,None,Block(self)]
        #]
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]

        self.selectedBlock = pygame.Vector2(-1,-1)
    
    def getBoundingbox(self, rootSize, project):
        bSscaler = min(rootSize[0] * 0.04, 100)
        bS = pygame.Vector2(int((project.gridsize.x / project.gridsize.y) * bSscaler), bSscaler)
        return pygame.Vector2(
            len(self.map[0]) * bS.x,
            len(self.map) * bS.y
        )