import pygame
from engine.Nodes.PlayerNode import PlayerNode

class BirdNode(PlayerNode):
    def __init__(self, parent, x, y, scene):
        super().__init__(parent, x=x, y=y)
        self.spawn_timer = .5
        self.gravity = 75
        self.speed = 50
        self.scene = scene
        self.dead = False

    def collided(self, my_rect, other_rect):
        if self.spawn_timer > 0:
            return  # ignorera kollision under spawn
        self.scene.game_over()
        self.dead = True


    def _update_node(self, node, delta, the_input):
        if self.dead: return
        if self.spawn_timer > 0:
            self.spawn_timer -= delta
        # Gravity
        self.position[1] += self.gravity * delta    


        if the_input.key_pressed_once(pygame.K_SPACE):
            self.position[1] -= self.speed