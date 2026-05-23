import pygame
import random
import numpy as np
from src.robots.robot import Robot
from src.supervisor.supervisory_ai import SupervisoryAI
from src.metrics.failure_model import FailureModel

WIDTH, HEIGHT = 800, 600

class SimulationEnv:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Supervisory AI System')
        self.clock = pygame.time.Clock()

        self.robots = []
        colors = [(255,0,0),(0,255,0),(0,0,255),(255,128,0),
                  (128,0,128),(0,200,200),(255,0,128),(128,128,0)]

        for i in range(8):
            self.robots.append(
                Robot(
                    random.randint(50,750),
                    random.randint(50,550),
                    colors[i]
                )
            )

        self.supervisor = SupervisoryAI(self.robots)
        self.metrics = FailureModel()
        self.running = True

    def run(self):
        while self.running:
            self.win.fill((255,255,255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            for r in self.robots:
                r.move_towards_target()

            self.supervisor.monitor_and_reassign(800,600)

            risk = self.metrics.compute_risk(self.robots)

            self.supervisor.draw(self.win, 800,600)

            for r in self.robots:
                r.draw(self.win)

            pygame.display.set_caption(f'Risk: {risk:.2f}')
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
