import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    fps_clock = pygame.time.Clock()

    play_surface = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('DTE2602')

    dx = 0
    dy = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                break

        play_surface.fill(pygame.Color(255, 255, 255))

        pygame.draw.rect(play_surface, pygame.Color(0, 0, 255), Rect(0 + dx, 50, 150, 80))
        pygame.draw.rect(play_surface, pygame.Color(0, 255, 0), Rect(100, 0 + dy, 50, 90))

        pygame.display.flip()
        fps_clock.tick(10)

        if dx < 400:
            dx += 10
        else:
            dx = 0

        if dy < 400:
            dy += 5
        else:
            dy = 0
