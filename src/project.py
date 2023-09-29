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
            [None,  Block(self),      None,   None,None,None],
            [Block(self),     Block(self),      Block(self),Block(self),Block(self),      None],
            [Block(self),     None,   Block(self),Block(self),None,      None],
            [None,   Block(self),     Block(self),      None,None,Block(self)]
        ]

        self.pointer = None
    
    def getBoundingbox(self):
        bS = pygame.Vector2(int((self.gridsize.x / self.gridsize.y) * 100), 100)
        return pygame.Vector2(
            len(self.map[0]) * bS.x,
            len(self.map) * bS.y
        )