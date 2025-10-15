from Code.const import SHOT_SPEED, ENTITY_DAMAGE, DEFAULT_DAMAGE
from Code.entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.damage = ENTITY_DAMAGE.get(self.name, DEFAULT_DAMAGE)
        self.max_health = 1
        self.health = 1
        self.speed = SHOT_SPEED

    def move(self,):
        self.rect.centerx +=SHOT_SPEED