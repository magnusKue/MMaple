import pygame_gui, pygame, random

class Camera:
    def __init__(self):
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1

    def handleEvents(self, event, rootSize, project):
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed(3)[1]:
                self.offset += event.rel
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                self.centerCam(rootSize, project)

    def centerCam(self, rootSize, project):
        self.offset.x = rootSize[0] - (0.5*rootSize[0]*.8) - (0.5 * project.getBoundingbox().x)
        self.offset.y = rootSize[1] - (0.5*rootSize[1]) - (0.5 * project.getBoundingbox().y)
        

class MapView:
    def __init__(self, rootSize, project):
        self.camera = Camera()
        self.camera.centerCam(rootSize, project)
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
                    pygame.draw.rect(surface, (100,100,100), pygame.Rect(x*bS.x+self.camera.offset.x,  y*bS.y+self.camera.offset.y,  bS.x,  bS.y), 1)
                else:
                    pygame.draw.rect(surface, (100,100,100), pygame.Rect(x*bS.x+self.camera.offset.x,  y*bS.y+self.camera.offset.y,  bS.x,  bS.y))

