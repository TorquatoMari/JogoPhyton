#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))  # cria a janela do jogo

    def run(self):
        while True:  # precisa de um loop pra janela se manter aberta
            menu = Menu(self.window)
            menu.run()
            pass

        # for event in pygame.event.get():  # retorna todos os eventos
        # if event.type == pygame.QUIT:  # evento de fechar janela
        # pygame.quit()  # fecha a janela
        # quit()
