
import math
import pygame
from pygame.locals import *

import graph_tools as gt
import graph_search_solution as gs

# Add colors as needed
RED_COLOR = pygame.Color(255, 0, 0)
GREEN_COLOR = pygame.Color(0, 255, 0)
BLUE_COLOR = pygame.Color(0, 0, 255)
L_BLUE_COLOR = pygame.Color(0, 255, 255)
BLACK_COLOR = pygame.Color(0, 0, 0)
WHITE_COLOR = pygame.Color(255, 255, 255)
PURPLE_COLOR = pygame.Color(128, 0, 128)

W_WIDTH = 650
W_HEIGHT= 650
B_OFFSET = 10 # Border offset
S_OFFSET = 25 # Squares offset
S_SIZE = 60 # Squares size

def draw_box(surface : pygame.Surface, x_corner : int, y_corner : int, size : int, color : pygame.Color):
    ''' Helper function to draw a rectangular box of the specified color and size'''
    pygame.draw.rect(surface, BLACK_COLOR, Rect(x_corner - 1, y_corner - 1, size + 2, size + 2)) # A black outline
    pygame.draw.rect(surface, color, Rect(x_corner, y_corner, size, size))

if __name__ == "__main__":
    pygame.init()
    fps_clock = pygame.time.Clock()

    play_surface = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
    pygame.display.set_caption('Breadth-first visualization')
    simulator_speed = 5

    maze_text = gt.read_maze_text("maze_10x10.txt")
    graph = gt.maze_text_to_graph(maze_text)
    maze = gt.maze_text_to_matrix(maze_text)

    explored_squares = []

    start_node = (1, 1)
    end_node = (7, 6)

    came_from, path = gs.breadth_first_search(graph, start_node, end_node)

    maze_iter = came_from.__iter__()
    node = maze_iter.__next__()

    # Pygame boilerplate code
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                break
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                    running = False
                    break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                print("x_min=" + str(math.floor(pos[0])))

        play_surface.fill(WHITE_COLOR) # Fill the screen with white
        pygame.draw.polygon(play_surface, BLACK_COLOR, [(B_OFFSET, B_OFFSET), (W_WIDTH - B_OFFSET, B_OFFSET),
                                                        (W_HEIGHT - B_OFFSET, W_HEIGHT - B_OFFSET), (B_OFFSET, W_HEIGHT - B_OFFSET)], 3)

        # Render the squares
        for x in range(10):
            for y in range(10):
                if maze[x][y] == 1:
                    draw_box(play_surface, x * S_SIZE + S_OFFSET, y * S_SIZE + S_OFFSET, S_SIZE, WHITE_COLOR)
                else:
                    draw_box(play_surface, x * S_SIZE + S_OFFSET, y * S_SIZE + S_OFFSET, S_SIZE, BLACK_COLOR)

                if x == start_node[0] and y == start_node[1]:
                    draw_box(play_surface, x * S_SIZE + S_OFFSET, y * S_SIZE + S_OFFSET, S_SIZE, RED_COLOR)
                if x == end_node[0] and y == end_node[1]:
                    draw_box(play_surface, x * S_SIZE + S_OFFSET, y * S_SIZE + S_OFFSET, S_SIZE, GREEN_COLOR)
                if x == node[0] and y == node[1]:
                    draw_box(play_surface, x * S_SIZE + S_OFFSET, y * S_SIZE + S_OFFSET, S_SIZE, BLUE_COLOR)


        # Refresh the screen
        pygame.display.flip()
        fps_clock.tick(simulator_speed)

        # Update tickers
        if maze_iter.__length_hint__() > 0:
            node = maze_iter.__next__()
        else:
            maze_iter = came_from.__iter__()