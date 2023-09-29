import pygame, pygame_gui, random
import uiRoomView
import uiMapView 
from definitions import *


class UI:
    def __init__(self, rootSize, app):
        self.mode = MAPVIEW

        self.mapManager = pygame_gui.UIManager(rootSize)
        self.roomManager = pygame_gui.UIManager(rootSize)

        self.mapView = uiMapView.MapView(self.mapManager, rootSize)
        self.roomView = uiRoomView.RoomView(self.roomManager)
        
    def getManager(self):
        if self.mode == MAPVIEW:
            return self.mapManager
            
        elif self.mode == ROOMVIEW:
            return self.roomManager

    def handleEvents(self, event, app):
        pass