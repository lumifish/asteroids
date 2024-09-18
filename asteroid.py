from circleshape import *
from constants import *
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        new_x = self.position.x
        new_y = self.position.y
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        smaller_asteroid1 = Asteroid(new_x, new_y, new_rad)
        smaller_asteroid2 = Asteroid(new_x, new_y, new_rad)

        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        smaller_asteroid1.velocity = a * 1.2
        smaller_asteroid2.velocity = b * 1.2



