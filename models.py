import arcade,random
class Meow:
    def __init__(self):
        self.hungry = 100
        self.time = 0
    def update(self, delta):
        self.time+=delta
        if self.time < 5:
            return
        self.time = 0
        self.hungry-=10
            
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
        self.position = [(400,325),(600,325),(565,100),(360,200)]
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
        for i in range(len(self.meow_list)):
            self.meow_list[i].update(delta)
            if self.meow_list[i].hungry<=0:
                del self.meow_list[i]
                self.meow_sprite_list[i].kill()
                break


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            if self.coin.coin > 0:
                self.meow_list.append(Meow())
                meow_sprite = arcade.Sprite('images/meow.png')
                position = self.position[random.randint(0,3)]
                meow_sprite.set_position(position[0],position[1])
                self.meow_sprite_list.append(meow_sprite)
                self.coin.coin -= 5

