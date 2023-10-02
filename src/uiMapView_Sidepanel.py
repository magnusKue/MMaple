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

class OptionPanel:
    def __init__(self, manager, rootSize, parent, project): 
        self.parent = parent       
        self.Panel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, min(rootSize[0]*.2, 450), 50),
            manager=manager,
            container=manager.get_root_container()
        )

        self.saveButton = uiButtons.Save_Button(
            pos  = pygame.Vector2(5,5), 
            size = pygame.Vector2(40, 40)
        )
        self.saveButton.loadIcon("assets/save.png")

        self.projectButton = uiButtons.Project_Button(
            pos  = pygame.Vector2(50,5), 
            size = pygame.Vector2(40, 40),
            parent= self
        )
        self.projectButton.loadIcon("assets/save.png")

        self.projectWindow = ProjectWindow(
            rootSize=rootSize,
            manager=manager,
            project=project
        )
        self.projectWindow.window.hide()

    def initProjectWindow(self, manager, project, rootSize):
        self.projectWindow = ProjectWindow(
            rootSize,
            manager=manager,
            project=project
        )
        self.projectWindow.window.set_display_title("Project properties")
        project.blocking = True


        
    def handleEvents(self, event, project, rootSize):
        self.saveButton.handleEvents(event, project)
        self.projectButton.handleEvents(event, project, rootSize)

        if event.type == pygame_gui.UI_WINDOW_CLOSE:
            project.blocking = False

    def draw(self, surface, project):
        self.saveButton.draw(surface, project)
        self.projectButton.draw(surface, project)

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
                text=">",
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
                text="<",
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
                text="\/",
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
                text="/\\",
                container=self.Panel.get_container(),
                manager=manager
            )

    def handleEvents(self, event, project, rootSize):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.createBlockButton:
                self.createBlock(project)
                self.parent.mapWindow.recalcSurf(project, rootSize)
            
            if event.ui_element == self.createBottomBlockButton: self.copyBlock(project, 0, 1);self.parent.mapWindow.recalcSurf(project, rootSize)
            if event.ui_element == self.createTopBlockButton:    self.copyBlock(project, 0, -1);self.parent.mapWindow.recalcSurf(project, rootSize)
            if event.ui_element == self.createLeftBlockButton:   self.copyBlock(project, -1, 0);self.parent.mapWindow.recalcSurf(project, rootSize)
            if event.ui_element == self.createRightBlockButton:  self.copyBlock(project, 1, 0);self.parent.mapWindow.recalcSurf(project, rootSize)

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
        
    def draw(self, surface, project):
        if not project.getSelected() and project.selectedBlock != pygame.Vector2(-1,-1):
            for button in [self.createBlockButton, self.createTopBlockButton, self.createBottomBlockButton, self.createLeftBlockButton, self.createRightBlockButton]:
                button.show()
        else:
            for button in [self.createBlockButton, self.createTopBlockButton, self.createBottomBlockButton, self.createLeftBlockButton, self.createRightBlockButton]:
                button.hide()



class Bottompanel:
    def __init__(self, manager, rootSize):        
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
                (rootSize[0]*0.5) - 250,
                (rootSize[1]*0.5) - 250,
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

