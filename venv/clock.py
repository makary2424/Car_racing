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

    def reposition(self):
        self.image = pg.image.load('imgs/clock.png')
        self.width = 100
        self.height = 100
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.screen_rect.width)
        self.rect.bottom = self.screen_rect.top
        self.y = float(self.rect.y)
        self.speed = ((randint(10, 30)) / 10) * self.game.speed_up

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.top > self.screen_rect.bottom:
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)






