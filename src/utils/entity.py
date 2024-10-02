from dataclasses import dataclass

from .components import COMPONENT_LIST


@dataclass
class Entity:
    tiled_class: str
    components: COMPONENT_LIST
