# Code/const.py

import pygame

#C
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE  = (109, 157, 197)


#D
DEFAULT_HP = 50
DEFAULT_DAMAGE = 10
DEFAULT_ENEMY_SPEED = 3  # fallback, se vier um nome não mapeado

#E
ENTITY_HEALTH = {
    'Player': 300,
    'Enemy1': 70,
    'Enemy2': 65,
    'Enemy3': 60,
}


ENEMY_SPEED = {
    'Enemy1': 4,
    'Enemy2': 3,
    'Enemy3': 5,
}


EVENT_ENEMY = pygame.USEREVENT + 1

ENEMY_SCALE = 0.5

ENTITY_SHOT_DELAY={'Player':20}

ENTITY_DAMAGE = {
    'Player': 0,      # o player em si não “causa dano” por contato (se for o tiro que causa)
    'PlayerShot': 25, # dano do projétil do player
    'Enemy1': 10,
    'Enemy2': 12,
    'Enemy3': 15,
}

# M
MENU_OPTION = (
    'NEW GAME',
    'SCORE',
    'EXIT'
)

#P
PLAYER_SPEED = 5



#S
SHOT_SPEED=5

# W
WIN_WIDTH  = 1280
WIN_HEIGHT = 720