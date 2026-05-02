import pygame
from engine.Nodes.Sprite import SpriteNode

class ScrollingBackground(SpriteNode):
    def __init__(self, parent, texture, name="ScrollingBckg" ,x=0, y=0, width=800, height=600, speed=100, screen_size_x=500):
        super().__init__(parent, texture=texture, x=x, y=y, width=width, height=height)
        self.speed = speed
        
        self.screen_size_x = screen_size_x

        self.bg2 = SpriteNode(parent, texture=texture,name="Background 2" ,x=x+width, y=y, width=width, height=height)
        parent.children.insert(0, self.bg2)
    def _update_node(self, node, delta, the_input):
        self.position[0] -= self.speed * delta
        self.bg2.position[0] -= self.speed * delta

        if self.position[0] + self.width <= 0:
            self.position[0] = int(self.bg2.position[0] + self.width) - 3

        if self.bg2.position[0] + self.width <= 0:
            self.bg2.position[0] = int(self.position[0] + self.width) - 3