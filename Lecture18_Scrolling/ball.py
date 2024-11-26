from pico2d import *
import game_world
import game_framework
import random

import server


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        sx, sy =  self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)
        bb = self.get_bb()
        draw_rectangle(bb[0] - server.background.window_left, bb[1] - server.background.window_bottom
                       , bb[2] - server.background.window_left, bb[3] - server.background.window_bottom)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        game_world.remove_object(self)
        pass
