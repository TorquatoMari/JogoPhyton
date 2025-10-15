# Code/entityFactory.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from Code.background import Background
from Code.const import WIN_WIDTH, WIN_HEIGHT
from Code.player import Player
from Code.enemy import Enemy

class EntityFactory:
    @staticmethod
    def get_entity(entity_name=str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                # nomes devem bater com os arquivos em Assets: Level1Bg0.png ... Level1Bg5.png
                bg_names = ['Level1Bg0','Level1Bg1','Level1Bg2','Level1Bg3','Level1Bg4','Level1Bg5']
                speed = 2  # mesma velocidade para todas

                layers = []
                for n in bg_names:
                    # duas cópias lado a lado, MESMO name (usa a mesma imagem)
                    bg1 = Background(name=n, position=(0, 0), speed=speed)
                    bg2 = Background(name=n, position=(WIN_WIDTH, 0), speed=speed)
                    layers.extend([bg1, bg2])
                return layers

            case 'Player':
                p = Player('Player', (10, 0))
                p.rect.midleft = (10, WIN_HEIGHT // 2)
                return p

            case 'Enemy1' | 'Enemy2'|'Enemy3':
                e = Enemy(entity_name, (0, 0))
                margin = 8
                min_y = e.rect.height // 2 + margin
                max_y = WIN_HEIGHT - e.rect.height // 2 - margin
                y = random.randint(min_y, max_y)
                e.rect.left = WIN_WIDTH + margin
                e.rect.centery = y
                return e

            case _:
                raise ValueError(f"Entidade desconhecida: {entity_name}")