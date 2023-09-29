import pygame_gui, pygame, random

class Camera:
    def __init__(self, parent):
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1
        self.parent = parent

    def handleEvents(self, event, rootSize, project):
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed(3)[1]:
                self.offset += pygame.Vector2(event.rel[0]/self.zoom, event.rel[1]/self.zoom)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                self.centerCam(rootSize, project)

        if event.type == pygame.MOUSEWHEEL:
            self.zoom = min(max(self.zoom + (event.precise_y*0.1) + (event.precise_x*0.1), 1), 1.5)
            self.parent.recalcSurf(project)
            

    def centerCam(self, rootSize, project):
        self.offset.x = rootSize[0] - (0.5*rootSize[0]*.8) - (0.5 * project.getBoundingbox().x)
        self.offset.y = rootSize[1] - (0.5*rootSize[1]) - (0.5 * project.getBoundingbox().y)
        

class MapView:
    def __init__(self, rootSize, project):
        self.camera = Camera(self)
        self.camera.centerCam(rootSize, project)
        self.manager = pygame_gui.UIManager(rootSize)
        self.sidePanel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, rootSize[0]*.2, rootSize[1]),
            manager=self.manager,
            container=self.manager.get_root_container()
        )

        self.surf = self.recalcSurf(project)

    def draw(self, surface, project):
        surface.blit(self.surf, (self.camera.offset.x, self.camera.offset.y))
    
    def recalcSurf(self, project):
        print("recalculated")
        bS = pygame.Vector2(int((project.gridsize.x / project.gridsize.y) * 100), 100) # blocksize
        bounds = pygame.Vector2(
            len(project.map)*bS.x,
            len(project.map)*bS.y
        )
        tempSurf =  pygame.Surface(bounds, pygame.SRCALPHA, 32).convert_alpha()
        for y, row in enumerate(project.map):
            for x, room in enumerate(row):
                if not room:
                    pygame.draw.rect(tempSurf, (100,100,100), pygame.Rect(x*bS.x,  y*bS.y,  bS.x,  bS.y), 1)
                else:
                    pygame.draw.rect(tempSurf, (100,100,100), pygame.Rect(x*bS.x,  y*bS.y,  bS.x,  bS.y))

        self.surf = pygame.transform.scale_by(tempSurf, self.camera.zoom)
        return self.surf

