import pygame
import random
import numpy as np
from src.robots.robot import Robot
from src.supervisor.supervisory_ai import SupervisoryAI
from src.metrics.failure_model import FailureModel

WIDTH, HEIGHT = 800, 600

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

robots = []
colors = [(255,0,0),(0,255,0),(0,0,255),(255,128,0),
          (128,0,128),(0,200,200),(255,0,128),(128,128,0)]

for i in range(8):
    robots.append(Robot(
        random.randint(50,750),
        random.randint(50,550),
        colors[i]
    ))

supervisor = SupervisoryAI(robots)
metrics = FailureModel()

running = True
while running:
    clock.tick(60)
    WIN.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for r in robots:
        r.move_towards_target()

    supervisor.monitor_and_reassign(WIDTH, HEIGHT)
    risk = metrics.compute_risk(robots)

    supervisor.draw(WIN, WIDTH, HEIGHT)

    for r in robots:
        r.draw(WIN)

    pygame.display.set_caption(f"System Risk: {risk:.2f}")
    pygame.display.update()

pygame.quit()
