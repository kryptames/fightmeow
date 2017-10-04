import arcade
from models import World

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

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
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.meow_sprite = ModelSprite('images/meow.png',
                                                model=self.world.meow) 
        self.meow_sprite.set_position(650,350)
        
    def update(self, delta):
        self.world.update(delta)
        
    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                              SCREEN_WIDTH, SCREEN_HEIGHT, arcade.load_texture(self.world.background)) 
        self.meow_sprite.draw()
        
 
def main():
    window = MEOWWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()