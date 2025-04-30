import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock() # Create a Clock object
    dt = 0 # Initialize delta time variable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0, 0, 0)) # Fill screen black initially
        player.update(dt)
        player.draw(screen) # Draw player
        pygame.display.flip() # Update the screen
        dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS and calculate delta time
        
        print(clock.get_fps()) # print fps


if __name__ == "__main__":
    main()
