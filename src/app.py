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
        self.ui = UI(self.window.rootSize, self)
        
        

    def run(self):
        while self.running:
            deltatime = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:				
                    if event.key == K_ESCAPE:
                        running = False

                if event.type == pygame.VIDEORESIZE:
                    #self.ui.mapManager.set_window_resolution(event.size)
                    #self.ui.roomManager.set_window_resolution(event.size)
                    self.window.rootSize = event.size
                    self.ui = UI(self.window.rootSize, self)	

                self.ui.getManager().process_events(event)
                self.ui.handleEvents(event, self)

            self.ui.getManager().update(deltatime)
            self.window.root.fill(self.ui.getManager().ui_theme.get_colour('dark_bg'))

            self.ui.getManager().draw_ui(self.window.root)
            pygame.display.flip()
        pygame.quit()
        sys.exit()