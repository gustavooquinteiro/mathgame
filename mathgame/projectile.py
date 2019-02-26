import pygame
import platforms

class Projectile(pygame.sprite.Sprite):
    def __init__(self, damage=1, speed =0.2, direction=[10,20], position=2):
        super().__init__()
        self.damage = damage
        self.speed = speed
        self.direction = direction 
        multiplier = speed / float((direction[0]**2 + direction[1]**2) ** 0.5)
        self.movement = [int(multiplier * direction[0]), int(multiplier * direction[1])]
        self.initimage()
        self.rect = pygame.Rect(position, self.image.get_size())
        
        
    def update(self):
        self.rect = self.rect.move(self.movement)
        
        
    def collidewith(self, enemy):
        enemy.loseenergy(self.damage)
        
        
        
        

