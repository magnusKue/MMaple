import pygame, pygame_gui
import uiRoomView, uiMapView 
from definitions import *


class UI:
    def __init__(self, rootSize, project):
        self.mode = MAPVIEW

        self.mapView = uiMapView.MapView(rootSize, project)
        self.roomView = uiRoomView.RoomView(rootSize)
        
    def getManager(self):
        if self.mode == MAPVIEW:
            return self.mapView.manager
            
        elif self.mode == ROOMVIEW:
            return self.roomView.manager
    
    def draw(self, surface, project, rootSize):
        if self.mode == MAPVIEW:
            self.mapView.draw(surface, project, rootSize)
            self.mapView.manager.draw_ui(surface)
            
        elif self.mode == ROOMVIEW:
            self.roomView.manager.draw_ui(surface)

    def handleEvents(self, event, rootSize, project):
        self.mapView.handleEvents(event, rootSize, project)