import pygame

class Camera:
    def __init__(self, parent):
        self.offset = pygame.Vector2(0,0)
        self.zoom = 1
        self.parent = parent

    def handleEvents(self, event, rootSize, project):
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed(3)[1]:
                self.offset += pygame.Vector2(event.rel[0], event.rel[1])
            
            mousePos = (pygame.mouse.get_pos() - self.parent.camera.offset)/self.zoom
            bS = self.parent.mapWindow.getBlockSize(rootSize, project)

            if mousePos.x > 0 and mousePos.x < len(project.map[0]) * bS.x:
                if (mousePos.y > 0 and mousePos.y < len(project.map[1]) * bS.y) or (self.parent.mapWindow.hoveredBlock != pygame.Vector2(-1,-1)):
                    self.parent.mapWindow.recalcSurf(project, rootSize)
            elif self.parent.mapWindow.hoveredBlock != pygame.Vector2(-1,-1):
                self.parent.mapWindow.recalcSurf(project, rootSize)
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                self.centerCam(rootSize, project)

        elif event.type == pygame.MOUSEWHEEL:
            self.zoom = min(max(self.zoom + (event.precise_y*0.1) + (event.precise_x*0.1), 1), 2)
            self.parent.mapWindow.recalcSurf(project, rootSize)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and event.pos[0] > min(rootSize[0]*.2, 450):
                project.selectedBlock = self.parent.mapWindow.hoveredBlock
                self.parent.mapWindow.recalcSurf(project, rootSize)
            

    def centerCam(self, rootSize, project):
        self.offset.x = rootSize[0] - (0.5*rootSize[0]*.8) - (0.5 * project.getBoundingbox(rootSize, project).x)
        self.offset.y = rootSize[1] - (0.5*rootSize[1]) - (0.5 * project.getBoundingbox(rootSize, project).y)

class MapWindow:
    def __init__(self, project, parent, rootSize) -> None:
        self.parent = parent
        
        bS = self.getBlockSize(rootSize, project)
        addIconScaler = 0.125
        self.addIcon = pygame.transform.scale(pygame.image.load("assets\plus.png"), (bS.x * 0.125, bS.x * 0.125)).convert_alpha()
        
        self.surf = self.recalcSurf(project, rootSize)
        self.hoveredBlock = pygame.Vector2(-1,-1)


    def getBlockSize(self, rootSize, project):
        bSscaler = min(rootSize[0] * 0.04, 50)
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

        hovered = False
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

                if pygame.Vector2(x,y) == project.selectedBlock:
                    pygame.draw.rect(tempSurf, (200,200,200), pygame.Rect(x*bS.x,  y*bS.y,  bS.x,  bS.y), 2)
                if relMousePos.x  > x*bS.x  and relMousePos.y > y*bS.y :
                    if relMousePos.x < x*bS.x  + bS.x and relMousePos.y < y*bS.y + bS.y:
                        pygame.draw.rect(tempSurf, (200,100,100), pygame.Rect(x*bS.x,  y*bS.y,  bS.x,  bS.y), 2)
                        self.hoveredBlock = pygame.Vector2(x,y)
                        hovered = True
        if not hovered:
            self.hoveredBlock = pygame.Vector2(-1,-1)
                        
        self.surf = pygame.transform.scale_by(tempSurf, self.parent.camera.zoom)
        return self.surf
    
    def getSurface(self) -> pygame.Surface:
        return self.surf