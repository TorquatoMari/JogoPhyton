#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from Code.const import ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):
    def __init__(self,name:str,position:tuple):
        self.name = name
        self.surf = pygame.image.load('./Assets/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0],top=position[1])
        self.speed=0
        self.damage=ENTITY_DAMAGE.get(self.name,0)
        self.last_dmg='None'



    @abstractmethod
    def move(self, ):
        pass
