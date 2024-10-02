import typing as t
from collections.abc import Callable
from dataclasses import dataclass

import pygame


@dataclass
class Image:
    surf: pygame.Surface


@dataclass
class Gravity:
    intensity: float = 0.5  # Default intensity


@dataclass
class HitBox:
    rect: pygame.Rect


@dataclass
class Pos:
    pos: pygame.Vector2


class Components:
    def __init__(self) -> None:
        self.hitbox: HitBox | None = None
        self.pos: Pos | None = None
        self.gravity: Gravity | None = None
        self.image: Image | None = None

    def set_hitbox(self, pos: t.Sequence[float], size: t.Sequence[float]) -> t.Self:
        self.pos = Pos(pos=pygame.Vector2(pos))
        self.hitbox = HitBox(rect=pygame.Rect(pos, size))

        return self

    def set_gravity(self, intensity: float = 0.5) -> t.Self:
        self.gravity = Gravity(intensity)

        return self

    def set_image(self, surf: pygame.Surface) -> t.Self:
        self.image = Image(surf)

        return self
