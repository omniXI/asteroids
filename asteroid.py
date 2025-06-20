import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius, velocity2)
            asteroid.velocity = velocity1 * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius, velocity1)
            asteroid.velocity = velocity2 * 1.2

