import pygame
from platforms import *
from constants import *
from levels import *

class Character(pygame.sprite.Sprite):

    def __init__(self, level=None):
        super().__init__()
        self.level = level

    def update(self):
        self.calc_grav(self.level.gravity)
        # Move left/right
        self.rect.x += self.change_x
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self,
            self.level.platform_list,
            False)

        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(
            self,
            self.level.platform_list,
            False)

        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

    def calc_grav(self, gravity = .35):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += gravity

        # See if we are on the ground.
        if (self.rect.y >= SCREEN_HEIGHT - self.rect.height
            and self.change_y >= 0):
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
