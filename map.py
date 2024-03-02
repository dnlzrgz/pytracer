import pygame

_ = 0
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, _, 1, 1, 1, 1, 1, _, _, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, 1, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, _, 1, 1, 1, _, 1, 1, 1, 1],
    [1, 1, _, 1, 1, 1, 1, _, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, _, 1, 1, _, _, 1],
    [1, _, _, _, 1, _, _, _, 1, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Map:
    def __init__(self, game) -> None:
        self.game = game
        self.map = {}
        self.load()

    def load(self):
        for j, row in enumerate(map):
            for i, value in enumerate(row):
                if value != 0:
                    self.map[(i, j)] = value

    def draw(self):
        [
            pygame.draw.rect(
                self.game.screen,
                "darkgray",
                (
                    pos[0] * 100,
                    pos[1] * 100,
                    100,
                    100,
                ),
                2,
            )
            for pos in self.map
        ]
