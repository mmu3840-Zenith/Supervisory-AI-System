import random
import math
import pygame

class Robot:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.target = (random.randint(50,750), random.randint(50,550))
        self.energy = 100
        self.failure = 0

    def move_towards_target(self):
        dx = self.target[0] - self.x
        dy = self.target[1] - self.y
        dist = math.hypot(dx, dy)

        if dist > 1:
            self.x += dx / dist * 2
            self.y += dy / dist * 2
        else:
            self.target = (random.randint(50,750), random.randint(50,550))
            self.energy = max(0, self.energy - 10)

        self.failure = 100 - self.energy

    def draw(self, win):
        pygame.draw.circle(win, self.color, (int(self.x), int(self.y)), 20)
        pygame.draw.rect(win, (200,200,200),
            (self.x-20, self.y-30, 40, 5))
        pygame.draw.rect(win, (0,200,0),
            (self.x-20, self.y-30, 40*(self.energy/100), 5))
