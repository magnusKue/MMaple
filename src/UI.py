import pygame, pygame_gui
import uiRoomView, uiMapView, uiStartView
from definitions import *


class UI:
    def __init__(self, rootSize, project, startViewValues = False):
        if not startViewValues:
            startViewValues = {
                            "name" : "new project",
                            "mapX" : "20",
                            "mapY" : "20",
                            "roomX" : "30",
                            "roomY" : "25",
                            "path" : ""
                        }
        self.mapView = uiMapView.MapView(rootSize, project)
        self.roomView = uiRoomView.RoomView(rootSize)
        self.startView = uiStartView.StartView(rootSize, project, startViewValues)
        
    def getManager(self, project):
        if project.mode == MAPVIEW:
            return self.mapView.manager
            
        elif project.mode == ROOMVIEW:
            return self.roomView.manager
        
        elif project.mode == STARTVIEW:
            return self.startView.manager
    
    def draw(self, surface, project, rootSize):
        if project.mode == MAPVIEW:
            self.mapView.draw(surface, project, rootSize)
            self.mapView.manager.draw_ui(surface)
            self.mapView.drawFront(surface, project, rootSize)
            
        elif project.mode == ROOMVIEW:
            self.roomView.manager.draw_ui(surface)
        
        elif project.mode == STARTVIEW:
            self.startView.manager.draw_ui(surface)

    def handleEvents(self, event, rootSize, project):
        if project.mode == MAPVIEW:
            self.mapView.handleEvents(event, rootSize, project)
        elif project.mode == STARTVIEW:
            self.startView.handleEvents(event, rootSize, project, self)