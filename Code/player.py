#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from Code.PlayerShot import PlayerShot
from Code.const import PLAYER_SPEED, WIN_HEIGHT, WIN_WIDTH, ENTITY_HEALTH, DEFAULT_HP, ENTITY_SHOT_DELAY
from Code.entity import Entity


class Player(Entity):
    def __init__(self,name=str,position=tuple):
        super().__init__(name,position)
        self.shot_delay=ENTITY_SHOT_DELAY[self.name]
        base_hp = ENTITY_HEALTH.get(name, DEFAULT_HP)
        self.max_health = base_hp
        self.health = base_hp

        self.score = 0

        # i-frames
        self.invuln_time = 0.0
        self.invuln_max = 0.5  # ajuste fino: 0.3–0.7s

    def update_timers(self, dt: float):
        if self.invuln_time > 0.0:
            self.invuln_time = max(0.0, self.invuln_time - dt)

    def take_hit(self, dmg: int):
        if self.invuln_time <= 0.0:
            self.health = max(0, self.health - dmg)
            self.invuln_time = self.invuln_max



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

    def shot(self):
        self.shot_delay-=1
        if self.shot_delay<=0:
            self.shot_delay=ENTITY_SHOT_DELAY[self.name]
            pressed_key=pygame.key.get_pressed()
            if pressed_key[pygame.K_RCTRL]:
               return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx,self.rect.centery))