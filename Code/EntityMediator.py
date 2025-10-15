from Code.PlayerShot import PlayerShot
from Code.const import WIN_WIDTH
from Code.enemy import Enemy
from Code.entity import Entity
from Code.player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent=Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True

        # Enemy x Player (dano por contato no Player)
        elif (isinstance(ent1, Enemy) and isinstance(ent2, Player)) or (
                        isinstance(ent1, Player) and isinstance(ent2, Enemy)):
            # AABB overlap
            if (
                    ent1.rect.right >= ent2.rect.left
                    and ent1.rect.left <= ent2.rect.right
                    and ent1.rect.bottom >= ent2.rect.top
                    and ent1.rect.top <= ent2.rect.bottom
            ):
                # identifica quem é quem
                enemy, player = (ent1, ent2) if isinstance(ent1, Enemy) else (ent2, ent1)
                # aplica dano ao player com base no dano do inimigo (asteroide)
                player.health -= getattr(enemy, "damage", 0)
                player.last_dmg = enemy.name
            return  # evita cair no bloco abaixo

        if valid_interaction:  # mesma coisa que if valid_interaction==True
           if (
                ent1.rect.right >= ent2.rect.left
                and ent1.rect.left <= ent2.rect.right
                and ent1.rect.bottom >= ent2.rect.top
                and ent1.rect.top <= ent2.rect.bottom
             ):
                ent1.health -=ent2.damage
                ent2.health-=ent1.damage
                ent1.last_dmg=ent2.name
                ent2.last_dmg=ent1.name
    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]) -> None:
        # remove com segurança iterando sobre uma cópia
        for ent in entity_list[:]:
            hp = getattr(ent, "health", None)
            if isinstance(hp, (int, float)) and hp <= 0:
                entity_list.remove(ent)
