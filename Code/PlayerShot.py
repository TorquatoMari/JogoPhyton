from Code.const import SHOT_SPEED
from Code.entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self,):
        self.rect.centerx +=SHOT_SPEED