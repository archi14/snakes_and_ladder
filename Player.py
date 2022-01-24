class Player():

    def __init__(self, name, position=0):
        self.name = name
        self.position = position
    
    def get_position(self):
        return self.position
    
    def updatePosition(self, position):
        self.position = position

