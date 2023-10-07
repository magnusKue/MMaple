import pygame_gui 
import pygame, random, time, math
import uiButtons, uiMapView_Window,uiMapView_Sidepanel, definitions


        
class MapView:
    def __init__(self, rootSize, project):
        self.camera = uiMapView_Window.Camera(self)
        self.camera.centerCam(rootSize, project)

        self.manager = pygame_gui.UIManager(rootSize, project.themePath)
    
        self.optionsPanel = uiMapView_Sidepanel.OptionPanel(self.manager, rootSize, self, project)
        self.topPanel = uiMapView_Sidepanel.Toppanel(self.manager, rootSize, self)
        self.bottomPanel = uiMapView_Sidepanel.Bottompanel(self.manager, rootSize, project, self)
        self.toolPanel = uiMapView_Sidepanel.ToolPanel(self.manager, rootSize, self)


        self.mapWindow = uiMapView_Window.MapWindow(project, self, rootSize)

        

    def drawFront(self, surface, project, rootSize):
        self.topPanel.drawFront(surface, project)
        self.bottomPanel.drawFront(surface, project)

    def draw(self, surface, project, rootSize):
        self.topPanel.draw(surface, project)
        surface.blit(self.mapWindow.getSurface(), (self.camera.offset.x, self.camera.offset.y))
    
    def handleEvents(self, event, rootSize, project):
        for panel in [self.camera, self.mapWindow, self.optionsPanel, self.topPanel, self.toolPanel]:
            panel.handleEvents(event, project, rootSize)

        self.bottomPanel.handleEvents(event, project, rootSize, self.mapWindow)
