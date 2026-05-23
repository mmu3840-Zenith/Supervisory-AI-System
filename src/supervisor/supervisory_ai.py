import pygame

class SupervisoryAI:
    def __init__(self, robots):
        self.robots = robots

    def monitor_and_reassign(self, w, h):
        for r in self.robots:
            if r.energy < 20:
                r.target = (w//2, h//2)

    def draw(self, win, w, h):
        pygame.draw.circle(win, (50,50,200), (w//2, h//2), 30)
        for r in self.robots:
            pygame.draw.line(win, (0,0,0), (w//2,h//2), (r.x,r.y), 1)
