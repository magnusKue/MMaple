import pygame_gui 
import pygame


        
class StartView:
    def __init__(self, rootSize, project):
        self.manager = pygame_gui.UIManager(rootSize)
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

            blockShift = 0
            xS = 150 # xShift
            cW = self.createPanel.get_container().get_rect().w*0.4

            if True: ## TEXT
                self.nameText = pygame_gui.elements.UILabel(
                    pygame.Rect(0, 50+blockShift, 0.5*cW, 25),
                    text = "name:       ",
                    manager = self.manager, 
                    container = self.createPanel.get_container()
                )

                self.mapSizeText = pygame_gui.elements.UILabel(
                    pygame.Rect(0, 100+blockShift, 0.5*cW, 25),
                    text = "map size:   ",
                    manager = self.manager, 
                    container = self.createPanel.get_container()
                )

                if True: # MAP: X && Y
                    self.mapSizeXText = pygame_gui.elements.UILabel(
                        pygame.Rect(xS+cW*0.3-5, 100+blockShift, 15, 25),
                        text = "X",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                    self.mapSizeXText = pygame_gui.elements.UILabel(
                        pygame.Rect(xS + cW*0.8, 100+blockShift, 15, 25),
                        text = "Y",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                self.roomSizeText = pygame_gui.elements.UILabel(
                    pygame.Rect(0, 150+blockShift, 0.5*cW, 25),
                    text = "room size:  ",
                    manager = self.manager, 
                    container = self.createPanel.get_container()
                )

                if True: # ROOM: X && Y
                    self.roomSizeXText = pygame_gui.elements.UILabel(
                        pygame.Rect(xS+cW*0.3-5, 150+blockShift, 15, 25),
                        text = "X",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                    self.roomSizeXText = pygame_gui.elements.UILabel(
                        pygame.Rect(xS + cW*0.8, 150+blockShift, 15, 25),
                        text = "Y",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                self.pathText = pygame_gui.elements.UILabel(
                    pygame.Rect(0, 200+blockShift, 0.5*cW, 25),
                    text = "directory:  ",
                    manager = self.manager, 
                    container = self.createPanel.get_container()
                )



            if True: ## INPUT
                if True: # NAME INPUT
                     self.nameInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS, 50+blockShift, cW, 25),
                        initial_text="new project",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                if True: # MAPSIZE INPUTS
                    self.mapSizeXInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS, 100+blockShift, cW*0.3-5, 25),
                        initial_text="20",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )
                    self.mapSizeXInput.set_allowed_characters("numbers")

                    self.mapSizeYInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS + cW*0.5 + 5, 100+blockShift, cW*0.3-5, 25),
                        initial_text="20",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )
                    self.mapSizeYInput.set_allowed_characters("numbers")
                
                if True: # ROOMSIZE INPUTS
                    self.roomSizeXInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS, 150+blockShift, cW*0.3-5, 25),
                        initial_text="25",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )
                    self.roomSizeXInput.set_allowed_characters("numbers")
    
                    self.roomSizeYInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS + cW*0.5 + 5, 150+blockShift, cW*0.3-5, 25),
                        initial_text="15",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )
                    self.roomSizeYInput.set_allowed_characters("numbers")

                if True: # PATH INPUTS
                    self.pathInput = pygame_gui.elements.UITextEntryLine(
                        pygame.Rect(xS, 200+blockShift, cW - 65, 25),
                        initial_text="",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                    self.pathButton = pygame_gui.elements.UIButton(
                        pygame.Rect(xS + cW - 60, 200+blockShift, 60, 25),
                        text="open",
                        manager = self.manager, 
                        container = self.createPanel.get_container()
                    )

                    

    def handleEvents(self, event, rootSize, project):
        pass