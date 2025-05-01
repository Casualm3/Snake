import pygame
import random
from constants import BLOCK_SIZE
# Load images for food types

# Load apple image and scale it to the block size
apple_image = pygame.image.load('./images/apple.jpg')
apple_image = pygame.transform.scale(apple_image, (BLOCK_SIZE, BLOCK_SIZE))
# Load pear image and scale it to the block size
pear_image = pygame.image.load('./images/pear.jpg')
pear_image = pygame.transform.scale(pear_image, (BLOCK_SIZE, BLOCK_SIZE))

# List of food images
food_images = [apple_image, pear_image]

# Function to get a random food image
def get_random_food_image():
    return random.choice(food_images)
