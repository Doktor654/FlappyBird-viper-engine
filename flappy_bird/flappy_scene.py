import pygame
from engine.Scene import Scene
from flappy_bird.flappy_nodes.BirdNode import BirdNode
from flappy_bird.flappy_nodes.ScrollingBackground import ScrollingBackground
from flappy_bird.flappy_nodes.PipeNode import PipeNode
from engine.Nodes.CollisionBody import CollisionBody
from engine.Nodes.Sprite import SpriteNode
from engine.Nodes.Camera import CameraNode
from engine.Nodes.Label import LabelNode
from engine.Nodes.Button import ButtonNode
import random

class FlappyScene(Scene):
    def Initialize(self, collision_system):
        self.collision_system = collision_system
        super().Initialize(collision_system)

        self.is_dead : bool = False
        self.showing : bool = False
        self.score = 0
        self.pipes = []
        ## Background
        self.background = ScrollingBackground(self.root, texture="flappy_bird/assets/bg.png",name="Background" ,x=0, y=0, width=900, height=504, screen_size_x=600)
        self.root.children.insert(0, self.background)
        
        ## Bird
        self.bird = BirdNode(self.root, x=300, y=250, scene=self)
        self.root.children.append(self.bird)

        self.bird_sprite = SpriteNode(self.bird,texture="flappy_bird/assets/bird.png",name="BirdSprite", x=0, y=0, width=50, height=50)
        self.bird.children.append(self.bird_sprite)

        self.bird_collision = CollisionBody(self.bird, color=(111,11,111,0),width=50, height=50, static=False)
        self.bird.children.append(self.bird_collision)
        collision_system.add_to_bodies(self.bird_collision)


        ## Top detection
        self.top_death_collision = CollisionBody(self.root, color=(155, 0,0, 0),width=600, height=10, static=True)
        self.root.children.append(self.top_death_collision)
        collision_system.add_to_bodies(self.top_death_collision)
      
        ## Bot Detection

        self.bot_death_collision = CollisionBody(self.root, color=(1, 155,0, 0),y=490,width=600, height=10, static=True)
        self.root.children.append(self.bot_death_collision)
        collision_system.add_to_bodies(self.bot_death_collision)

        # Create pipes

        self.create_pipes(collision_system)

        self.camera.set_position(x=300, y=250)
        #self.camera.follow(self.bird)
        
        self.Pointslabel = LabelNode(self.root, text="SCORE : 0",x=250, y=0, font_size=32)
        self.root.children.append(self.Pointslabel)
        
        self.root.debug_print_tree()

    ## Game Over
    def game_over(self):
        if not self.is_dead:
            
            self.game_over_label = LabelNode(self.root, text="GAME OVER", x=200, y=200, font_size=32)
            self.root.children.append(self.game_over_label)

            self.TestButton = ButtonNode(self.root, text="RESTART", color=(30,50,0),x=200, y=250, width=200, height=100, font_size=20)
            self.root.children.append(self.TestButton)
            self.TestButton.on_click.connect(self.restart)
            for pipe in self.pipes:
                pipe.game_over = True
            self.is_dead = True
    def restart(self):
        self.root.children.clear()
        self.collision_system.collision_bodies.clear()
        
        self.score = 0
        self.Initialize(self.collision_system)
        self.is_dead = False

    # Update
    def update(self, delta, input):

            #return
        if not self.is_dead:
            self.Pointslabel.text = "Score : %s" % self.score
        self._update_node(self.root, delta, self.input)

    ## Creating Pipes
    

    def time_to_create(self):
        self.create_pipes(self.collision_system)

    def get_random_value(self):
        return random.randint(100, 400)

    def create_pipe_sizes(self):
        right_sizes : bool = False

        while right_sizes == False:
            self.random_y_top_value = self.get_random_value()
            self.random_y_bot_value = self.get_random_value()

            if (self.random_y_top_value + self.random_y_bot_value) < 410:
                print("Too small hole, retry")
                return True
                
    
    def create_pipes(self, collision_system):
        if self.create_pipe_sizes():
            print("sizes : ", self.random_y_bot_value, self.random_y_top_value)
            # Pipe Above
            self.pipe1 = PipeNode(self.root, name="Pipe 1",scene=self,x= 600, y=0,  is_spawner=True)
            self.root.children.append(self.pipe1)

            self.pipe_sprite = SpriteNode(self.pipe1,texture="flappy_bird/assets/pipe.png",name="PipeSprite", x=0, y=0, width=100, height=self.random_y_top_value, flip_y=True)
            self.pipe1.children.append(self.pipe_sprite)

            self.pipe1Coll = CollisionBody(self.pipe1, color = (155, 0, 0, 0),width = 100, height=self.random_y_top_value, static=True)
            self.pipe1.children.append(self.pipe1Coll)
            collision_system.add_to_bodies(self.pipe1Coll)

            self.pipes.append(self.pipe1)

            # Pipe Below
            self.pipe2 = PipeNode(self.root, name="Pipe 2",scene=self, x= 600, y= 500 - self.random_y_bot_value,  is_spawner=False)
            self.root.children.append(self.pipe2)

            self.pipe_sprite2 = SpriteNode(self.pipe2,texture="flappy_bird/assets/pipe.png",name="PipeSprite", x=0, y=0, width=100, height=self.random_y_bot_value)
            self.pipe2.children.append(self.pipe_sprite2)

            self.pipe2Coll = CollisionBody(self.pipe2, color = (155, 0, 0, 0), width = 100, height=self.random_y_bot_value, static=True)
            self.pipe2.children.append(self.pipe2Coll)
            collision_system.add_to_bodies(self.pipe2Coll)
            self.pipes.append(self.pipe2)
            # Create pass area to show score later
           # self.passArea = CollisionBody(self.root, color=(0, 50, 155, 100),x=self.pipe1.position[0] ,width=30, height= 600 - (self.random_y_bot_value + self.random_y_top_value), static = False)
           # self.root.children.append(self.passArea)
            #collision_system.add_to_bodies(self.passArea)