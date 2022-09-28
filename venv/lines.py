import pygame as pg
from random import randint
from pygame.sprite import Sprite
class Line:
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pg.image.load('imgs/fon_doroga.png')
        self.image = pg.transform.scale(self.image, (self.screen_rect.width, self.image.get_height()))
        self.rect = self.image.get_rect()
        self.speed = 1
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        # if self.rect.top > self.screen_rect.bottom:
        #     self.rect.bottom = self.screen_rect.top
        #     self.y = float(self.rect.y)
        #     self.speed = randint(10, 30) / 10
        #     self.image = choice(self.images)
        #     self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
        #




