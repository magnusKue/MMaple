import pygame_gui
import pygame, random
import struc, uiButtons

class OptionPanel:
    def __init__(self, manager, rootSize, parent): 
        self.parent = parent       
        self.Panel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, min(rootSize[0]*.2, 450), 50),
            manager=manager,
            container=manager.get_root_container()
        )

        self.saveButton = uiButtons.Button(
            pos  = pygame.Vector2(5,5), 
            size = pygame.Vector2(40, 40)
        )
        self.saveButton.loadIcon("assets/save.png")
        
    def handleEvents(self, event):
        self.saveButton.handleEvents(event)

    def draw(self, surface):
        self.saveButton.draw(surface)

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

        self.createBlockButton = pygame_gui.elements.UIButton(
            pygame.Rect(
                5,
                self.Panel.get_container().get_rect().height * 0.5 - 30,
                self.Panel.get_container().get_rect().width-10,
                60
            ),
            text="create new block",
            container=self.Panel.get_container(),
            manager=manager
        )

    def handleEvents(self, event, project, rootSize):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.createBlockButton:
                self.createBlock(project)
                self.parent.mapWindow.recalcSurf(project, rootSize)

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
            self.createBlockButton.show()
        else:
            self.createBlockButton.hide()



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