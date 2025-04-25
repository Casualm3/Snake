import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 800

# Colors
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Block size
BLOCK_SIZE = 20

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake and food initialization
snake = [(100, 100)]
snake_dir = (BLOCK_SIZE, 0)
food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
    random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

# Game over function
def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Control snake direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, BLOCK_SIZE):
        snake_dir = (0, -BLOCK_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -BLOCK_SIZE):
        snake_dir = (0, BLOCK_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (BLOCK_SIZE, 0):
        snake_dir = (-BLOCK_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-BLOCK_SIZE, 0):
        snake_dir = (BLOCK_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake = [new_head] + snake[:-1]

    # Check for collisions
    if new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT or new_head in snake[1:]:
        game_over()

    # Check if snake eats the food
    if new_head == food:
        snake.append(snake[-1])  # Grow the snake
        food = (random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)

    # Draw everything
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(10)