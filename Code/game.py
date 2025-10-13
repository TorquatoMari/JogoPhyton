#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.const import WIN_WIDTH, WIN_HEIGHT
from Code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))  # cria a janela do jogo

    def run(self):
        while True:  # precisa de um loop pra janela se manter aberta
            menu = Menu(self.window)
            menu.run()
            pass

