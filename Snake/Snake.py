from tkinter import W
import pygame
import Snake.Colors as Colors

class Snake:
    def __init__(self, window, width, height, length=3):
        self.length = length
        self.x = width // 2
        self.y = height // 2
        self.body = []
        self.window = window
        self.direction = 1
        self.green = Colors.Green

        for i in range(1, length + 1):
            self.body.append(SnakeSegment(window, self.x + (25 * i), self.y))

    def move(self):
        """
        Moves the entire snake one space
        """
        if self.direction == 0:
            self.body[0].y -= 25
        elif self.direction == 1:
            self.body[0].x += 25
        elif self.direction == 2:
            self.body[0].y += 25
        elif self.direction == 3:
            self.body[0].x -= 25

        self.body.pop(-1)

    def eat(self):
        """
        Adds a new segment to the snake.
        """
        self.body.insert(0, SnakeSegment(self.window, (self.body[0].x), self.body[0].y))

    def turn(self, direction=0):
        """
        Sets the direction of the snake.
        """
        self.direction = direction

    def draw(self):
        """
        Draws the snake to the screen.
        """
        for segment in self.body:
            segment.draw()


class SnakeSegment:
    def __init__(self, window, x, y):
        self.x = x
        self.y = y
        self.window = window

    def draw(self):
        """
        Draws the snake segment to the screen.
        """
        # pygame.draw.rect(self.window, COLORS.Green, (400, 400, 100, 100))
        pygame.draw.rect(self.window, Colors.Green, pygame.Rect(self.x, self.y, 25, 25))
