import pygame, definitions
import pygame_gui
import tkinter as tk
from tkinter import colorchooser

class Button:
    def __init__(self, pos, size) -> None:
        self.pos = pos
        self.size = size

        self.margin = 6

        self.image = None
        self.hovered = False
    
    def handleEvents(self, event, project):
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
                self.clicked()

    def draw(self, surface:pygame.Surface, project):
        pygame.draw.rect(surface, (60,60,60), pygame.Rect(self.pos, self.size))
        pygame.draw.rect(surface, (100,100,100), pygame.Rect(self.pos, self.size), 1)
        if self.image:
            surface.blit(self.image, pygame.Rect((self.pos.x+self.margin, self.pos.y+self.margin), self.size))
        if self.hovered and not project.blocking:
            transparency = pygame.Surface(self.size, pygame.SRCALPHA, 32)
            transparency.fill((255,255,255,30))
            surface.blit(transparency,self.pos)
            
    def loadIcon(self, path) -> pygame.Surface:
        self.image = pygame.transform.scale(pygame.image.load(path), (self.size.x-(2*self.margin), self.size.y-(2*self.margin)))
        return self.image
    
    def clicked(self):
        pass

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

class Save_Button(Button):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.loadIcon("assets\save.png")
    
    def clicked(self):
        print("this is the part where its supposed to save")

class Project_Button(Button):
    def __init__(self, pos, size, parent):
        super().__init__(pos, size)
        self.loadIcon("assets\save.png")
        self.parent = parent

    def clicked(self):
        self.parent.initProjectWindow(
            manager=self.parent.parent.manager, 
            project=self.projectStamp, 
            rootSize=self.rootSizeStamp
        )
    
    def handleEvents(self, event, project, rootSize):
        super().handleEvents(event, project)
        self.projectStamp = project
        self.rootSizeStamp = rootSize

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
        
class areaEditButton(Button):
    def __init__(self, pos, size, parent):
        super().__init__(pos, size)
        self.loadIcon("assets\edit.png")
        self.parent = parent
        self.rootSizeStamp = None
        self.projectStamp = None

    def clicked(self):
        self.parent.initAreaWindow(
            manager=self.parent.parent.manager,
            rootSize=self.rootSizeStamp
        )
        self.projectStamp.blocking = True

    def handleEvents(self, event, project, rootSize, mapWindow):
        super().handleEvents(event, project) 
        self.rootSizeStamp = rootSize
        self.projectStamp = project
