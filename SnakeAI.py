import pygame
import sys
import random
import snake as s
import constants as c

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = c.SCREEN_WIDTH
HEIGHT = c.SCREEN_HEIGHT
BLOCK_SIZE = c.BLOCK_SIZE
# Colors
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
#WHITE = (255, 255, 255)
def getRandomLocation():
    x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    print(f"Random location generated: ({x}, {y})")
    return (x, y)
# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake and food initialization
snake = s.Snake(20) # Create a snake with a length of 20 blocks
food = getRandomLocation()  # Random food position
# Game over function
def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, FOOD_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Load apple image and scale it to the block size
apple_image = pygame.image.load('./images/apple.jpg')
apple_image = pygame.transform.scale(apple_image, (BLOCK_SIZE, BLOCK_SIZE))
# Load pear image and scale it to the block size
pear_image = pygame.image.load('./images/pear.jpg')
pear_image = pygame.transform.scale(pear_image, (BLOCK_SIZE, BLOCK_SIZE))
FoodType = random.choice([apple_image, pear_image])
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
    if new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= WIDTH or new_head[1] >= HEIGHT or new_head in snake.body[1:]:
        game_over()

    # Check if snake eats the food
    if new_head == food:
        snake.body.append(snake.body[-1])  # Grow the snake
        food = getRandomLocation()  # Generate new food position
        FoodType = apple_image if FoodType == pear_image else pear_image

    # Draw everything
    screen.fill(BACKGROUND_COLOR)
    # Draw gridlines
    for x in range(0, WIDTH, 20):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 20):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))
    for segment in snake.body:
            pygame.draw.rect(screen, snake.color, pygame.Rect(segment[0], segment[1], c.BLOCK_SIZE, c.BLOCK_SIZE))    
   
    screen.blit(FoodType, (food[0], food[1]))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(10)