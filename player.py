import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)


    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_h]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, dt):
        if self.timer > 0:
            pass
        else:
            self.timer = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y)
            velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = velocity * PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt
