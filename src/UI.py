import pygame, pygame_gui
import uiRoomView, uiMapView, uiStartView
from definitions import *


class UI:
    def __init__(self, rootSize, project):
        self.mode = STARTVIEW

        self.mapView = uiMapView.MapView(rootSize, project)
        self.roomView = uiRoomView.RoomView(rootSize)
        self.startView = uiStartView.StartView(rootSize, project)
        
    def getManager(self):
        if self.mode == MAPVIEW:
            return self.mapView.manager
            
        elif self.mode == ROOMVIEW:
            return self.roomView.manager
        
        elif self.mode == STARTVIEW:
            return self.startView.manager
    
    def draw(self, surface, project, rootSize):
        if self.mode == MAPVIEW:
            self.mapView.draw(surface, project, rootSize)
            self.mapView.manager.draw_ui(surface)
            self.mapView.drawFront(surface, project, rootSize)
            
        elif self.mode == ROOMVIEW:
            self.roomView.manager.draw_ui(surface)
        
        elif self.mode == STARTVIEW:
            self.startView.manager.draw_ui(surface)

    def handleEvents(self, event, rootSize, project):
        if self.mode == MAPVIEW:
            self.mapView.handleEvents(event, rootSize, project)
        elif self.mode == STARTVIEW:
            self.startView.handleEvents(event, rootSize, project)