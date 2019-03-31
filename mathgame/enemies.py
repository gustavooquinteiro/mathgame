import pygame
from spritesheet_functions import SpriteSheet
import random
from constants import*
from character import Character
import os

class Enemy(Character):
    def __init__(self, x, y, player, level, initial = -9):
        super().__init__(level)        
        self.change_x = random.randrange(-5, -1)
        width = 52
        height = 147
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vy = 0
        self.player = player
        self.change_y = 0
        self.count = 0
        self.power = random.randint(initial, 9)
        relpath = os.path.relpath(os.path.join(SPRITE_FOLDER, ENEMIES_PNG))
        self.sprite_sheet = SpriteSheet(relpath)
        if self.power > 0:
            self.image = self.sprite_sheet.get_image(425,0,52,147)
        elif self.power == 0:
            self.image.fill(WHITE)
        else:
            self.image = self.sprite_sheet.get_image(477, 0, 52, 147)

    def update(self):
        self.destroy()
        super().update()

    def draw(self, screen):
       self.update()
       if self.power is not 0:
           screen.blit(self.image, (self.rect.x, self.rect.y))

    def loseenergy(self, power):
        self.power -= power
        if self.power == 0:
            self.image.fill(WHITE)
            self.change_x = 0

        if self.power < 0:
            self.image = self.sprite_sheet.get_image(477, 0, 52, 147)
            self.change_x += random.randrange(-5, -1)

        if self.power > 0:
            self.change_x += random.randrange(1, 3)

    def destroy(self):
        if self.power is not 0 and pygame.sprite.collide_rect(self, self.player) and self.count == 0 and not self.player.invisible:
            self.count += 1
            self.player.hit(abs(self.power) * 10)
