import pygame

from src import shared, utils


class PlayerSystem:
    def update(self) -> None:
        player = shared.entities["player"][0]
        player.pos.pos.x += 15 * shared.dt
        player.hitbox.rect.topleft = player.pos.pos
        shared.camera.attach_to(player.pos.pos)

    def draw(self) -> None:
        player = shared.entities["player"][0]
        shared.screen.blit(
            player.image.surf, shared.camera.transform(player.hitbox.rect)
        )
