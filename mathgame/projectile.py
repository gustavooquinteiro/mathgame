import pygame
import platforms

class Projectile(object):
    def __init__(self, x, y, radius, color, facing, damage):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
        self.damage = damage
        
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
        
        
        

