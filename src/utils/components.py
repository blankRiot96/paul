import abc

import pygame

from src import shared


class Component(abc.ABC):
    """Base class for every mechanical component of an entity"""


class Controllable(Component):
    """Can be moved around with hardware input"""


class Gravitational(Component):
    """Is affected by the world's gravity"""


class Collidable(Component):
    """Can collide with other `Collidable` entities"""
