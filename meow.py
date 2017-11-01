import arcade
from models import *

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()

class MeowWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        # set world bg
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT,"images/background-living.jpg")
        self.coin_sprite = ModelSprite('images/coin.png', model=self.world.coin)
        self.block_food_sprite = ModelSprite('images/Block.png', model=self.world.block_food)
        self.food_sprite = ModelSprite('images/food.png', model=self.world.food)

        self.choose = Choose(self.world,"images/choose.png")
        self.fight = Fight(self.world,self.choose,"images/background-working.jpg")
        self.training = Training(self.world, self.choose)
        

    def update(self, delta):
        if self.world.choose_status == False:
            self.world.update(delta)
        else:
            if self.world.fight_status:
                self.fight.update(delta)
                if self.fight.count:
                    self.fight.count = 0
                    self.world.fight_status = False
                    self.world.choose_status = False
        if self.world.training_status:
            self.training.update(delta)

    def on_draw(self):
        arcade.start_render()

        if self.world.choose_status == False and self.world.fight_status == False:

            # draw bg
            arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                                SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture(self.world.background)) 
            # draw cat
            self.world.meow_sprite_list.draw()
            # draw block food
            self.block_food_sprite.draw()
            self.food_sprite.draw()
            # draw coin
            self.coin_sprite.draw()
            arcade.draw_text(str(self.world.coin.status),
                                    self.width - 40, self.height - 30,
                                    arcade.color.CITRINE, 20)    
            for i in range(0,len(self.world.meow_list)):
                arcade.draw_text('Lv:{0}  Dmg:{1}'.format(str(self.world.meow_list[i].level),str(self.world.meow_list[i].damage)),
                                        self.world.meow_sprite_list[i].center_x - 60, self.world.meow_sprite_list[i].center_y + 50,
                                        arcade.color.BLUE_YONDER, 20)
            #  draw food 
            self.food_sprite.draw()
            arcade.draw_text('Left: {0}'.format(str(self.world.food.status)),
                                        self.food_sprite.center_x - 50, self.food_sprite.center_y + 50,
                                        arcade.color.BRICK_RED, 20)

            # draw botton
            arcade.draw_texture_rectangle(80, 30, 150, 53,
                                                    arcade.load_texture("images/train button.png"))
            if self.world.training_status:
                arcade.draw_texture_rectangle(80, 30, 150, 53,
                                                    arcade.load_texture("images/train button-off.png"))
            arcade.draw_texture_rectangle(620, 30, 150, 53,
                                                    arcade.load_texture("images/fight button.png"))

        elif self.world.choose_status:
            if self.world.choose_press:
                arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                        SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture(self.choose.background))
                arcade.draw_texture_rectangle(580, 50, 150, 53,
                                                    arcade.load_texture("images/choose botton.png"))
                if self.choose.chose_sprite.center_x != 100 and self.choose.chose_sprite.center_y != 100:
                    self.choose.chose_sprite.draw()
                    arcade.draw_texture_rectangle(580, 50, 150, 53,
                                                    arcade.load_texture("images/chose button.png"))

                for i in range(len(self.world.pic)):
                    arcade.draw_texture_rectangle(self.world.choose_position[i][0], self.world.choose_position[i][1], 100, 88,
                                                    arcade.load_texture("images/choose_meow{0}.png".format(self.world.pic[i])))

                
            elif self.world.fight_status:
                arcade.set_background_color(arcade.color.BLACK)
                if self.fight.time < 4:
                    arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200, 261, 75.5,
                                                    arcade.load_texture("images/enemy_banner.png"))
                    arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 112.5, 126,
                                                    arcade.load_texture("images/enemy.png"))
                elif self.fight.time > 4 and self.fight.time < 12:
                    arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 260, 30,
                                                    arcade.load_texture("images/loading{0}.png".format(int(self.fight.time) % 4)))
                else:
                    if self.fight.result:
                        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 700, 700,
                                                    arcade.load_texture("images/win.png"))
                    else:
                        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 700, 700,
                                                    arcade.load_texture("images/lose.png"))

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        if not self.world.choose_status and not self.world.fight_status:
            self.world.on_mouse_press(x, y, button, modifiers)
        # center block is 650,30
        else:
            self.choose.on_mouse_press(x, y, button, modifiers)
        

def main():
    window = MeowWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()