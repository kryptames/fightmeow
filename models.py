import arcade
class Meow:
    def __init__(self):
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
        self.meow_list = []
        meow = Meow()
        self.meow_list.append(meow)
        self.coin = Coin()
        self.block_food = BlockFood()
        self.meow_sprite_list = arcade.SpriteList()
        meow_sprite = arcade.Sprite('images/meow.png')
        meow_sprite.center_x = 400
        meow_sprite.center_y = 325
        self.meow_sprite_list.append(meow_sprite)
 
    def update(self, delta):
        # self.meow.update(delta)
        pass
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.meow_list.append(Meow())
            meow_sprite = arcade.Sprite('images/meow.png')
            meow_sprite.center_x = 600
            meow_sprite.center_y = 325
            self.meow_sprite_list.append(meow_sprite)
