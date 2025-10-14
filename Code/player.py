#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Code.const import PLAYER_SPEED, WIN_HEIGHT, WIN_WIDTH
from Code.entity import Entity


class Player(Entity):
    def __init__(self,name=str,position=tuple):
        super().__init__(name,position)


    def move(self, ):
        pressed_key=pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top>0:
            self.rect.centery -= PLAYER_SPEED
        if pressed_key[pygame.K_DOWN] and self.rect.bottom<WIN_HEIGHT:
            self.rect.centery += PLAYER_SPEED
        if pressed_key[pygame.K_LEFT] and self.rect.left >0:
            self.rect.centerx -= PLAYER_SPEED
        if pressed_key[pygame.K_RIGHT] and self.rect.right <WIN_WIDTH:
            self.rect.centerx += PLAYER_SPEED
        pass

