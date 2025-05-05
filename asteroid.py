import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(100, 60)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (200, 200, 200),
            (int(self.position.x), int(self.position.y)),
             self.radius, 2
             )

    def update(self, dt):
        self.position += self.velocity * dt
        
    
