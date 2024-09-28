from dataclasses import dataclass
from pathlib import Path

import pygame
import pytmx


@dataclass
class TileInfo:
    pos: pygame.Vector2
    image: pygame.Surface


class MapReader:
    def __init__(self, path: str | Path) -> None:
        self.map = pytmx.load_pygame(path)
        self.process_map()

    def process_map(self):
        self.tiles: list[TileInfo] = []
        self.tile_size = self.map.tilewidth
        for layer in self.map.layers:
            for x, y, image in layer.tiles():
                self.tiles.append(
                    TileInfo(pygame.Vector2(x, y) * self.tile_size, image)
                )
