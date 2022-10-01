import pygame as pg
from pygame.sprite import Sprite

class Car(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pg.image.load('imgs/car.png')
        self.image = pg.transform.scale(self.image, (self.image.get_width()//3, self.image.get_height()//3))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.speed = 2
        self.move_right = False
        self.move_left = False
        self.turbo = False
        # pg.transform.scale(pg.image.load('imgs/pngegg.png'), (90, 80))

    def update(self):
        if self.turbo:
            speed = self.speed * 2
        else:
            speed = self.speed
        if self.move_right:
            if self.x < self.screen_rect.width - self.rect.width:
                self.x += speed
        if self.move_left:
            if self.x > 0:
                self.x -= speed
        self.rect.x = int(self.x)


    def draw(self):
        self.screen.blit(self.image, self.rect)