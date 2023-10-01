import pygame, pygame_gui
from pygame.locals import *
from window import Window
from project import Project
from UI import *
from definitions import *
import sys

class App:
    def __init__(self):
        self.running = True

        success, failures = pygame.init()
        print(f"successes: {success}\nfailures: {failures}")

        self.project = Project()

        self.clock = pygame.time.Clock()

        self.window = Window([1500,800])
        self.ui = UI(self.window.rootSize, self.project)
        
        

    def run(self):
        while self.running:
            deltatime = self.clock.tick()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:				
                    if event.key == K_ESCAPE:
                        running = False

                if event.type == pygame.VIDEORESIZE:
                    width,height = event.size
                    width = max(1000, width)
                    height = max(800, height)
                    self.window = Window([width, height])
                    self.ui = UI(self.window.rootSize, self.project)	

                self.ui.getManager().process_events(event)
                self.ui.handleEvents(event, self.window.rootSize, self.project)

            self.ui.getManager().update(deltatime)
            self.window.root.fill(self.ui.getManager().ui_theme.get_colour('dark_bg'))
            #print(int(self.clock.get_fps()))
            self.ui.draw(self.window.root, self.project, self.window.rootSize)
            pygame.display.flip()
        pygame.quit()
        sys.exit()