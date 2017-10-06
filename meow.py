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

class MEOWWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        # set world bg
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT,"images/background-living.jpg")

        # self.meow_sprite = ModelSprite('images/meow.png', model=self.world.meow)
        self.coin_sprite = ModelSprite('images/coin.png', model=self.world.coin)
        self.food_sprite = ModelSprite('images/Block.png', model=self.world.block_food)

        # add init cat
        

    def update(self, delta):
        self.world.update(delta)
        
    def on_draw(self):
        arcade.start_render()
        # draw bg
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                              SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture(self.world.background)) 
        # draw cat
        self.world.meow_sprite_list.draw()
        # draw block food
        self.food_sprite.draw()
        # draw coin
        self.coin_sprite.draw()
        arcade.draw_text(str(self.world.coin.coin),
                                self.width - 30, self.height - 30,
                                arcade.color.YELLOW, 20)       
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
def main():
    window = MEOWWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()