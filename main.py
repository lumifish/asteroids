import pygame
from constants import *
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    frames = 60
    dt = 0
    game_running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while game_running:
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(frames) / 1000


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()