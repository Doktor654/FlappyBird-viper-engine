from engine.Nodes.TransformNode import TransformNode

class PipeNode(TransformNode):
    def __init__(self, parent, scene,children=[], name="PlayerNode", x=0, y=0, active=True, is_spawner=False):
        super().__init__(parent, children or [], name, active)
        self.position[0] = x
        self.position[1] = y
        self.scene = scene

        self.spawned_new_pipes = False
        self.is_spawner = is_spawner
        self.game_over = False
    def collided(self, my_rect, other_rect):
       # self.game_over = True
       pass
    
    def _update_node(self, node, delta, the_input):
        if self.game_over : return
        self.position[0] -= 100 * delta
        if self.position[0] <= 300 and self.is_spawner:
            if not self.spawned_new_pipes:
                print("SPawn")
                self.scene.time_to_create()
                self.spawned_new_pipes = True
                self.scene.score += 1
        
        if self.position[0] <= -100:
            self.remove_from_scene(self.scene.collision_system)