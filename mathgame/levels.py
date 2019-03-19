import pygame
from constants import *
import platforms
from enemies import Enemy
import random

# parent class
class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -1000
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = []
        self.player = player
        self.level = [[]]

    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(BLUE)
        screen.blit(self.background,(self.world_shift // 3,0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x



    def spawn(self, interval = 5):
        if isinstance(self, Level_08) or isinstance(self, Level_09) or isinstance(self, Level_10):
            for i in range(interval):
                self.enemy_list.append(Enemy(SCREEN_WIDTH, random.randrange(50,SCREEN_HEIGHT), self.player, self,random.randrange(-9, 1)))
        else:
            for i in range(interval):
                self.enemy_list.append(Enemy(SCREEN_WIDTH, random.randrange(round(SCREEN_HEIGHT - SCREEN_HEIGHT / 4, SCREEN_HEIGHT)), self.player, self,random.randrange(-9, 1)))


# level 1 = just walk around
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_01).convert()
        self.background.set_colorkey(WHITE)
        self.level_limit = -1500

        # Array with type of platform, and x, y location of the platform.
        self.level = [ [platforms.GRASS_LEFT, 0, 500]]
        for i in range(1, SCREEN_WIDTH - 600):
            self.level.append([platforms.GRASS_MIDDLE, 70*i, 500])
        self.level.append([platforms.GRASS_RIGHT, 70*i, 500])


        # Go through the array above and add platforms
        for platform in self.level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
    """
        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 2500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        #self.spawn()
    """
    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL1, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))


# level 2 - sprint
class Level_02(Level_01):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_02).convert()
        self.background.set_colorkey(WHITE)
        self.level_limit = -1500

        # Array with type of platform, and x, y location of the platform.
        self.level = [ [platforms.GRASS_LEFT, 0, 500]]
        for i in range(1,20):
            self.level.append([platforms.GRASS_MIDDLE, 20+70*i, 500])
        self.level.append([platforms.GRASS_RIGHT, 1400, 500])
        self.level.append([platforms.GRASS_MIDDLE, 1600, 500])

        # Go through the array above and add platforms
        for platform in self.level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1600
        block.rect.y = 500
        block.boundary_left = 1500
        block.boundary_right = 2500
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        #self.spawn()

    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL2, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))

#level 3 - jump
class Level_03(Level_02):
    def __init__(self, player):
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_03).convert()
        self.background.set_colorkey(WHITE)
        self.level_limit = -1000

        self.level = [ [platforms.GRASS_LEFT, 0, 500]]
        for i in range(1, 5):
            self.level.append([platforms.GRASS_MIDDLE, 70*i, 500])
        self.level.append([platforms.GRASS_RIGHT, 350, 500])
        for i in range(1, 10):
            self.level.append([platforms.GRASS_MIDDLE, 350+70*i, 500-50*i])

        for i in range(1, 10):
            self.level.append([platforms.GRASS_MIDDLE, 1500+70*i, 500-50*i])

        for platform in self.level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        for i in range(1,3):
            block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
            block.rect.x = 1100 + 100*i
            block.rect.y = 300 + 100*i
            block.boundary_top = 100 + 70*i
            block.boundary_bottom = 500 + 70*i
            block.change_y = -1
            block.player = self.player
            block.level = self
            self.platform_list.add(block)

    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL3, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))

#level 4 - shoot
class Level_04(Level_03):
    def __init__(self, player):
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_04).convert()
        self.level = [ [platforms.GRASS_LEFT, 0, 500]]
        for i in range(1, 50):
            self.level.append([platforms.GRASS_MIDDLE, 70*i, 500])
        self.level.append([platforms.GRASS_RIGHT, 70*i, 500])

        self.level.append([platforms.GRASS_MIDDLE, 100, 200])
        for i in range(1, 3):
            self.level.append([platforms.GRASS_MIDDLE, 100+70*i, 200-50*i])

        for platform in self.level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        self.spawn()


    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL4, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))

#level 5 - double jump
class Level_05(Level_04):
    def __init__(self, player):
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_05).convert()

        self.level = [ [platforms.GRASS_LEFT, 0, 500]]
        for i in range(1, 20):
            self.level.append([platforms.GRASS_MIDDLE, 70*i, 500])
        self.level.append([platforms.GRASS_RIGHT, 70*i, 500])

        for i in range(1, 5):
            self.level.append([platforms.STONE_PLATFORM_MIDDLE, 240+70*i, 580-100*i])

        for platform in self.level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1000
        block.rect.y = 60
        block.boundary_top = 290
        block.boundary_bottom = 500
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        self.spawn()

    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL5, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))

#level 6 - invisibility
class Level_06(Level_05):
    def __init__(self, player):
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_06).convert()

        self.level = [ [platforms.GRASS_LEFT, 0, 500]]
        for i in range(1, 30):
            self.level.append([platforms.GRASS_MIDDLE, 70*i, 500])
        self.level.append([platforms.GRASS_RIGHT, 70*i, 500])

        for platform in self.level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        self.spawn(10)

    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL6, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))


#level 7 - increase power
class Level_07(Level_06):
    def __init__(self, player):
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_07).convert()

        self.level = [ [platforms.GRASS_LEFT, 0, 500]]
        for i in range(1, 30):
            self.level.append([platforms.GRASS_MIDDLE, 70*i, 500])
        self.level.append([platforms.GRASS_RIGHT, 70*i, 500])

        for platform in self.level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        self.spawn()

    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL7, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))


#level 8 - dont fall
class Level_08(Level_07):
    def __init__(self, player):
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_08).convert()
        for i in range(1, 30):
            self.level.append([platforms.STONE_PLATFORM_MIDDLE, random.randrange(i, 1700), random.randrange(i, 1000)])
        self.spawn(10)

    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL8, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))


#level 9 - twice power
class Level_09(Level_08):
    def __init__(self, player):
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_09).convert()
        self.spawn(10)

    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL9, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))

#level 10 - heal
class Level_10(Level_09):
    def __init__(self, player):
        super().__init__(player)
        self.createLevel()

    def createLevel(self):
        self.background = pygame.image.load(BACKGROUND_10).convert()
        self.spawn(15)

    def tip(self, screen):
        font = pygame.font.SysFont(FONT, 20)
        text = font.render(TIP_LVL10, 1, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 780, 10))
