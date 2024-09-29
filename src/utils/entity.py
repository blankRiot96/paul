import abc

import pygame

from src import shared

from .components import Component


class Entity(abc.ABC):
    """Base class for every Entity in the game"""

    def __init__(self, components: list[Component]) -> None:
        super().__init__()
