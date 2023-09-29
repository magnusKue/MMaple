import pygame_gui, pygame

class camera:
    def __init__(self):
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1

class MapView:
    def __init__(self, rootSize):
        self.manager = pygame_gui.UIManager(rootSize)
        self.sidePanel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, rootSize[0]*.2, rootSize[1]),
            manager=self.manager,
            container=self.manager.get_root_container()
        )

    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), pygame.Rect(200,200,1000,1000))