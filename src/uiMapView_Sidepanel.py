import pygame_gui
import pygame

class Toppanel:
    def __init__(self, manager, rootSize):        
        self.sidePanel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, min(rootSize[0]*.2, 450), rootSize[1]*0.5),
            manager=manager,
            container=manager.get_root_container()
        )

class Bottompanel:
    def __init__(self, manager, rootSize):        
        self.sidePanel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, rootSize[1]*0.5, min(rootSize[0]*.2, 450), rootSize[1]*0.5),
            manager=manager,
            container=manager.get_root_container()
        )