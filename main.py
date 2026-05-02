import sys, pygame
## Import all the different parts
#sys.path.append(os.path.join(os.path.dirname(__file__), 'MyEngine'))
from engine.game_loop import GameLoop
from engine.Scene import Scene
from Renderer.renderer import Renderer
from engine.input import Input
from engine.CollisionSystem import CollisionSystem
from flappy_bird.flappy_scene import FlappyScene


## Initialize the scene, renderer and game_loop
## and then run the gameloop from there
the_input = Input()
the_scene = FlappyScene(the_input)
the_collision_system = CollisionSystem()


the_renderer = Renderer(the_scene, (600, 500))
the_game_loop = GameLoop(the_scene, the_collision_system ,the_renderer, the_input, fps=144)


the_game_loop.run(the_scene)


