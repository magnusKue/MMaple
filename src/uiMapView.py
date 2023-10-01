import pygame_gui 
import pygame, random, time, math
import uiButtons, uiMapView_Window, definitions


        
class MapView:
    def __init__(self, rootSize, project):
        self.camera = uiMapView_Window.Camera(self)
        self.camera.centerCam(rootSize, project)

        self.manager = pygame_gui.UIManager(rootSize)
        self.sidePanel = Sidepanel(self.manager, rootSize)

        self.mapWindow = uiMapView_Window.MapWindow(project, self, rootSize)

        self.buttons = []
        
        buttonSize = self.getButtonSize(rootSize)
        self.buttons.append(
            uiButtons.ToolSwap_Button(
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




        