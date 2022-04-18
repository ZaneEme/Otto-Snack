from random import random
import pygame
import random
from otto_snack.Game import Snake
from otto_snack.Game import COLORS


class Apple:
    def __init__(self, window, width, height, snake, good=True):
        self.snake = snake
        self.x = width // 32 * random.randint(1, 31)
        self.y = height // 32 * random.randint(1, 31)

        while self.snake_collision():
            self.x = width // 32 * random.randint(1, 31)
            self.y = height // 32 * random.randint(1, 31)

        self.good = good
        self.window = window

    def snake_collision(self):
        """
        Checks if the apple is colliding with the snake.
        """
        for segment in self.snake.body:
            if segment.x == self.x and segment.y == self.y:
                return True
        return False

    def draw(self):
        """
        Draws the apple.
        If the apple is good, it is drawn in red.
        If the apple is bad, it is drawn in blue.
        """
        if self.good == True:
            pygame.draw.rect(self.window, COLORS.RED, (self.x, self.y, 25, 25))
        else:
            pygame.draw.circle(self.window, COLORS.BLUE, (self.x, self.y), 10)
