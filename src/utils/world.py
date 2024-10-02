from pathlib import Path

import pygame
import pytmx

from src import shared

from .components import Components
from .systems import CollisionSystem, GravitySystem

type TiledClass = str


class World:
    def __init__(self, map_path: str | Path, systems: list) -> None:
        shared.entities = {}
        self.map = pytmx.load_pygame(map_path)
        self.process_map()
        self.systems = systems

    def process_map(self):
        for layer_index, layer in enumerate(self.map.layers):
            self.process_tiled_layer(layer_index, layer)

    def process_tiled_layer(self, layer_index: int, layer: pytmx.TiledTileLayer):
        for x, y, image in layer.tiles():
            properties = self.map.get_tile_properties(x, y, layer_index)
            self.process_tile(properties, x, y, image)

    def process_tile(
        self, properties: dict, x: int, y: int, image: pygame.Surface | None
    ):
        tiled_class_name = properties["type"]
        pos = pygame.Vector2(x, y) * self.map.tilewidth
        components = (
            Components()
            .set_hitbox(pos, size=image.get_size())
            .set_gravity()
            .set_image(image)
        )

        if shared.entities.get(tiled_class_name) is None:
            shared.entities[tiled_class_name] = []
        shared.entities[tiled_class_name].append(components)

    def update(self):
        for system in self.systems:
            system.update()

    def draw(self):
        for system in self.systems:
            system.draw()
