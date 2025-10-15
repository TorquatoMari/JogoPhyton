#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from Code.EntityMediator import EntityMediator
from Code.const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY
from Code.entityFactory import EntityFactory
from Code.entity import Entity
from Code.player import Player


class Level:
    def __init__(self,window,name,game_mode):
        self.window = window
        self.name = name
        self.game_mode=game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        self.timeout=20000 #20 segundos
        pygame.time.set_timer(EVENT_ENEMY, millis=4000)


    def run(self):
        pygame.mixer_music.load('./Assets/Level1.mp3.wav')
        pygame.mixer_music.play(-1)
        clock=pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf,dest=ent.rect)
                ent.move()
                if isinstance(ent,(Player)):
                    shot=ent.shot()
                    if shot is not None:
                       self.entity_list.append(shot)
                if ent.name == 'Player':
                    self.level_text(text=f'Player - Health: {ent.health}',text_size=14,text_color=COLOR_WHITE,text_pos=(10, 25),)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==EVENT_ENEMY:
                    choice=random.choice(('Enemy1','Enemy2','Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))





            #printed text
            self.level_text(text=f'{self.name}-Timeout={self.timeout / 1000:.1f}s',text_size=14,text_color=COLOR_WHITE,text_pos=(10, 5))
            self.level_text(text=f'fps={clock.get_fps():.0f}',text_size=14,text_color=COLOR_WHITE,text_pos=(10, WIN_HEIGHT - 35),)
            self.level_text(text=f'entidades={len(self.entity_list)}',text_size=14,text_color=COLOR_WHITE,text_pos=(10, WIN_HEIGHT - 20))
            pygame.display.flip()
            #Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pass




    def level_text (self, text_size: int, text: str, text_color: tuple, text_pos=None):
        text_font: Font = pygame.font.Font("./Assets/PressStart2P-Regular.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0],top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
