import pygame_gui
import pygame

class Sidepanel:
    def __init__(self, manager, rootSize):        
        self.sidePanel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, rootSize[0]*.2, rootSize[1]),
            manager=manager,
            container=manager.get_root_container()
        )