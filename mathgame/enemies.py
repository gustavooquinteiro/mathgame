import pygame
import constants
from spritesheets_functions import SpriteSheet
import random 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.level = random.randint(1, 9)
        self.vx = random.randrange(1, 4)
        self.image = 
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange()
        self.vy = 0
        self.dy = 0.5
        
        
    def update(self):
        self.rect.x += self.vx
        self.vy += self.dy
        
        
    def loseenergy(self, power):
        self.level -= power
        if self.level == 0:
            # mudar o sprite
        if self.level < 0:
            # mudar o sprite
        
    def destroy(self):
        if self.level is not 0:
            # code to death of player
            
        
        
        
        
        
        
