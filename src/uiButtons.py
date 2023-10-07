import pygame, definitions
import pygame_gui
import tkinter as tk
from tkinter import colorchooser
class ColorButton:
    def __init__(self, pos, size, color=(255,0,0)) -> None:
        self.pos = pos
        self.size = size

        self.margin = 6

        self.color = color
        self.hovered = False
    
    def handleEvents(self, event, project, mapWindow, rootSize):
        if event.type == pygame.MOUSEMOTION:
            if event.pos[0] > self.pos[0] and event.pos[1] > self.pos[1]:
                if event.pos[0] < self.pos[0] + self.size.x and event.pos[1] < self.pos[1] + self.size.y:
                    self.hovered = True
                else: 
                    self.hovered = False
            else: 
                self.hovered = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.hovered and not project.blocking:
                self.clicked(project, mapWindow, rootSize)

    def draw(self, surface:pygame.Surface, project):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.pos, self.size))
        pygame.draw.rect(surface, (int(self.color[0]*0.7), int(self.color[1]*0.7), int(self.color[2]*0.7)), pygame.Rect(self.pos, self.size), 1)
        if self.hovered and not project.blocking:
            transparency = pygame.Surface(self.size, pygame.SRCALPHA, 32)
            transparency.fill((255,255,255,30))
            surface.blit(transparency,self.pos)

    def clicked(self, project, mapWindow, rootSize):
        pass

class RoomColorButton(ColorButton):
    def __init__(self, pos, size, project, color=(255, 0, 0)) -> None:
        super().__init__(pos, size, color)
        if project.selectedBlock != pygame.Vector2(-1,-1):
            if project.getSelected():
                self.color = project.rooms[project.getSelected().room].color
            else:
                self.color = (100,100,100)
        else:
            self.color = (80,80,80)
    
    def handleEvents(self, event, project, rootSize, mapWindow):
        super().handleEvents(event, project, mapWindow, rootSize)
        if project.selectedBlock != pygame.Vector2(-1,-1):
            if project.getSelected():
                self.color = project.rooms[project.getSelected().room].color
            else:
                self.color = (150,50,50)
        else:
            self.color = (150,50,50)    
    
    def clicked(self, project, mapWindow, rootSize):
        if project.getSelected():
            choosenColor = colorchooser.askcolor(title ="Choose a new room color!", initialcolor=project.rooms[project.getSelected().room].color)[0]
            if choosenColor:
                project.rooms[project.getSelected().room].color = choosenColor
            mapWindow.recalcSurf(project, rootSize)
