import pygame
import math
from settings import PLAYER_ANGLE, PLAYER_POS, PLAYER_SPEED, PLAYER_ROT_SPEE


class Player:
    def __init__(self, game) -> None:
        self.game = game
        self.x = PLAYER_POS[0]
        self.y = PLAYER_POS[1]
        self.angle = PLAYER_ANGLE

    def move(self):
        # Calculate the movement based on the player's angle
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0

        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # Forwards
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:  # Backwards
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:  # Tankish left
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d]:  # Tankish right
            dx += -speed_sin
            dy += speed_cos

        self.check_collision(dx, dy)

        if keys[pygame.K_LEFT]:  # Rotate left
            self.angle -= PLAYER_ROT_SPEE * self.game.delta_time
        if keys[pygame.K_RIGHT]:  # Rotate right
            self.angle += PLAYER_ROT_SPEE * self.game.delta_time

        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.map

    def check_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pygame.draw.circle(
            self.game.screen,
            "green",
            (self.x * 100, self.y * 100),
            15,
        )

    def update(self):
        self.move()

    @property
    def pos(self):
        # Current position of the player
        return self.x, self.y

    @property
    def map_pos(self):
        # Current position of the player in the map
        return int(self.x), int(self.y)
