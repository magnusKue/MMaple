import pygame_gui
import pygame
import struc

class Toppanel:
    def __init__(self, manager, rootSize):        
        self.sidePanel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, 0, min(rootSize[0]*.2, 450), rootSize[1]*0.5),
            manager=manager,
            container=manager.get_root_container()
        )

        self.blockNameLabel = pygame_gui.elements.UILabel(
            pygame.Rect(
                10,10,
                self.sidePanel.get_container().get_rect().width-10,
                20
            ),
            text="Block:",
            container=self.sidePanel.get_container(),
            manager=manager
        )

        self.createBlockButton = pygame_gui.elements.UIButton(
            pygame.Rect(
                5,
                self.sidePanel.get_container().get_rect().height * 0.5 - 15,
                self.sidePanel.get_container().get_rect().width-10,
                30
            ),
            text="create new block",
            container=self.sidePanel.get_container(),
            manager=manager
        )

    def handleEvents(self, event, project):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            project.rooms.append(struc.Room())
            newBlock = struc.Block(project)
            newBlock.room = project.rooms[-1] # add index of room
            project.map[int(project.selectedBlock.y)][int(project.selectedBlock.x)] = newBlock

    def draw(self, surface, project):
        if not project.map[int(project.selectedBlock.y)][int(project.selectedBlock.x)] and project.selectedBlock != pygame.Vector2(-1,-1):
            self.createBlockButton.show()
        else:
            self.createBlockButton.hide()



class Bottompanel:
    def __init__(self, manager, rootSize):        
        self.sidePanel = pygame_gui.elements.UIPanel(
            pygame.Rect(0, rootSize[1]*0.5, min(rootSize[0]*.2, 450), rootSize[1]*0.5),
            manager=manager,
            container=manager.get_root_container()
        )