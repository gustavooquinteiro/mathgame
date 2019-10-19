"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame
import os
from constants import *
from levels import *
from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
from character import Character
from projectile import Projectile

class Player(Character):
    """ This class represents the bar at the bottom that the player
    controls. """


    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()
        relpath = os.path.relpath(os.path.join(SPRITE_FOLDER, PLAYER_PNG))
        self.health = 100
        sprite_sheet = SpriteSheet(relpath)

        # -- Attributes
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
        self.invisible = False

        # This holds all the images for the animated walk left/right
        # of our player
        self.walking_frames_l = []
        self.walking_frames_r = []

        # What direction is the player facing?
        self.direction = "R"

        # List of sprites we can bump against
        self.level = None
        self.power = 1
        self.iskill = False
        self.bullets = []

        self.countspace = 0
        self.countrepeatleft = 0
        self.countrepeatright = 0
        self.countrepeatdown = 0

        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(0, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

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
        if self.rect.bottom == SCREEN_HEIGHT and not self.avoidthevoid():
            self.kill()
            self.iskill = True

    def avoidthevoid(self):
        return (isinstance(self.level, Level_08)
                or isinstance(self.level, Level_09)
                or isinstance(self.level, Level_10))

    def shoot(self):
        if (isinstance(self.level, Level_04)
            or isinstance(self.level, Level_05)
            or isinstance(self.level, Level_06)
            or isinstance(self.level, Level_07)
            or isinstance(self.level, Level_08)
            or isinstance(self.level, Level_09)
            or isinstance(self.level, Level_10)):
            if self.direction is "R":
                facing = 1
                shift = 65
            else:
                facing = -1
                shift = -10

            self.bullets.append(
                Projectile(
                    round(self.rect.x + shift),
                    round(self.rect.y + 55),
                    6*self.power,
                    GREEN,
                    facing,
                    self.power))

    def jump(self):
        """ Called when user hits 'jump' button. """
        if (isinstance(self.level, Level_03)
            or isinstance(self.level, Level_04)
            or isinstance(self.level, Level_05)
            or isinstance(self.level, Level_06)
            or isinstance(self.level, Level_07)
            or isinstance(self.level, Level_08)
            or isinstance(self.level, Level_09)
            or isinstance(self.level, Level_10)):
            # move down a bit and see if there is a platform below us.
            # Move down 2 pixels because it doesn't work well if we only move down 1
            # when working with a platform moving down.
            #if isinstance(self.level, levels.Level_02):
            self.rect.y += 2
            platform_hit_list = pygame.sprite.spritecollide(
                self,
                self.level.platform_list,
                False)
            self.rect.y -= 2

            # If it is ok to jump, set our speed upwards
            if (len(platform_hit_list) > 0
                or self.rect.bottom > SCREEN_HEIGHT):
                self.change_y = -10
            self.doublejump()


    def doublejump(self):
        if (isinstance(self.level, Level_05)
            or isinstance(self.level, Level_06)
            or isinstance(self.level, Level_07)
            or isinstance(self.level, Level_08)
            or isinstance(self.level, Level_09)
            or isinstance(self.level, Level_10)):
            self.countspace += 1
            if self.countspace > 1:
                self.change_y = -20
                self.countspace = 0

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.iskill = True

    def increasepower(self):
        if (isinstance(self.level, Level_09)
            or isinstance(self.level, Level_10)):
            self.power += 2
        if (isinstance(self.level, Level_07)
            or isinstance(self.level, Level_08)
            or isinstance(self.level, Level_09)
            or isinstance(self.level, Level_10)):
            self.power += 1

    def sprint(self, direction):
        self.direction = direction
        if self.direction is "L":
            self.change_x = -24
        elif self.direction is "R":
            self.change_x = 24

    def heal(self):
        if isinstance(self.level, Level_10):
            self.health = min(self.health + 10, 100)

    def invisibility(self):
        if (isinstance(self.level, Level_06)
            or isinstance(self.level, Level_07)
            or isinstance(self.level, Level_08)
            or isinstance(self.level, Level_09)
            or isinstance(self.level, Level_10)):
            self.invisible = not self.invisible

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        if self.countrepeatleft <= 1:
            self.change_x = -6
            self.direction = "L"
        if (isinstance(self.level, Level_02)
            or isinstance(self.level, Level_03)
            or isinstance(self.level, Level_04)
            or isinstance(self.level, Level_05)
            or isinstance(self.level, Level_06)
            or isinstance(self.level, Level_07)
            or isinstance(self.level, Level_08)
            or isinstance(self.level, Level_09)
            or isinstance(self.level, Level_10)):
            self.countrepeatleft += 1
            if self.countrepeatleft > 1:
                self.sprint(self.direction)
                self.countrepeatleft = 0

    def go_right(self):
        """ Called when the user hits the right arrow. """
        if self.countrepeatright <= 1:
            self.change_x = 6
            self.direction = "R"
        if (isinstance(self.level, Level_02)
            or isinstance(self.level, Level_03)
            or isinstance(self.level, Level_04)
            or isinstance(self.level, Level_05)
            or isinstance(self.level, Level_06)
            or isinstance(self.level, Level_07)
            or isinstance(self.level, Level_08)
            or isinstance(self.level, Level_09)
            or isinstance(self.level, Level_10)):
            self.countrepeatright += 1
            if self.countrepeatright > 1:
                self.sprint(self.direction)
                self.countrepeatright = 0

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        self.change_y = 0
        self.heal()
