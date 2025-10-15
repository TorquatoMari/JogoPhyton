# Code/background.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from Code.const import WIN_WIDTH, WIN_HEIGHT
from Code.entity import Entity

class Background(Entity):
    def __init__(self, name=str, position=(0,0), speed=2):
        # IMPORTANTE: super carrega ./Assets/{name}.png
        super().__init__(name=name, position=position)

        # ESCALA uma única vez para o tamanho da janela
        self.surf = pygame.transform.smoothscale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        # Reposiciona o rect após o scale
        self.rect = self.surf.get_rect(topleft=position)

        self.speed = speed

    def move(self):
        self.rect.x -= self.speed
        # wrap usando a largura já escalada
        if self.rect.right <= 0:
            self.rect.left += self.rect.width * 2