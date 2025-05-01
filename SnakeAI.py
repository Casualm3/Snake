import pygame
import sys
import snake as s
import constants as c
import foodType as f
from helperFunctions import getRandomLocation
# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = c.SCREEN_WIDTH
SCREEN_HEIGHT = c.SCREEN_HEIGHT
BLOCK_SIZE = c.BLOCK_SIZE
# Colors
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake and food initialization
snake = s.Snake() # Create a snake with a length of 20 blocks
snack = f.get_random_food()  # Get a random food item

# Game over function
def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, FOOD_COLOR)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Function to draw the snake and food    
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Control snake direction
    keys = pygame.key.get_pressed()
    snake.move(keys)

    # Move the snake
    new_head = (snake.body[0][0] + snake.direction[0], snake.body[0][1] + snake.direction[1])
    snake.body = [new_head] + snake.body[:-1]

    # Check for collisions
    if new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] >= SCREEN_HEIGHT or new_head in snake.body[1:]:
        game_over()

    # Check if snake eats the food
    if new_head == snack.location:
        snake.body.append(snake.body[-1])  # Grow the snake
        snack = f.get_random_food()  # Get a new food item
        snack.location = getRandomLocation()  # Generate new food position

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    # Draw gridlines
    for x in range(0, SCREEN_WIDTH, 20):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, 20):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (SCREEN_WIDTH, y))
    for segment in snake.body:
            pygame.draw.rect(screen, snake.color, pygame.Rect(segment[0], segment[1], c.BLOCK_SIZE, c.BLOCK_SIZE))    
    # Move the food to the left
    if pygame.time.get_ticks() // 100 % 10 == 0:  # Run every 10th iteration (approx. every second at 10 FPS)
        foodLocation = snack.location
        foodLocation = (foodLocation[0] - BLOCK_SIZE, foodLocation[1]) if foodLocation[0] > 0 else getRandomLocation()
        snack.location = foodLocation
    # Draw the food
    screen.blit(snack.image, snack.location)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(10)