import pygame
from constants import BLOCK_SIZE

class Snake:
    color = (0, 255, 0)  # Snake color (green)
    body = []  # List to store the snake's body segments
    direction = (BLOCK_SIZE, 0)  # Direction of the snake (x, y)
    growing = False  # Flag to indicate if the snake is growing

    def __init__(self, length=5):
        # Initial position of the snake (list of segments)
        self.body =[(5 * BLOCK_SIZE, 5 * BLOCK_SIZE) for _ in range(length)]  

    def move(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w] and self.direction != (0, BLOCK_SIZE):
            self.direction = (0, -BLOCK_SIZE)
        if keys[pygame.K_DOWN] or keys[pygame.K_s] and self.direction != (0, -BLOCK_SIZE):
            self.direction = (0, BLOCK_SIZE)
        if keys[pygame.K_LEFT] or keys[pygame.K_a] and self.direction != (BLOCK_SIZE, 0):
            self.direction = (-BLOCK_SIZE, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] and self.direction != (-BLOCK_SIZE, 0):
            self.direction = (BLOCK_SIZE, 0)
        