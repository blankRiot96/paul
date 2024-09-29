import pygame

from src import shared, utils
from src.enums import State
from src.player import Player


class GameState:
    def __init__(self) -> None:
        shared.next_state = None
        self.map = utils.MapReader("assets/level_1.tmx")
        shared.camera = utils.Camera()
        for tile in self.map.tiles:
            if tile.id == 13:
                shared.player = Player()
            elif tile.id in (0, 1, 2, 10, 11, 12, 20, 21, 22):
                pass

    def update(self):
        dx = shared.keys[pygame.K_d] - shared.keys[pygame.K_a]
        dy = shared.keys[pygame.K_s] - shared.keys[pygame.K_w]
        dv = pygame.Vector2(dx, dy) * 200 * shared.dt
        shared.camera.offset += dv

    def draw(self):
        for tile in self.map.tiles:
            shared.screen.blit(tile.image, shared.camera.transform(tile.pos))
