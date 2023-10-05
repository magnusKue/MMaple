import pygame_gui 
import pygame, random, time, math
import uiButtons, uiMapView_Window,uiMapView_Sidepanel, definitions


        
class MapView:
    def __init__(self, rootSize, project):
        self.camera = uiMapView_Window.Camera(self)
        self.camera.centerCam(rootSize, project)

        self.manager = pygame_gui.UIManager(rootSize)

        self.optionsPanel = uiMapView_Sidepanel.OptionPanel(self.manager, rootSize, self, project)
        self.topPanel = uiMapView_Sidepanel.Toppanel(self.manager, rootSize, self)
        self.bottomPanel = uiMapView_Sidepanel.Bottompanel(self.manager, rootSize, project, self)
        self.toolPanel = uiMapView_Sidepanel.ToolPanel(self.manager, rootSize, self)


        self.mapWindow = uiMapView_Window.MapWindow(project, self, rootSize)

        self.buttons = []
        
        buttonSize = 40
        self.buttons.append(
            uiButtons.ToolSwap_Button(
                pos = pygame.Vector2(rootSize[0]-buttonSize-5, int(0.5*(rootSize[1]-min(rootSize[1]-200, 700)))+5),
                size = pygame.Vector2(buttonSize, buttonSize)
            )
        )

    def drawFront(self, surface, project, rootSize):
        for button in self.buttons:
            button.draw(surface, project)
        self.optionsPanel.draw(surface, project)
        self.topPanel.drawFront(surface, project)
        self.bottomPanel.drawFront(surface, project)

    def draw(self, surface, project, rootSize):
        surface.blit(self.mapWindow.getSurface(), (self.camera.offset.x, self.camera.offset.y))
        self.topPanel.draw(surface, project)
    
    def handleEvents(self, event, rootSize, project):
        self.camera.handleEvents(event, rootSize, project)
        for button in self.buttons:
            button.handleEvents(event, project)

        self.mapWindow.handleEvents(event, project, rootSize)
        self.optionsPanel.handleEvents(event, project, rootSize)
        self.topPanel.handleEvents(event, project, rootSize)
        self.bottomPanel.handleEvents(event, project, rootSize)
