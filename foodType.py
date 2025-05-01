import pygame
import random
from constants import BLOCK_SIZE
from helperFunctions import getRandomLocation

# Load images for food types
class FoodType:
    def __init__(self, location, image, quality, duration):
        self.location = location
        self.image = image
        self.quality = quality
        self.duration = duration
# Load apple image and scale it to the block size

apple_image = pygame.image.load('./images/apple.jpg')
apple_image = pygame.transform.scale(apple_image, (BLOCK_SIZE, BLOCK_SIZE))
apple = FoodType(getRandomLocation(), apple_image, 1, 5)  # Quality: 1, Duration: 5 seconds
# Load pear image and scale it to the block size
pear_image = pygame.image.load('./images/pear.jpg')
pear_image = pygame.transform.scale(pear_image, (BLOCK_SIZE, BLOCK_SIZE))
pear = FoodType(getRandomLocation, pear_image, 2, 10)  # Quality: 2, Duration: 10 seconds
# List of food images
food = [apple, pear]

# Function to get a random food image
def get_random_food():
    return random.choice(food)
