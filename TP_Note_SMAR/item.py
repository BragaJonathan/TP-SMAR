import random

from pygame.math import Vector2


class Item:

    def __init__(self, type):
        self.position = Vector2(random.randint(0,800), random.randint(0,600))
        self.type = type