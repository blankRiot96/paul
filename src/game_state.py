import pygame

from src import shared, utils
from src.enums import State
from src.player import PlayerSystem
from src.tiles import TileSystem


class GameState:
    def __init__(self) -> None:
        shared.next_state = None
        shared.camera = utils.Camera()
        self.world = utils.World(
            "assets/level_1.tmx", systems=[PlayerSystem(), TileSystem()]
        )

    def update(self):
        self.world.update()

    def draw(self):
        self.world.draw()
