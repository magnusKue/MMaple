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
            [None,  Block(self),      None,   None],
            [Block(self),     Block(self),      Block(self),      None],
            [Block(self),     None,   Block(self),      None],
            [None,   Block(self),     Block(self),      Block(self)]
        ]

        self.pointer = None