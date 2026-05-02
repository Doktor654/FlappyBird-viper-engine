import pygame
from engine.Node import Node

class DeathBox(Node):
    def __init__(self, parent, children=[], x=0, y=0, name="DeathBox",active=True):
        super().__init__(parent, children, name, active)

        
    def collided(self, my_rect ,other_rect):
        pass