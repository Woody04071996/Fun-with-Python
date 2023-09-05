import math, random
from livewires import games, color

games.init(screen_width = 1100, screen_height = 800, fps = 50)


class Warrior(games.Sprite):
    """postac"""

    image = games.load_image("postac1.png")


    def move(self):
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Warrior.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Warrior.ROTATION_STEP
    
    









        
