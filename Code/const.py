# Code/const.py

import pygame

# Cores
COLOR_WHITE = (255, 255, 255)
COLOR_BLUE  = (109, 157, 197)

# HP
DEFAULT_HP = 50
ENTITY_HEALTH = {
    'Player': 300,
    'Enemy1': 70,
    'Enemy2': 65,
    'Enemy3': 60,
}

# Velocidades
# Velocidade por tipo de inimigo
ENEMY_SPEED = {
    'Enemy1': 4,
    'Enemy2': 3,
    'Enemy3': 2,
}
DEFAULT_ENEMY_SPEED = 3  # fallback, se vier um nome não mapeado

PLAYER_SPEED = 5

# Eventos
EVENT_ENEMY = pygame.USEREVENT + 1

# Escala
ENEMY_SCALE = 0.5

# Menu
MENU_OPTION = (
    'NEW GAME',
    'SCORE',
    'EXIT'
)

# Janela
WIN_WIDTH  = 1280
WIN_HEIGHT = 720