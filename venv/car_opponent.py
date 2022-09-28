import pygame as pg
from random import randint
from pygame.sprite import Sprite
from random import choice
class Car_opponent:
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image1 = pg.image.load('imgs/car_opponent.png')
        self.image1 = pg.transform.scale(self.image1, (self.image1.get_width()//4, self.image1.get_height()//4))
        self.image2 = pg.image.load('imgs/car_opponent2.png')
        self.image2 = pg.transform.scale(self.image2, (self.image2.get_width() // 2, self.image2.get_height() // 2))
        self.image3 = pg.image.load('imgs/car_opponent3.png')
        self.image3 = pg.transform.scale(self.image3, (self.image3.get_width() // 3.5, self.image2.get_height() // 1))
        self.images = [self.image1, self.image2, self.image3]
        self.image = choice(self.images)





        self.rect = self.image.get_rect()
        self.speed = randint(10, 30) / 10 + game.road.speed
        self.y = float(self.rect.y)
        self.rect.x = randint(0, self.screen_rect.width - self.rect.width)
    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y
        if self.rect.top > self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.top
            self.y = float(self.rect.y)
            self.speed = randint(10, 30) / 10
            self.image = choice(self.images)
            self.rect.x = randint(0, self.screen_rect.width - self.rect.width)





