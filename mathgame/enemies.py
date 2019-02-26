import pygame
from spritesheet_functions import SpriteSheet
import random 
from constants import*
from character import Character

class Enemy(Character):
    def __init__(self, x, y, player):
        super().__init__()
        self.level = None
        self.change_x = random.randrange(-4, -1)
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        self.rect.x = x
        self.rect.y = y
        self.vy = 0
        self.dy = 0.5
        self.player = player
        self.power = random.randint(1, 9)
        
    def update(self):
        self.destroy()
        self.rect.x += self.change_x
        if self.rect.left > SCREEN_WIDTH + 100 or self.rect.right < SCREEN_WIDTH:
            self.kill()     
        
    def loseenergy(self, power):
        self.power -= power
        if self.level is 0:
            self.image.fill(WHITE)
            self.change_x = 0
        if self.level < 0:
            self.image.fill(RED)
            self.change_x = random.randrange(1, 4)
        
    def destroy(self):
        if self.level is not 0 and pygame.sprite.collide_rect(self, self.player):
            self.player.kill()
            
    def move(self):
        distance = 80
        speed = 8

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1
            
        
        
        
        
        
        
