class Meow:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.hungry = 100
    
    def update(self, delta):
        if delta %50 ==0:
            self.hungry -=5
            
    def eat(self,food):
        if self.hungry<100:
            self.hungry+=food
class Food:
    def __init__(self,number):
        self.food = 100
        self.get = number*5
    def eaten(self):
        self.food -= self.get
    
class World:
    def __init__(self, width, height,img):
        START_COIN = 10
        self.width = width
        self.height = height
        self.background = img
        self.meow = Meow(self, 400, 325)
        self.coin = START_COIN
 
    def update(self, delta):
        self.meow.update(delta)