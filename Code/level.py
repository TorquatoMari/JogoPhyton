#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from Code.EntityMediator import EntityMediator
from Code.const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY
from Code.entityFactory import EntityFactory
from Code.entity import Entity
from Code.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode


        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))


        self.level_duration_ms = 60_000
        self.time_left_ms = self.level_duration_ms

        self.last_score = 0


        pygame.time.set_timer(EVENT_ENEMY, millis=4000)

    def run(self):
        try:
            pygame.mixer_music.load('./Assets/Level1.mp3.wav')
            pygame.mixer_music.play(-1)
        except Exception:
            pass

        clock = pygame.time.Clock()

        while True:
            dt = clock.tick(60) / 1000.0
            self.time_left_ms = max(0, self.time_left_ms - int(dt * 1000))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY and self.time_left_ms > 0:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))


            player = next((e for e in self.entity_list if isinstance(e, Player)), None)
            if player:
                player.update_timers(dt)
                if player.health <= 0:
                    pygame.time.set_timer(EVENT_ENEMY, 0)
                    try:
                        pygame.mixer_music.fadeout(800)
                    except Exception:
                        pass
                    self.last_score = getattr(player, "score", 0)
                    return "GAME_OVER"


            if self.time_left_ms == 0:
                pygame.time.set_timer(EVENT_ENEMY, 0)
                try:
                    pygame.mixer_music.fadeout(800)
                except Exception:
                    pass
                self.last_score = getattr(player, "score", 0) if player else 0
                return "WIN"


            for ent in self.entity_list:
                ent.move()
                self.window.blit(source=ent.surf, dest=ent.rect)

                if isinstance(ent, Player):
                    shot = ent.shot()
                    if shot is not None:
                        self.entity_list.append(shot)


            secs = self.time_left_ms / 1000
            self.level_text(
                text=f'{self.name} - Timeout={secs:0.1f}s',
                text_size=14,
                text_color=COLOR_WHITE,
                text_pos=(10, 5)
            )
            if player:
                self.level_text(
                    text=f'Player - Health: {player.health}  Score: {getattr(player, "score", 0)}',
                    text_size=14,
                    text_color=COLOR_WHITE,
                    text_pos=(10, 25)
                )
            self.level_text(
                text=f'fps={clock.get_fps():.0f}',
                text_size=14,
                text_color=COLOR_WHITE,
                text_pos=(10, WIN_HEIGHT - 35)
            )
            self.level_text(
                text=f'entidades={len(self.entity_list)}',
                text_size=14,
                text_color=COLOR_WHITE,
                text_pos=(10, WIN_HEIGHT - 20)
            )

            pygame.display.flip()


            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos=None):
        text_font: Font = pygame.font.Font("./Assets/PressStart2P-Regular.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
