import pygame_gui
import pygame, random
import struc, uiButtons

class ToolPanel:
    def __init__(self, manager, rootSize, parent): 
        self.parent = parent       
        height = min(rootSize[1]-200, 700) 
        margin = int(0.5*(rootSize[1]-height))
        self.Panel = pygame_gui.elements.UIPanel(
            pygame.Rect(rootSize[0]-50, margin, 60, rootSize[1] - (2*margin)),
            manager=manager,
            container=manager.get_root_container()
        )

        self.toolSwapButton = pygame_gui.elements.UIButton(
            relative_rect= pygame.Rect(5,5,40,40),
            manager=manager,
            container=self.Panel.get_container(),
            text="",
            object_id=pygame_gui.core.ObjectID(object_id="#toolSwapButton")
        )
    
    def handleEvents(self, event, project, rootSize):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.toolSwapButton:
                print("swapedy swap swap")

class OptionPanel:
    def __init__(self, manager, rootSize, parent, project): 
        self.parent = parent       
        self.Panel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, min(rootSize[0]*.2, 450), 50),
            manager=manager,
            container=manager.get_root_container()
        )

        self.saveButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(0,0,self.Panel.get_abs_rect().h-6,self.Panel.get_abs_rect().h-6),
            text="",
            manager = self.parent.manager,
            container = self.Panel.get_container(),
            object_id=pygame_gui.core.ObjectID(object_id="#saveButton")
        )


        self.projectButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.Panel.get_abs_rect().h-6,0,self.Panel.get_abs_rect().h-6,self.Panel.get_abs_rect().h-6),
            text="",
            manager = self.parent.manager,
            container = self.Panel.get_container(),
            object_id=pygame_gui.core.ObjectID(object_id="#projectButton")
        )

        self.projectWindow = ProjectWindow(
            rootSize=rootSize,
            manager=manager,
            project=project
        )
        self.projectWindow.draggable = False
        self.projectWindow.window.hide()

    def initProjectWindow(self, manager, project, rootSize):
        self.projectWindow = ProjectWindow(
            rootSize,
            manager=manager,
            project=project
        )
        self.projectWindow.window.set_display_title("Project properties")
        self.projectWindow.window.draggable = False
        project.blocking = True
     
    def handleEvents(self, event, project, rootSize):
        if event.type == pygame_gui.UI_WINDOW_CLOSE:
            project.blocking = False
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.projectButton:
                self.initProjectWindow(self.parent.manager, project, rootSize)
            elif event.ui_element == self.saveButton:
                print("this is the part where it's supposed to save")

class Toppanel:
    def __init__(self, manager, rootSize, parent): 
        self.parent = parent       
        self.Panel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 50, min(rootSize[0]*.2, 450), rootSize[1]*0.5-50),
            manager=manager,
            container=manager.get_root_container()
        )

        self.blockNameLabel = pygame_gui.elements.UILabel(
            pygame.Rect(
                10,10,
                self.Panel.get_container().get_rect().width-10,
                20
            ),
            text="Block:",
            container=self.Panel.get_container(),
            manager=manager
        )

        if True: ## CREATION BUTTONS
            buttonSL = 50 # button sidelength 
            self.createBlockButton = pygame_gui.elements.UIButton(
                pygame.Rect(
                    (0.5*self.Panel.get_container().get_rect().width) - (0.5*buttonSL),
                    (0.5*self.Panel.get_container().get_rect().height) - (0.5*buttonSL),
                    buttonSL,
                    buttonSL
                ),
                text="+",
                container=self.Panel.get_container(),
                manager=manager
            )

            self.createLeftBlockButton = pygame_gui.elements.UIButton(
                pygame.Rect(
                    (0.5*self.Panel.get_container().get_rect().width) - (0.5*buttonSL) - buttonSL - 5,
                    (0.5*self.Panel.get_container().get_rect().height) - (0.5*buttonSL),
                    buttonSL,
                    buttonSL
                ),
                text="⇨",
                container=self.Panel.get_container(),
                manager=manager
            )

            self.createRightBlockButton = pygame_gui.elements.UIButton(
                pygame.Rect(
                    (0.5*self.Panel.get_container().get_rect().width) - (0.5*buttonSL) + buttonSL + 5,
                    (0.5*self.Panel.get_container().get_rect().height) - (0.5*buttonSL),
                    buttonSL,
                    buttonSL
                ),
                text="⇦",
                container=self.Panel.get_container(),
                manager=manager
            )

            self.createTopBlockButton = pygame_gui.elements.UIButton(
                pygame.Rect(
                    (0.5*self.Panel.get_container().get_rect().width) - (0.5*buttonSL) ,
                    (0.5*self.Panel.get_container().get_rect().height) - (0.5*buttonSL)- buttonSL - 5,
                    buttonSL,
                    buttonSL
                ),
                text="⇩",
                container=self.Panel.get_container(),
                manager=manager
            )

            self.createBottomBlockButton = pygame_gui.elements.UIButton(
                pygame.Rect(
                    (0.5*self.Panel.get_container().get_rect().width) - (0.5*buttonSL) ,
                    (0.5*self.Panel.get_container().get_rect().height) - (0.5*buttonSL)+ buttonSL + 5,
                    buttonSL,
                    buttonSL
                ),
                text="⇧",
                container=self.Panel.get_container(),
                manager=manager
            )

    def handleEvents(self, event, project, rootSize):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if   event.ui_element == self.createBlockButton:       self.createBlock(project);       self.parent.mapWindow.recalcSurf(project, rootSize)  
            elif event.ui_element == self.createBottomBlockButton: self.copyBlock(project, 0, 1);   self.parent.mapWindow.recalcSurf(project, rootSize)
            elif event.ui_element == self.createTopBlockButton:    self.copyBlock(project, 0, -1);  self.parent.mapWindow.recalcSurf(project, rootSize)
            elif event.ui_element == self.createLeftBlockButton:   self.copyBlock(project, -1, 0);  self.parent.mapWindow.recalcSurf(project, rootSize)
            elif event.ui_element == self.createRightBlockButton:  self.copyBlock(project, 1, 0);   self.parent.mapWindow.recalcSurf(project, rootSize)

    def copyBlock(self, project, x,y):
        if x==-1 and int(project.selectedBlock.x) == 0: return
        if y==-1 and int(project.selectedBlock.y) == 0: return
        if x==1 and int(project.selectedBlock.x) == len(project.map[0])-1: return
        if y==1 and int(project.selectedBlock.y) == len(project.map)-1: return
        if not project.map[int(project.selectedBlock.y)+y][int(project.selectedBlock.x)+x]: return
        newBlock = struc.Block(project)
        newBlock.room = project.map[int(project.selectedBlock.y)+y][int(project.selectedBlock.x)+x].room # add index of room
        project.map[int(project.selectedBlock.y)][int(project.selectedBlock.x)] = newBlock
    
    def createBlock(self, project):
        availableCol = project.roomColorDefaults
        for room in project.rooms:
            if room.color in availableCol:
                availableCol.remove(room.color) 

        if availableCol:
            col = random.choice(availableCol)
        else:
            col = (random.randint(0,170), random.randint(0,170), random.randint(0,170))
        
        project.rooms.append(struc.Room(color = col))

        newBlock = struc.Block(project)
        newBlock.room = len(project.rooms)-1 # add index of room
        project.map[int(project.selectedBlock.y)][int(project.selectedBlock.x)] = newBlock
        
    def draw(self, surface, project): # check neighbours to see if buttons should be visible or not
        if not project.getSelected() and project.selectedBlock != pygame.Vector2(-1,-1):
            self.createBlockButton.show()
            if project.selectedBlock.y > 0:
                if project.map[int(project.selectedBlock.y-1)][int(project.selectedBlock.x)]:
                    self.createTopBlockButton.show()
                else: self.createTopBlockButton.hide()
            if project.selectedBlock.x > 0:
                if project.map[int(project.selectedBlock.y)][int(project.selectedBlock.x-1)]:
                    self.createLeftBlockButton.show()
                else: self.createLeftBlockButton.hide()
            if project.selectedBlock.y < len(project.map)-1:
                if project.map[int(project.selectedBlock.y+1)][int(project.selectedBlock.x)]:
                    self.createBottomBlockButton.show()
                else: self.createBottomBlockButton.hide()
            if project.selectedBlock.x < len(project.map)-1:
                if project.map[int(project.selectedBlock.y)][int(project.selectedBlock.x+1)]:
                    self.createRightBlockButton.show()
                else: self.createRightBlockButton.hide()
        else:
            for button in [self.createBlockButton, self.createTopBlockButton, self.createBottomBlockButton, self.createLeftBlockButton, self.createRightBlockButton]:
                button.hide()

    def drawFront(self, surface, project):
        if project.getSelected():
            pR = self.Panel.get_abs_rect()
            pygame.draw.rect(
                surface, 
                (100,100,100), 
                pygame.Rect(
                    pR.left+ 25,
                    pR.top + 38,
                    pR.width-50,
                    150
                ),
                2
            )

class Bottompanel:
    def __init__(self, manager, rootSize, project, parent):   
        self.parent = parent     
        self.Panel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, rootSize[1]*0.5, min(rootSize[0]*.2, 450), rootSize[1]*0.5),
            manager=manager,
            container=manager.get_root_container()
        )

        self.blockNameLabel = pygame_gui.elements.UILabel(
            pygame.Rect(
                10,10,
                self.Panel.get_container().get_rect().width-10,
                20
            ),
            text="Room:",
            container=self.Panel.get_container(),
            manager=manager
        )

        self.areaText = pygame_gui.elements.UILabel(
            pygame.Rect(
                10,92,
                int(self.Panel.get_container().get_rect().width*.3),
                20
            ),
            text = "Area:     ",
            container=self.Panel.get_container(),
            manager=manager
        )

        self.areaDropdown = pygame_gui.elements.UIDropDownMenu(
            relative_rect=pygame.Rect(
                int(self.Panel.get_container().get_rect().width*.2),
                90,
                int(self.Panel.get_container().get_rect().width*.6),
                25
            ),
            options_list=["queen's garden", "deepnest", "greenpath", "kingdom's edge"],
            starting_option="queen's garden",
            container=self.Panel.get_container(),
            manager=manager
        )

        self.areaEditButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(int(self.Panel.get_container().get_rect().width*.8) + 5,90,25,25),
            text="",
            manager=manager,
            container=self.Panel.get_container(),
            object_id=pygame_gui.core.ObjectID(object_id="#areaEditButton")
        )

        self.colorText = pygame_gui.elements.UILabel(
            pygame.Rect(
                10,50,
                int(self.Panel.get_container().get_rect().width*.3),
                20
            ),
            text = "Color:    ",
            container=self.Panel.get_container(),
            manager=manager
        )

        self.colorButton = uiButtons.RoomColorButton(
            pos=pygame.Vector2(
                self.Panel.get_container().get_rect().left - 2 + int(self.Panel.get_container().get_rect().width*.5),
                self.Panel.get_container().get_rect().top + 50
            ),
            size=pygame.Vector2(self.Panel.get_container().get_rect().width*.3, 20),
            project=project
        )

        self.areaWindow = AreaWindow(manager, rootSize)
        self.areaWindow.window.set_blocking(True)
        self.areaWindow.window.hide()

    def handleEvents(self, event, project, rootSize, mapWindow):
        self.colorButton.handleEvents(event, project, rootSize, mapWindow)

        if event.type == pygame_gui.UI_WINDOW_CLOSE:
            if event.ui_element == self.areaWindow:
                project.blocking = False
                
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.areaEditButton:
                self.initAreaWindow(manager=self.parent.manager, rootSize=rootSize)
                project.blocking = True

    def drawFront(self, surface, project):
        self.colorButton.draw(surface, project)

    def initAreaWindow(self, manager, rootSize):
        self.areaWindow = AreaWindow(manager, rootSize)
        self.areaWindow.window.set_blocking(True)
        self.areaWindow.window.draggable = False

class ProjectWindow:
    def __init__(self, rootSize, manager, project) -> None:

        values = {
            "project name:":f"[ {project.name} ]",
            "map size:":f"[ {len(project.map[0])} | {len(project.map)} ]",
            "block size:":f"[ {int(project.gridsize.x)} | {int(project.gridsize.x)} ]"
        }

        windowSize = pygame.Vector2(300,len(values)* 25 + 100)
        self.window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(
                (rootSize[0]*0.5) - (.5*windowSize.x),
                (rootSize[1]*0.5) - (.5*windowSize.y),
                windowSize.x,
                windowSize.y
            ),
            manager=manager
        )
        self.window.set_blocking(True)

        wC = self.window.get_container() # window container
        self.descText = pygame_gui.elements.UILabel(
            pygame.Rect(5,5, wC.get_rect().w-10, 25),
            text="Project properties:",
            container=wC,
            manager=manager
        )

        self.items = []
        for index, valuePair in enumerate(values.items()):
            self.items.append(
                pygame_gui.elements.UILabel(
                    pygame.Rect(5,35 + index * 25, wC.get_rect().w-10, 25),
                    text=f"{valuePair[0]} {valuePair[1]}",
                    container=wC,
                    manager=manager
                )
            )

class AreaWindow:
    def __init__(self, manager, rootSize):

        self.window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(
                (rootSize[0]*0.5) - 250,
                (rootSize[1]*0.5) - 250,
                500,
                500
            ),
            manager=manager
        )
        self.window.set_blocking(True)

        wC = self.window.get_container() # window container
        self.descText = pygame_gui.elements.UILabel(
            pygame.Rect(5,5, wC.get_rect().w-10, 25),
            text="Areas:",
            container=wC,
            manager=manager
        )

