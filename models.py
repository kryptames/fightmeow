import arcade,random
class Meow:
    def __init__(self):
        self.hungry = 100
        self.time = 0
        self.level = 1
        self.damage = random.randint(0,30)
        self.exp = 0

    def update(self, delta):
        self.time+=delta
        if self.time < 10:
            return
        self.time = 0
        self.hungry-=10

    def eat(self,food):
        if self.hungry<100 and self.time == 0:
            self.hungry+=food.get
            food.eaten()

class Enemy(arcade.Sprite):
    def __init__(self,filename, SCALE):
        super().__init__(filename, SCALE)
        self.damage = random.randint(0,30)

class BlockFood:
    def __init__(self):
        self.x = 50
        self.y = 650

class Food:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.status = 100
        self.get = 10
    def eaten(self):
        self.status -= self.get
        
    def buy(self):
        self.status += 30

class Coin:
    def __init__(self):
        self.x = 650
        self.y = 675
        START_COIN = 50
        self.coin = START_COIN
    def buy_meow(self):
        self.coin -= 10
    def buy_food(self):
        self.coin -= 2

class World:
    def __init__(self, width, height,img):
        self.position = [(600,325),(565,100),(360,200)]
        self.used_position =[(400,325)]
        self.width = width
        self.height = height
        self.background = img
        self.coin = Coin()
        self.block_food = BlockFood()
        self.food = Food()

        # set class meow list 
        self.meow_list = []
        meow = Meow()
        self.meow_list.append(meow)

        #  set arcade meow
        self.meow_sprite_list = arcade.SpriteList()
        meow_sprite = arcade.Sprite('images/meow.png')
        meow_sprite.center_x = 400
        meow_sprite.center_y = 325
        self.meow_sprite_list.append(meow_sprite)
 
    def update(self, delta):
        for i in range(len(self.meow_list)):
            self.meow_list[i].update(delta)
            # eat food 
            if self.food.status > 0:
                self.meow_list[i].eat(self.food)
            # starving
            if self.meow_list[i].hungry<=0:
                self.position.append((self.meow_sprite_list[i].center_x,self.meow_sprite_list[i].center_y))
                del self.meow_list[i]
                self.meow_sprite_list[i].kill()
                break

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            if self.coin.coin > 0 and len(self.position) > 0:
                # add meow
                self.meow_list.append(Meow())
                meow_sprite = arcade.Sprite('images/meow.png')
                position = self.position.pop(random.randint(0,len(self.position)-1))
                meow_sprite.set_position(position[0],position[1])
                self.used_position.append((position[0],position[1]))
                self.meow_sprite_list.append(meow_sprite)
                self.coin.buy_meow()
                print(position)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and (x > 25 and x < 75 ) and (y > 625 and y < 675):
            self.food.buy()
            self.coin.buy_food()

class Choose:
    def __init__(self,world,img):
        self.world = world
        self.background = img
    def update(self):
        pass
    
