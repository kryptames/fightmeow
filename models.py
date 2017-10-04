class Meow:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
    def update(self, delta):
        pass
    
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background = "images/background-living.jpg"
        self.meow = Meow(self, 400, 325)
 
 
    def update(self, delta):
        self.meow.update(delta)