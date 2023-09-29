import pygame
from pygame.locals import *

class Window:
    def __init__(self, rootSize):
        self.rootSize = rootSize
        self.root = pygame.display.set_mode(self.rootSize, RESIZABLE)
        pygame.display.set_caption("Maple")