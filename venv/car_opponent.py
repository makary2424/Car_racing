import pygame as pg
from random import randint
from pygame.sprite import Sprite
from random import choice
class Car_opponent(Sprite):
    def __init__(self, game, line_number):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.reposition(line_number)

    def reposition(self, line_number):
        cars = ['car_opponent.png', 'car_opponent2.png', 'car_opponent3.png']
        self.image = pg.image.load(f'imgs/{choice(cars)}')
        self.width = 100
        self.height = 200
        self.image = pg.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.line_number = line_number
        self.rect.x = self.line_number * self.width
        self.rect.bottom = self.screen_rect.top
        self.y = float(self.rect.y)
        self.speed = ((randint(10, 30)) / 10) * self.game.speed_up

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.top > self.screen_rect.bottom:
            self.kill()






