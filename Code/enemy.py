#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.const import WIN_WIDTH, ENEMY_SCALE, ENTITY_HEALTH, DEFAULT_HP, ENEMY_SPEED, DEFAULT_ENEMY_SPEED
from Code.entity import Entity



class Enemy(Entity):
    def __init__(self, name: str, position: tuple[int, int]):
        super().__init__(name, position)  # Entity define self.surf e self.rect (left/top)

        base_hp = ENTITY_HEALTH.get(name, DEFAULT_HP)
        self.max_health = base_hp
        self.health = base_hp

        # Velocidade por tipo
        self.speed = ENEMY_SPEED.get(name, DEFAULT_ENEMY_SPEED)

        # scale único
        w, h = self.surf.get_size()
        self.surf = pygame.transform.smoothscale(self.surf, (int(w * ENEMY_SCALE), int(h * ENEMY_SCALE)))

        # preserva a âncora left/top original
        left, top = self.rect.left, self.rect.top
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = left, top

    def move(self):
        #self.rect.centerx -= ENEMY_SPEED[self.name]
        self.rect.centerx -= self.speed

