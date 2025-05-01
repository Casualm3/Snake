import random
from constants import BLOCK_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

def getRandomLocation():
    x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return (x, y)