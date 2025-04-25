import constants as c
import pygame

class Snake:
    color = (0, 255, 0)  # Snake color (green)
    body = []  # List to store the snake's body segments
    direction = (c.BLOCK_SIZE, 0)  # Direction of the snake (x, y)
    growing = False  # Flag to indicate if the snake is growing

    def __init__(self):
        pass
        # Initial position of the snake (list of segments)
        #self.body = [(5, 5)]  # Starting segments
        #self.direction = (c.BLOCK_SIZE, 0) # Initial direction
        #self.growing = False  # Flag to indicate if the snake is growing

    def move(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w] and self.direction != (0, c.BLOCK_SIZE):
            self.direction = (0, -c.BLOCK_SIZE)
        if keys[pygame.K_DOWN] or keys[pygame.K_s] and self.direction != (0, -c.BLOCK_SIZE):
            self.direction = (0, c.BLOCK_SIZE)
        if keys[pygame.K_LEFT] or keys[pygame.K_a] and self.direction != (c.BLOCK_SIZE, 0):
            self.direction = (-c.BLOCK_SIZE, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and self.direction != (-c.BLOCK_SIZE, 0):
            self.direction = (c.BLOCK_SIZE, 0)
        