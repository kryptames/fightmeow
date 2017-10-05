class Meow:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.hungry = 100
    
    def update(self, delta):
        pass
            
    def eat(self,food):
        if self.hungry<100:
            self.hungry+=food

class BlockFood:
    def __init__(self):
        self.x = 50
        self.y = 650
    def add_food(self):
        self.food = Food()

class Food:
    def __init__(self):
        self.food = 100
        GET = 5
    def eaten(self):
        self.food -= GET

class Coin:
    def __init__(self):
        self.x = 650
        self.y = 675
        START_COIN = 10
        self.coin = START_COIN

class World:
    def __init__(self, width, height,img):
        START_COIN = 10
        self.width = width
        self.height = height
        self.background = img
        self.meow = Meow(self, 400, 325)
        self.coin = Coin()
        self.block_food = BlockFood()
        
 
    def update(self, delta):
        self.meow.update(delta)