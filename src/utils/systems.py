import abc

from src import shared

from .components import *


class System(abc.ABC):
    # def __init__(self, entity_classes: list[str]) -> None:
    #     super().__init__()
    #     self.entity_classes = entity_classes

    def update(self):
        # for entity_class in self.entity_classes:
        #     for entities in shared.entities[entity_class]:
        #         for entity in entities:
        #             pass
        pass


class GravitySystem:
    pass


class CollisionSystem:
    pass
