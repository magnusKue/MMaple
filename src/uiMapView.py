import pygame_gui, pygame, random

class Camera:
    def __init__(self):
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1

        self.down = False
        self.downPos = pygame.Vector2(0,0)
    def handleEvents(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                self.downPos = event.pos
                self.down = True

        elif event.type == pygame.MOUSEMOTION and self.down:
            self.offset += event.rel
        
        elif event.type == pygame.MOUSEBUTTONUP:
            self.down = False
        

class MapView:
    def __init__(self, rootSize):
        self.camera = Camera()
        self.manager = pygame_gui.UIManager(rootSize)
        self.sidePanel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, rootSize[0]*.2, rootSize[1]),
            manager=self.manager,
            container=self.manager.get_root_container()
        )

    def draw(self, surface, project):
        bS = pygame.Vector2(int((project.gridsize.x / project.gridsize.y) * 100), 100) # blocksize

        for y, row in enumerate(project.map):
            for x, room in enumerate(row):
                if not room:
                    pygame.draw.rect(surface, (100,100,100), pygame.Rect(200+x*bS.x+self.camera.offset.x,200+y*bS.y+self.camera.offset.y,bS.x,bS.y), 1)
                else:
                    pygame.draw.rect(surface, (100,100,100), pygame.Rect(200+x*bS.x+self.camera.offset.x,200+y*bS.y+self.camera.offset.y,bS.x,bS.y))

