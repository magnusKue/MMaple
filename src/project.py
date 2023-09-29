import struc, pygame

class Project:
    def __init__(self):
        self.map = [ # filled with either rooms or none
            None, None, None, None,
            None, None, None, None,
            None, None, None, None,
            None, None, None, None
        ]

        self.gridsize = pygame.Vector2() # size of rooms
        self.pointer = None