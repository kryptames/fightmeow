import arcade,random
class Meow:
    def __init__(self):
        self.hungry = 100
        self.time = 0
        self.level = 1
        self.damage = random.randint(0,30)
        self.exp = 0

    def update(self, delta):
        self.lvl_up()
        self.time+=delta
        if self.time < 10:
            return
        self.time = 0
        self.hungry-=10

    def eat(self,food):
        if self.hungry<100 and self.time == 0:
            self.hungry+=food.get
            food.eaten()

    def lvl_up(self):
        if self.exp >= (20 * self.level):
            self.level +=1
            self.damage_up()

    def damage_up(self):
        self.damage += self.level * 5

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
        self.x = 640
        self.y = 680
        START_COIN = 50
        self.status = START_COIN
    def buy_meow(self):
        self.status -= 10
    def buy_food(self):
        self.status -= 2

class World:
    def __init__(self, width, height,img):
        self.position = [(600,325),(565,100),(360,200)]
        self.used_position =[(400,325)]
        self.pic = [1]
        self.choose_position = [(150,550),(350,550),(550,550),(150,350)]
        self.img_meow = [""]
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
        meow_sprite = arcade.Sprite('images/meow1.png')
        meow_sprite.center_x = 400
        meow_sprite.center_y = 325
        self.meow_sprite_list.append(meow_sprite)

        # status
        self.choose_status = False
        self.fight_status = False
        self.training_status = False
        self.choose_press = False
        self.choose = ""
 
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
                del self.pic[i]
                break

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            if self.coin.status > 0 and len(self.position) > 0:
                # add meow
                self.meow_list.append(Meow())
                random_pic = random.randint(1,3)
                self.pic.append(random_pic)
                meow_sprite = arcade.Sprite('images/meow{0}.png'.format(random_pic))
                position = self.position.pop(random.randint(0,len(self.position)-1))
                meow_sprite.set_position(position[0],position[1])
                self.used_position.append((position[0],position[1]))
                self.meow_sprite_list.append(meow_sprite)
                self.coin.buy_meow()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT and (x > 25 and x < 75 ) and (y > 625 and y < 675):
            if self.coin.status > 0:
                self.food.buy()
                self.coin.buy_food()
        if button == arcade.MOUSE_BUTTON_LEFT and (x > 545 and x < 695 ) and (y > 5 and y < 55):
            self.choose_status = True
            self.choose = "FIGHT"
            print(self.choose)
            self.choose_press = True
        if button == arcade.MOUSE_BUTTON_LEFT and (x > 5 and x < 155 ) and (y > 5 and y < 55) and self.training_status == False:
            self.choose_status = True
            self.choose = "TRAIN"
            print(self.choose)
            self.choose_press = True

class Choose:
    def __init__(self,world,img):
        self.world = world
        self.background = img
        self.select = -1
        self.chose_sprite = arcade.Sprite("images/chose.png")
        self.chose_sprite.set_position(100,100)
    def update(self):
        pass
        
    def on_mouse_press(self, x, y, button, modifiers):
        # first 
        if button == arcade.MOUSE_BUTTON_LEFT and (x > 50 and x < 250 ) and (y > 450 and y < 650):
            self.chose_sprite.set_position(150,550)
            self.select = 0
        # second
        elif button == arcade.MOUSE_BUTTON_LEFT and (x > 250 and x < 450 ) and (y > 450 and y < 650) and (len(self.world.meow_list) >= 2):
            self.chose_sprite.set_position(350,550)
            self.select = 1
        # third
        elif button == arcade.MOUSE_BUTTON_LEFT and (x > 450 and x < 650 ) and (y > 450 and y < 650) and (len(self.world.meow_list) >= 3):
            self.chose_sprite.set_position(550,550)
            self.select = 2
        # forth
        elif button == arcade.MOUSE_BUTTON_LEFT and (x > 50 and x < 250 ) and (y > 250 and y < 450) and (len(self.world.meow_list) >= 4):
            self.chose_sprite.set_position(150,350)
            self.select = 3
        # select character
        if button == arcade.MOUSE_BUTTON_LEFT and (x > 505 and x < 655 ) and (y > 25 and y < 75) and self.select != -1:
            self.world.choose_press = False
            print("press")
            if self.world.choose == "TRAIN":
                self.world.training_status = True
            if self.world.choose == "FIGHT":
                self.world.fight_status = True
            #self.select = -1
            self.chose_sprite.set_position(100,100)

class Training:
    def __init__(self, world, choose):
        self.world = world
        self.choose = choose
        self.time = 0

    def update(self, delta):
        if self.time == 0:
            self.exp_increase(self.world.meow_list[self.choose.select])
            self.world.choose_status = False
        self.time+=delta
        # can't train again until 10 sec after train
        if self.time < 10:
            return
        self.choose.select = -1
        self.world.training_status = False
        self.time = 0

    def exp_increase(self,meow):
        meow.exp += random.randint(10,20)
        print("exp",meow.exp)


class Fight:
    def __init__(self, world, choose, img):
        self.world = world
        self.choose = choose
        self.background = img
        self.time = 0
        self.count = 0
        self.result = 0

    def update(self, delta):
        if self.time == 0:
            self.fighting(self.world.meow_list[self.choose.select].damage, random.randint(10,50))
        self.time+=delta
        if self.time < 15:
            return
        self.time = 0
        self.count = 1
        print("fight count",self.count)

    def fighting(self, meow_damage, enemy_damage):
        stamina = 100
        if stamina / meow_damage < stamina / enemy_damage:
            # win
            self.world.coin.status += 30
            self.result = 1
        elif stamina / meow_damage == stamina / enemy_damage:
            # lose
            self.world.coin.status += 0
            self.result = 0
        else:
            # lose
            self.world.coin.status += 0
            self.result = 0
