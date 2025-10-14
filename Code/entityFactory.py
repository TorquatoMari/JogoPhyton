#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from Code.background import Background
from Code.const import WIN_WIDTH, WIN_HEIGHT
from Code.player import Player
from Code.enemy import Enemy

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
            case 'Enemy1' | 'Enemy2' | 'Enemy3':
                e = Enemy(entity_name, (0, 0))  # posição provisória; vamos ajustar já
                margin = 8

                # limites de Y seguros considerando a altura do sprite
                min_y = e.rect.height // 2 + margin
                max_y = WIN_HEIGHT - e.rect.height // 2 - margin
                y = random.randint(min_y, max_y)

                # nascer totalmente fora da tela pela direita
                e.rect.left = WIN_WIDTH + margin
                e.rect.centery = y
                return e

            case _:
                raise ValueError(f"Entidade desconhecida: {entity_name}")


            #case 'Enemy1':
                #return Enemy('Enemy1',(WIN_WIDTH+10,random.randint(0,WIN_HEIGHT)))
            #case 'Enemy2':
                #return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))
            #case 'Enemy3':
                #return Enemy('Enemy3', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT)))

