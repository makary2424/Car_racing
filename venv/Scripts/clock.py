import pygame as pg
from random import randint
from pygame.sprite import Sprite
from random import choice
class Clock(Sprite):
    def __init__(self, game, line_number):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.reposition(line_number)