#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from Code.const import WIN_WIDTH, COLOR_WHITE, MENU_OPTION, COLOR_BLUE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Assets/preview-01.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option=0
        pygame.mixer_music.load('./Assets/menuMusic.mp3')
        pygame.mixer_music.play(-1)  # -1 para deixar a musica tocando sem fim
        while True:  # o desenho da imagem fica em um loop infinito
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=60, text='Space', text_color=COLOR_WHITE, text_center_pos=((WIN_WIDTH / 2), 220))
            self.menu_text(text_size=60, text='Vanguard', text_color=COLOR_WHITE,text_center_pos=((WIN_WIDTH / 2), 300))

            for i in range(len(MENU_OPTION)):  # outro loop
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_BLUE,text_center_pos=((WIN_WIDTH / 2), 400 + 30 * i))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE,text_center_pos=((WIN_WIDTH / 2), 400 + 30 * i))  # impressao dinamica

            pygame.display.flip()

            for event in pygame.event.get():  # retorna todos os eventos
              if event.type == pygame.QUIT:  # evento de fechar janela
                pygame.quit()  # fecha a janela
                quit()

              if event.type==pygame.KEYDOWN:
                  if event.key==pygame.K_DOWN: #seta para baixo
                      if menu_option<len(MENU_OPTION)-1:
                          menu_option+=1
                      else:
                          menu_option=0
                  if event.key == pygame.K_UP:  # seta para cima
                     if menu_option >0:
                          menu_option -= 1
                     else:
                          menu_option = len(MENU_OPTION)-1

                  if event.key == pygame.K_RETURN: #Enter
                      return MENU_OPTION[menu_option]





    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
          text_font: Font = pygame.font.Font("./Assets/PressStart2P-Regular.ttf", size=text_size)
          text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
          text_rect: Rect = text_surf.get_rect(center=text_center_pos)
          self.window.blit(source=text_surf, dest=text_rect)
