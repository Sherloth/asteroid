import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # Create a Clock object
    dt = 0 # Initialize delta time variable

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    counter = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black") # Fill screen black
        
        font_size = SCREEN_HEIGHT // 20
        font = pygame.font.SysFont("arial", font_size)
        text = f"Score: {counter}"
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, font_size // 2 + 5))
        screen.blit(text_surface, text_rect)
        
        updatable.update(dt) # Update updatable group
        for item in drawable:
            item.draw(screen) # Loop for drawing items from drawable group
        pygame.display.flip() # Update the screen
        dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS and calculate delta time
        for object in asteroids:
            if player.collide(object):
                print("Game over!")
                sys.exit()
        for object in asteroids:
            for bullet in shots:
                if object.collide(bullet):
                    object.split()
                    bullet.kill()
                    counter += 1

        


if __name__ == "__main__":
    main()
