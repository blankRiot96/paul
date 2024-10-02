from __future__ import annotations

import typing as t

import pygame

if t.TYPE_CHECKING:
    from src import utils
    from src.enums import State
    from src.player import Player
    from src.utils.components import Components

# Utils
entities: dict[str, list[Components]]

# Canvas
screen: pygame.Surface
srect: pygame.Rect
camera: utils.Camera

# Events
events: list[pygame.event.Event]
mouse_pos: pygame.Vector2
mouse_press: tuple[int, ...]
keys: list[bool]
kp: list[bool]
kr: list[bool]
dt: float
clock: pygame.Clock

# States
next_state: State | None

# Entities
player: Player
