import pygame
from spritesheet_functions import SpriteSheet
import random 
from constants import*
from character import Character

class Enemy(Character):
    def __init__(self, x, y, player, level, initial = -9):
        super().__init__()
        self.level = None
        self.change_x = random.randrange(-5, -1)
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vy = 0        
        self.player = player
        self.change_y = 0
        self.count = 0 
        self.power = random.randint(initial, 9)
        if self.power > 0:
            self.image.fill(BLUE)
        elif self.power == 0:
            self.image.fill(WHITE)
        else:
            self.image.fill(RED)
        
    def update(self):
        self.destroy()
        self.rect.x += self.change_x
        if self.power is 0 and self.rect.right < SCREEN_WIDTH or self.rect.bottom < SCREEN_HEIGHT:
            self.kill()     
    
    def draw(self, screen):
       self.update()
       screen.blit(self.image, (self.rect.x, self.rect.y))
   
    def loseenergy(self, power):
        self.power -= power
        if self.power == 0:
            self.image.fill(WHITE)
            self.change_x = 0
            
        if self.power < 0:
            self.image.fill(RED)    
            self.change_x += random.randrange(-5, -1)
            
        if self.power > 0:
            self.change_x += random.randrange(1, 3)
        
    def destroy(self):
        if self.power is not 0 and pygame.sprite.collide_rect(self, self.player) and self.count == 0:
            self.count += 1
            self.player.hit(abs(self.power) * 10)      

        
        
        
        
