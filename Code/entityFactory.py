#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.background import Background
from Code.const import WIN_WIDTH, WIN_HEIGHT
from Code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name=str,position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg=[]
                for i in range(3):
                    list_bg.append(Background(name=f'Level1Bg{i}', position= (0,0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case'Player':
                p = Player('Player', (10, 0))
                p.rect.midleft = (10, WIN_HEIGHT // 2)
                return p

