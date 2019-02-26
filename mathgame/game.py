import pygame
 
from constants import *
import levels
 
from player import Player
from enemies import Enemy

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
        self.countspace = 0
        self.countrepeatleft = 0
        self.countrepeatright = 0
        
    def new(self):
        self.level_list = []
        self.player = Player()
        self.active_sprite_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.level_list.append(levels.Level_01(self.player))
        self.level_list.append(levels.Level_02(self.player))
        self.level_list.append(levels.Level_03(self.player))
        self.level = 0
        self.current_level = self.level_list[self.level]
        self.player.level = self.current_level
        self.active_sprite_list.add(self.player)
        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
            
    
    def update(self):
        if self.player.iskill:
            self.playing = False
            self.gameover()
            return
            
        
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

        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    self.countrepeatleft += 1
                    if self.countrepeatleft > 1:
                        print("sprint l")
                        self.player.sprint("L")
                        self.countrepeatleft = 0
                        self.countrepeatright = 0
                    else:
                        self.player.go_left()
                        
                if event.key == pygame.K_RIGHT:
                    self.countrepeatright += 1
                    if self.countrepeatright > 1:
                        print("sprint r")
                        self.player.sprint("R")
                        self.countrepeatright = 0
                        self.countrepeatleft = 0
                    else:
                        self.player.go_right()
                        
                if event.key == pygame.K_UP:
                    self.countspace += 1;
                    if self.countspace > 1:
                        print("doublejump")
                        self.player.doublejump()
                        self.countspace = 0
                    self.player.jump()
                    
                if event.key == pygame.K_SPACE:                    
                    self.player.increasepower()
                    print("increasing power..")
                    
                if event.key == pygame.K_DOWN:
                    self.player.stop()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.countrepeatright = 0
                    self.player.stop()
                if event.key == pygame.K_LEFT:
                    self.countrepeatleft = 0
                    self.player.stop()

                
    def draw(self):
        self.screen.fill(BLACK)
        self.current_level.draw(self.screen)
        self.active_sprite_list.draw(self.screen)
        self.enemy_list.draw(self.screen)
        for e in self.enemy_list:
            e.move()
        self.clock.tick(FPS)
        pygame.display.flip()

        
    def show_start_screen(self):
        self.screen.fill(WHITE)
        self.draw_text("Math Game", 48, BLACK, SCREEN_WIDTH /2, SCREEN_HEIGHT / 4)
        self.draw_text("Arrows to move, space to shoot", 22, BLACK, SCREEN_WIDTH /2 , SCREEN_HEIGHT/2)
        self.draw_text("Press a key to play", 22, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()
        
    def gameover(self):
        self.screen.fill(WHITE)
        self.draw_text("Game Over", 48, BLACK, SCREEN_WIDTH /2, SCREEN_HEIGHT / 4)
        self.draw_text("Press q to quit or any other key to play again", 22, BLACK, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)

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
                    if event.key == ord('q'):
                        self.running = False
                    waiting = False
                    
    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
