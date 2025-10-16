#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame

from Code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, COLOR_WHITE
from Code.level import Level
from Code.menu import Menu
from Code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Seu Jogo")

    def run(self):
        while True:
            score=Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'Level', menu_return)
                result = level.run()

                final_score=getattr(level, "last_score", 0)
                score.save_score(menu_return, [final_score])


                if result == "WIN":
                    self._flash_message("YOU WIN!", 1.5)
                elif result == "GAME_OVER":
                    self._flash_message("GAME OVER", 1.8)

            elif menu_return == MENU_OPTION[1]:
                score.show_score()

            elif menu_return == MENU_OPTION[2]:  # "EXIT"
                pygame.quit()
                sys.exit()
            else:
                pass


    def _flash_message(self, text: str, seconds: float = 1.5):
        clock = pygame.time.Clock()
        elapsed = 0.0
        font = pygame.font.Font("./Assets/PressStart2P-Regular.ttf", 24)
        surf = font.render(text, True, COLOR_WHITE).convert_alpha()
        rect = surf.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

        while elapsed < seconds:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            self.window.fill((0, 0, 0))
            self.window.blit(surf, rect)
            pygame.display.flip()

            dt = clock.tick(60) / 1000.0
            elapsed += dt
