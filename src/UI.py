import pygame, pygame_gui, random
import uiRoomView
import uiMapView 
from definitions import *


class UI:
    def __init__(self, rootSize, app):
        self.mode = MAPVIEW

        self.mapView = uiMapView.MapView(rootSize)
        self.roomView = uiRoomView.RoomView(rootSize)
        
    def getManager(self):
        if self.mode == MAPVIEW:
            return self.mapView.manager
            
        elif self.mode == ROOMVIEW:
            return self.roomView.manager
    
    def draw(self, surface):
        if self.mode == MAPVIEW:
            self.mapView.draw(surface)
            self.mapView.manager.draw_ui(surface)
            
        elif self.mode == ROOMVIEW:
            self.roomView.manager.draw_ui(surface)

    def handleEvents(self, event, app):
        pass