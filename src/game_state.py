import pygame

from src import shared, utils
from src.enums import State


class GameState:
    def __init__(self) -> None:
        self.map = utils.MapReader("assets/level_1.tmx")
        shared.camera = utils.Camera()

    def update(self):
        dx = shared.keys[pygame.K_d] - shared.keys[pygame.K_a]
        dy = shared.keys[pygame.K_s] - shared.keys[pygame.K_w]
        dv = pygame.Vector2(dx, dy) * 400 * shared.dt
        shared.camera.offset += dv

    def draw(self):
        for tile in self.map.tiles:
            shared.screen.blit(tile.image, shared.camera.transform(tile.pos))
