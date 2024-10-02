import pygame

from src import shared, utils


class TileSystem:
    def update(self) -> None:
        pass

    def draw(self) -> None:
        for tile in shared.entities["tile"]:
            shared.screen.blit(tile.image.surf, shared.camera.transform(tile.pos.pos))
