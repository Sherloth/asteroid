import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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

    def rotate(self, angle):
        self.rotation += angle

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        angle_positive = self.velocity.rotate(angle)
        angle_negative = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = angle_positive * 1.2
        asteroid2.velocity = angle_negative * 1.2
    
