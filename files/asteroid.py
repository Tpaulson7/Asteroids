from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, ):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            newAngle = random.uniform(20, 50)
            newVector = self.velocity.rotate(newAngle)
            newVector2 = self.velocity.rotate(-newAngle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0], self.position[1], newRadius)
            asteroid2 = Asteroid(self.position[0], self.position[1], newRadius)
            asteroid1.velocity = newVector * 1.2
            asteroid2.velocity = newVector2 * 1.2