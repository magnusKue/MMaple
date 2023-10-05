import pygame_gui 
import pygame
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import definitions


        
class StartView:
    def __init__(self, rootSize, project, initVals):
        self.manager = pygame_gui.UIManager(rootSize, project.themePath)

        self.maxNumber = 2
        self.maxNameLen = 20

        size = pygame.Vector2(600,500)
        self.mainPanel = pygame_gui.elements.UIPanel(
            pygame.Rect((rootSize[0]*0.5)-(size.x*0.5), (rootSize[1]*0.5)-(size.y*0.5) ,size.x,size.y),
            manager   = self.manager,
            container = self.manager.get_root_container()
        )

        mainContainer = self.mainPanel.get_container()

        if True: # LOADPANEL
            self.loadPanel = pygame_gui.elements.UIPanel(
                pygame.Rect(10, 40, mainContainer.get_rect().w-20, mainContainer.get_rect().h*0.3),
                manager   = self.manager,
                container = mainContainer
            )

            self.loadText = pygame_gui.elements.UILabel(
                pygame.Rect(0, 0, self.loadPanel.get_container().get_rect().w, 25),
                text = "load project:",
                manager = self.manager, 
                container = self.loadPanel.get_container()
            )
            self.loadText.set_tooltip("Load an existing Project. Choose one from your recents or load from a file!")

        if True: # CREATE PANEL
            self.createPanel = pygame_gui.elements.UIPanel(
                pygame.Rect(10, self.loadPanel.get_abs_rect().h+45, mainContainer.get_rect().w-20, self.mainPanel.get_abs_rect().h - self.loadPanel.get_abs_rect().h-65),
                manager   = self.manager,
                container = mainContainer
            )

            self.createText = pygame_gui.elements.UILabel(
                pygame.Rect(0, 0, self.createPanel.get_container().get_rect().w, 25),
                text = "new project:",
                manager = self.manager, 
                container = self.createPanel.get_container()
            )
            self.createText.set_tooltip("Create a new Project!")

            blockShift = 30
            xS = 150 # xShift
            cW = self.createPanel.get_container().get_rect().w*0.4
            s = 35 # scaler

            if True: ## TEXT
                self.nameText = pygame_gui.elements.UILabel(
                    pygame.Rect(0, s+blockShift, 0.5*cW, 25),
                    text = "name:       ",
                    manager = self.manager, 
                    container = self.createPanel.get_container()
                )
                self.nameText.set_tooltip("determines under which filename the project is saved")

                self.mapSizeText = pygame_gui.elements.UILabel(
                    pygame.Rect(0, 2*s+blockShift, 0.5*cW, 25),
                    text = "map size:   ",
                    manager = self.manager, 
                    container = self.createPanel.get_container()
                )
                self.mapSizeText.set_tooltip("sets the number of blocks on the map")

                if True: # MAP: X && Y
                    self.mapSizeXText = pygame_gui.elements.UILabel(
                        pygame.Rect(xS+cW*0.3-5, (2*s)+blockShift, 15, 25),
                        text = "X",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                    self.mapSizeXText = pygame_gui.elements.UILabel(
                        pygame.Rect(xS + cW*0.8, (2*s)+blockShift, 15, 25),
                        text = "Y",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                self.roomSizeText = pygame_gui.elements.UILabel(
                    pygame.Rect(0, 3*s+blockShift, 0.5*cW, 25),
                    text = "block size: ",
                    manager = self.manager, 
                    container = self.createPanel.get_container()
                )
                self.roomSizeText.set_tooltip("sets the number of tiles per block")
                

                if True: # ROOM: X && Y
                    self.roomSizeXText = pygame_gui.elements.UILabel(
                        pygame.Rect(xS+cW*0.3-5, 3*s+blockShift, 15, 25),
                        text = "X",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                    self.roomSizeXText = pygame_gui.elements.UILabel(
                        pygame.Rect(xS + cW*0.8, 3*s+blockShift, 15, 25),
                        text = "Y",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                self.pathText = pygame_gui.elements.UILabel(
                    pygame.Rect(0, 4*s+blockShift, 0.5*cW, 25),
                    text = "directory:  ",
                    manager = self.manager, 
                    container = self.createPanel.get_container()
                )
                self.pathText.set_tooltip("determines where the project is saved to")

            if True: ## INPUT
                if True: # NAME INPUT
                     self.nameInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS, s+blockShift, cW, 25),
                        initial_text=initVals["name"],
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                if True: # MAPSIZE INPUTS
                    self.mapSizeXInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS, 2*s+blockShift, cW*0.3-5, 25),
                        initial_text=initVals["mapX"],
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )
                    self.mapSizeXInput.set_allowed_characters("numbers")

                    self.mapSizeYInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS + cW*0.5 + 5, 2*s+blockShift, cW*0.3-5, 25),
                        initial_text=initVals["mapY"],
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )
                    self.mapSizeYInput.set_allowed_characters("numbers")
                
                if True: # ROOMSIZE INPUTS
                    self.roomSizeXInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS, 3*s+blockShift, cW*0.3-5, 25),
                        initial_text=initVals["roomX"],
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )
                    self.roomSizeXInput.set_allowed_characters("numbers")
    
                    self.roomSizeYInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS + cW*0.5 + 5, 3*s+blockShift, cW*0.3-5, 25),
                        initial_text=initVals["roomY"],
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )
                    self.roomSizeYInput.set_allowed_characters("numbers")

                if True: # PATH INPUTS
                    self.pathInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS, 4*s+blockShift, cW - 65, 25),
                        initial_text=initVals["path"],
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                    self.pathButton = pygame_gui.elements.UIButton(
                        pygame.Rect(xS + cW - 60, 4*s+blockShift, 60, 25),
                        text="open",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

            self.createButton = pygame_gui.elements.UIButton(
                pygame.Rect(
                    5, 
                    self.createPanel.get_container().get_rect().h - 30 - 30, 

                    0.3*self.createPanel.get_container().get_rect().w, 
                    25
                ),
                text="create",
                manager = self.manager, 
                container = self.createPanel.get_container()
            )

            errorWindowSize = pygame.Vector2(300,200)

            self.errorWindow = pygame_gui.elements.UIWindow(
                pygame.Rect((rootSize[0]*0.5) - (errorWindowSize.x*0.5), (rootSize[1]*0.5) - (errorWindowSize.y*0.5), errorWindowSize.x, errorWindowSize.y),
                manager=self.manager
            )
            self.errorWindow.hide()

            self.errors = {
                "project name":False,
                "roomsize":False,
                "mapsize":False,
                "directory":False
            }
                    

    def handleEvents(self, event, rootSize, project, ui):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.pathButton:
                self.pathInput.set_text(str(filedialog.askdirectory()))

            elif event.ui_element == self.createButton:
                if self.checkValidInputs():
                    self.nameInput.set_text(str(self.nameInput.get_text()).strip())
                    self.createProject(project, ui, rootSize)
                else:
                    self.initErrorWindow(self.errors, rootSize)
        
        elif event.type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
            for element in [self.mapSizeXInput, self.mapSizeXText, self.roomSizeXInput, self.roomSizeYInput]:
                if event.ui_element == element:
                    if len(event.text) > self.maxNumber:
                        element.set_text(event.text[:self.maxNumber])
            if event.ui_element == self.nameInput:
                if len(event.text) > self.maxNameLen:
                        self.nameInput.set_text(event.text[:self.maxNameLen])

    def initErrorWindow(self, errors, rootSize):   
        errorList = [key for key in errors.keys() if errors[key]]

        errorWindowSize = pygame.Vector2(300,len(errorList)* 25 + 100)
        self.errorWindow = pygame_gui.elements.UIWindow(
            pygame.Rect((rootSize[0]*0.5) - (errorWindowSize.x*0.5), (rootSize[1]*0.5) - (errorWindowSize.y*0.5), errorWindowSize.x, errorWindowSize.y),
            manager=self.manager
        )
        self.errorWindow.set_blocking(True)
        self.errorWindow.window.draggable = False
        self.errorWindow.set_display_title("Creation failed!!")

        wC = self.errorWindow.get_container() # window container
        self.descText = pygame_gui.elements.UILabel(
            pygame.Rect(5,5, wC.get_rect().w-10, 25),
            text="Please fix the following Errors:",
            container=wC,
            manager=self.manager
        )

        self.errorTexts = []
        for index, error in enumerate(errorList):
            self.errorTexts.append(
                pygame_gui.elements.UILabel(
                    pygame.Rect(5,35 + index * 25, wC.get_rect().w-10, 25),
                    text=str("input valid "+error),
                    container=wC,
                    manager=self.manager
                )
            )

    def createProject(self, project, ui, rootSize):
        project.name = self.nameInput.get_text()
        project.gridsize = pygame.Vector2(int(self.roomSizeXInput.get_text()), int(self.roomSizeYInput.get_text()))
        project.map =  [ [None]*int(self.mapSizeXInput.get_text()) for i in range(int(self.mapSizeYInput.get_text()))]

        project.mode = definitions.MAPVIEW
        ui.mapView.mapWindow.recalcSurf(project, rootSize)
        pygame.display.set_caption("MMaple :: " + project.name)

    def checkPath(self):
        txt = str(self.pathInput.get_text())
        path = Path(txt)
        if path.is_dir() and txt:
            return True
        return False
    
    def checkValidInputs(self):
        self.errors = {
            "project name":False,
            "roomsize":False,
            "mapsize":False,
            "directory":False
        }
        
        if not self.checkPath():
            self.errors["directory"] = True
        
        for element in [self.mapSizeXInput, self.mapSizeXInput]:
            if not element.get_text():
                self.errors["mapsize"] = True
            elif int(element.get_text()) == 0:        
                self.errors["mapsize"] = True
        
        for element in [self.roomSizeXInput, self.roomSizeYInput]:
            if not element.get_text():
                self.errors["roomsize"] = True
            elif int(element.get_text()) == 0:        
                self.errors["roomsize"] = True     
            
        if not self.nameInput.get_text():
            self.errors["project name"] = True   
        
        if [key for key in self.errors.keys() if self.errors[key]]:
            return False
        return True # ALL CHECKS PASSED!!
        
        