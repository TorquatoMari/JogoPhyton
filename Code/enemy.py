#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.const import WIN_WIDTH, ENEMY_SPEED1, ENEMY_SCALE
from Code.entity import Entity



class Enemy(Entity):
    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__(name, position)  # Entity define self.surf e self.rect (left/top)
        # scale único
        w, h = self.surf.get_size()
        self.surf = pygame.transform.smoothscale(self.surf, (int(w * ENEMY_SCALE), int(h * ENEMY_SCALE)))
        # preservar a âncora left/top original
        left, top = self.rect.left, self.rect.top
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = left, top

    def move(self):
        self.rect.centerx -= ENEMY_SPEED1
        if self.rect.right <= 0:
            # reaparece totalmente fora da tela à direita
            self.rect.left = WIN_WIDTH + 8


#class Enemy(Entity):
    #def __init__(self,name=str,position=tuple):
        #super().__init__(name,position)


    #def move(self, ):
        #self.rect.centerx -= ENEMY_SPEED1
        #if self.rect.right <= 0:
            #self.rect.left = WIN_WIDTH
