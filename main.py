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
        updatable.update(dt) # Update updatable group
        for item in drawable:
            item.draw(screen) # Loop for drawing items from drawable group
        pygame.display.flip() # Update the screen
        dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS and calculate delta time
        for object in asteroids:
            if player.collide(object):
                print("Game over!")
                sys.exit()

        


if __name__ == "__main__":
    main()
