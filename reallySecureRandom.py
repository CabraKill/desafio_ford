import random

MIN_NUMBER = 0
MAX_NUMBER = 1000

def randomIntNumber(min: int = MIN_NUMBER, max: int = MAX_NUMBER):
    return random.randint(min, max)