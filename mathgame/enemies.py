import pygame
from spritesheet_functions import SpriteSheet
import random 
from constants import *

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
        self.player = None
        
    def update(self):
        self.destroy()
        self.rect.x += self.vx
        self.vy += self.dy
        if self.rect.left > SCREEN_WIDTH + 100 or self.rect.right < SCREEN_WIDTH:
            self.kill()     
        
    def loseenergy(self, power):
        self.level -= power
        if self.level is 0:
            # mudar o sprite
        if self.level < 0:
            # mudar o sprite
        
    def destroy(self):
        if self.level is not 0 and pygame.sprite.collide_rect(self, self.player):
            self.player.kill()
            
            
        
        
        
        
        
        
