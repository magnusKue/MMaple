import pygame, definitions

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
