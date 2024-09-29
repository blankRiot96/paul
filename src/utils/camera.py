import typing as t

import pygame


class Camera:
    def __init__(self) -> None:
        self.offset = pygame.Vector2()

    def attach_to(self, pos: t.Sequence, screen_size: t.Sequence[int]):
        self.offset.x += (pos[0] - self.offset.x - (screen_size[0] // 2)) * 0.08
        self.offset.y += (pos[1] - self.offset.y - (screen_size[1] // 2)) * 0.08

    def transform(self, pos: t.Sequence) -> pygame.Vector2:
        return pygame.Vector2(pos[0] - self.offset.x, pos[1] - self.offset.y)
