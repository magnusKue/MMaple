import pygame_gui, pygame, random, definitions, time, math

class Camera:
    def __init__(self, parent):
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1
        self.parent = parent

    def handleEvents(self, event, rootSize, project):
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed(3)[1]:
                self.offset += pygame.Vector2(event.rel[0]/self.zoom, event.rel[1]/self.zoom)
            self.parent.mapWindow.recalcSurf(project, rootSize)
            

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                self.centerCam(rootSize, project)

        elif event.type == pygame.MOUSEWHEEL:
            self.zoom = min(max(self.zoom + (event.precise_y*0.1) + (event.precise_x*0.1), 1), 1.5)
            self.parent.mapWindow.recalcSurf(project, rootSize)
            

    def centerCam(self, rootSize, project):
        self.offset.x = rootSize[0] - (0.5*rootSize[0]*.8) - (0.5 * project.getBoundingbox().x)
        self.offset.y = rootSize[1] - (0.5*rootSize[1]) - (0.5 * project.getBoundingbox().y)
        

class MapView:
    def __init__(self, rootSize, project):
        self.camera = Camera(self)
        self.camera.centerCam(rootSize, project)

        self.manager = pygame_gui.UIManager(rootSize)
        self.sidePanel = Sidepanel(self.manager, rootSize)

        self.mapWindow = MapWindow(project, self, rootSize)

        self.buttons = []
        
        buttonSize = self.getButtonSize(rootSize)
        self.buttons.append(
            ToolSwap_Button(
                pos = pygame.Vector2(rootSize[0]-buttonSize-30, 30),
                size=pygame.Vector2(buttonSize, buttonSize)
            )
        )
 
    def getButtonSize(self, rootSize):
        return max(min(rootSize[0]*0.025, 50), 35)

    def draw(self, surface, project, rootSize):
        surface.blit(self.mapWindow.getSurface(), (self.camera.offset.x, self.camera.offset.y))
        for button in self.buttons:
            button.draw(surface)
    
    def handleEvents(self, event, rootSize, project):
        self.camera.handleEvents(event, rootSize, project)
        for button in self.buttons:
            button.handleEvents(event, rootSize)

class MapWindow:
    def __init__(self, project, parent, rootSize) -> None:
        self.parent = parent
        
        bS = self.getBlockSize(rootSize, project)
        addIconScaler = 0.125
        self.addIcon = pygame.transform.scale(pygame.image.load("assets\plus.png"), (bS.x * 0.125, bS.x * 0.125)).convert_alpha()
        
        self.surf = self.recalcSurf(project, rootSize)


    def getBlockSize(self, rootSize, project):
        bSscaler = min(rootSize[0] * 0.04, 100)
        bS = pygame.Vector2(int((project.gridsize.x / project.gridsize.y) * bSscaler), bSscaler)
        return bS

    def recalcSurf(self, project, rootSize):
        bS = self.getBlockSize(rootSize, project) # blocksize
        bounds = pygame.Vector2(
            len(project.map)*bS.x,
            len(project.map)*bS.y
        )
        tempSurf =  pygame.Surface(bounds, pygame.SRCALPHA, 32).convert_alpha()
        
        relMousePos = pygame.Vector2(
            (pygame.mouse.get_pos()[0] - self.parent.camera.offset.x)/self.parent.camera.zoom,
            (pygame.mouse.get_pos()[1] - self.parent.camera.offset.y)/self.parent.camera.zoom
        )
        
        for y, row in enumerate(project.map):
            for x, room in enumerate(row):
                if not room:
                    pygame.draw.rect(tempSurf, (100,100,100), pygame.Rect(x*bS.x,  y*bS.y,  bS.x,  bS.y), 1)
                    tempSurf.blit(self.addIcon, dest=(
                        (x*bS.x + (0.5*bS.x)-(0.5 * self.addIcon.get_rect().width)),  
                        (y*bS.y + (0.5*bS.y)-(0.5 * self.addIcon.get_rect().height)))
                    )
                else:
                    pygame.draw.rect(tempSurf, (100,100,100), pygame.Rect(x*bS.x,  y*bS.y,  bS.x,  bS.y))
                if relMousePos.x  > x*bS.x  and relMousePos.y > y*bS.y :
                    if relMousePos.x < x*bS.x  + bS.x and relMousePos.y < y*bS.y + bS.y:
                        pygame.draw.rect(tempSurf, (200,100,100), pygame.Rect(x*bS.x,  y*bS.y,  bS.x,  bS.y), 2)
                        
        self.surf = pygame.transform.scale_by(tempSurf, self.parent.camera.zoom)
        return self.surf
    
    def getSurface(self) -> pygame.Surface:
        return self.surf
    
class Sidepanel:
    def __init__(self, manager, rootSize):        
        self.sidePanel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, rootSize[0]*.2, rootSize[1]),
            manager=manager,
            container=manager.get_root_container()
        )

class Button:
    def __init__(self, pos, size) -> None:
        self.pos = pos
        self.size = size

        self.image = None
        self.hovered = False
    
    def handleEvents(self, event, rootSize):
        if event.type == pygame.MOUSEMOTION:
            if event.pos[0] > self.pos[0] and event.pos[1] > self.pos[1]:
                if event.pos[0] < self.pos[0] + self.size.x and event.pos[1] < self.pos[1] + self.size.y:
                    self.hovered = True
                else: 
                    self.hovered = False
            else: 
                    self.hovered = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.hovered:
                self.clicked()

    def draw(self, surface:pygame.Surface):
        pygame.draw.rect(surface, (60,60,60), pygame.Rect(self.pos, self.size))
        pygame.draw.rect(surface, (100,100,100), pygame.Rect(self.pos, self.size), 1)
        surface.blit(self.image, pygame.Rect(self.pos, self.size))
        if self.hovered:
            transparency = pygame.Surface(self.size, pygame.SRCALPHA, 32)
            transparency.fill((255,255,255,100))
            surface.blit(transparency,self.pos)
            
    def loadIcon(self, path) -> pygame.Surface:
        self.image = pygame.transform.scale(pygame.image.load(path), self.size)
        return self.image
    
    def clicked(self):
        pass


class ToolSwap_Button(Button):
    def __init__(self, pos, size) -> None:
        super().__init__(pos, size)
        self.mode = definitions.EXPANDTOOL
        self.loadIcon("assets\expandTool.png")

    def clicked(self):
        if self.mode == definitions.MOVETOOL:
            self.mode = definitions.EXPANDTOOL
            self.loadIcon("assets\expandTool.png")
        elif self.mode == definitions.EXPANDTOOL:
            self.mode = definitions.MOVETOOL
            self.loadIcon("assets\cursor.png")

        