import pygame
from constants import *
import levels
from player import Player
from enemies import Enemy
from projectile import Projectile
import platform
import gettext
if platform.system() is 'Windows':
    import locale
    import ctypes
    windll = ctypes.windll.kernel32
    language = locale.windows_locale[windll.GetUserDefaultUILanguage()]
else:
    language = os.environ.get('LANGUAGE')
try:
    translation = gettext.translation('game', localedir='locale', languages=[language])
except Exception as e:
    # Send the exception for email
    translation = gettext.translation('game', localedir='locale', languages=['pt_BR'])
finally:
    translation.install()


class Game:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat(1, 500)
        size = [SCREEN_WIDTH, SCREEN_HEIGHT]
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.font_name = pygame.font.match_font(FONT)
        self.running = True
        self.isover = False
        self.gameispaused = False


    def new(self, level = 0):
        self.player = Player()
        self.active_sprite_list = pygame.sprite.Group()
        self.level_list = [levels.Level_01(self.player),
                           levels.Level_02(self.player),
                           levels.Level_03(self.player),
                           levels.Level_04(self.player),
                           levels.Level_05(self.player),
                           levels.Level_06(self.player),
                           levels.Level_07(self.player),
                           levels.Level_08(self.player),
                           levels.Level_09(self.player),
                           levels.Level_10(self.player)]
        self.active_sprite_list.add(self.player)
        self.level = level
        self.current_level = self.level_list[self.level]
        self.player.level = self.current_level
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.endgame()


    def update(self):
        if self.player.iskill:
            self.playing = False
            self.isover = True
            self.gameover()
            return

        if not self.gameispaused and self.running:
            self.active_sprite_list.update()
            self.current_level.update()
            # If the player gets near the right side, shift the world left (-x)
            if self.player.rect.right >= 500:
                diff = self.player.rect.right - 500
                self.player.rect.right = 500
                self.current_level.shift_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if self.player.rect.left <= 120:
                diff = 120 - self.player.rect.left
                self.player.rect.left = 120
                self.current_level.shift_world(diff)

            # If the player gets to the end of the level, go to the next level
            current_position = self.player.rect.x + self.current_level.world_shift
            if current_position < self.current_level.level_limit:
                self.player.rect.x = 120
                if self.level < len(self.level_list)-1:
                    self.level += 1
                    self.current_level = self.level_list[self.level]
                    self.player.level = self.current_level
                else:
                   self.endscreen();
        else:
            return


    def events(self):
        for bullet in self.player.bullets:
            for enemies in self.current_level.enemy_list:
                if bullet.y - bullet.radius < enemies.rect.y + 147 and bullet.y + bullet.radius > enemies.rect.y:
                    if bullet.x + bullet.radius > enemies.rect.x and bullet.x - bullet.radius < enemies.rect.x + 52:
                        enemies.loseenergy(self.player.power)
                        if bullet in self.player.bullets:
                            self.player.bullets.pop(self.player.bullets.index(bullet))
            if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                if bullet in self.player.bullets:
                    self.player.bullets.pop(self.player.bullets.index(bullet))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.gameispaused = True
                    self.pausescreen()

                if event.key == pygame.K_LEFT:
                    self.player.go_left()

                if event.key == pygame.K_RIGHT:
                    self.player.go_right()

                if event.key == pygame.K_UP:
                    if self.level < 2:
                        self.draw_text(_('The gravity here is too high to jump'), 24, RED, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                        self.draw_text(_('Press Enter to continue'), 22, RED, SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
                        pygame.display.flip()
                        self.wait_for_key()
                    else:
                        self.player.jump()

                if event.key == pygame.K_SPACE:
                    self.player.increasepower()
                    self.player.shoot()

                if event.key == pygame.K_DOWN:
                    self.player.invisibility()

            if event.type == pygame.KEYUP:
                self.player.stop()
                self.player.heal()



    def draw(self):
        self.screen.fill(BLACK)
        self.current_level.draw(self.screen)
        font = pygame.font.SysFont(FONT, 20, True)

        if not self.player.invisible:
            self.active_sprite_list.draw(self.screen)
            text = font.render(_('Health {}%') .format(self.player.health), 1, RED)
            self.screen.blit(text, (self.player.rect.x -10, self.player.rect.y -20))
            text = font.render(_('Press me'), 1, WHITE)
            self.screen.blit(text, (SCREEN_WIDTH - 200, 10))

        for bullet in self.player.bullets:
            bullet.draw(self.screen)

        self.clock.tick(FPS)

        for enemies in self.current_level.enemy_list:
            enemies.draw(self.screen)
            if enemies.power is not 0:
                text = font.render(_('Level {}').format(enemies.power), 1, WHITE)
                self.screen.blit(text, (enemies.rect.x- 10, enemies.rect.y - 20))

        pygame.display.flip()
        pygame.display.update()


    def show_start_screen(self):
        self.screen.fill(WHITE)
        self.draw_text(_("Math Game"), 48, BLACK, SCREEN_WIDTH /2, SCREEN_HEIGHT / 4)
        self.draw_text(_("Press enter to play"), 32, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text(TIP_LVL, 12, BLACK, SCREEN_WIDTH / 6, SCREEN_HEIGHT-15)
        pygame.display.flip()
        self.wait_for_key()

    def gameover(self):
        self.screen.fill(WHITE)
        self.draw_text("Game Over", 48, BLACK, SCREEN_WIDTH /2, SCREEN_HEIGHT / 4)
        self.draw_text(_("Press q to quit or enter to play again"), 22, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def pausescreen(self):
        self.current_level.tip(self.screen)
        self.draw_text(_("Game Paused"), 22, WHITE, SCREEN_WIDTH /2, SCREEN_HEIGHT/4)
        self.draw_text(_("Press q to quit"), 22, WHITE,SCREEN_WIDTH /2, SCREEN_HEIGHT * 1/2 )
        self.draw_text(_("Press Enter to continue"), 20, WHITE, SCREEN_WIDTH /2, SCREEN_HEIGHT * 2/3 )
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        self.running = False
                        self.playing = False
                        waiting = False
                    if event.key == pygame.K_RETURN:
                        waiting = False
                        if self.gameispaused:
                            self.gameispaused = False
                        if self.isover:
                            self.isover = False
                            self.new()

    def endscreen(self):
        self.screen.fill(WHITE)
        self.isover = True
        self.draw_text(_("You Won!!"), 40, BLACK, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.draw_text(_("Press q to quit or enter to play again"), 22, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def endgame(self):
        if self.isover and not self.running:
            pygame.quit()
