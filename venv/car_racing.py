import pygame as pg
from car import Car
from car_opponent import Car_opponent
from lines import Line


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.running = True
        self.car = Car(self)
        self.road = Line(self)
        self.car_opponent = Car_opponent(self)
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        self.running = False
                    if event.key == pg.K_d:
                        self.car.move_right = True
                    if event.key == pg.K_a:
                        self.car.move_left = True

                if event.type == pg.KEYUP:
                    if event.key == pg.K_d:
                        self.car.move_right = False
                    if event.key == pg.K_a:
                        self.car.move_left = False
                # pg.sprite.groupcollide(self.car, Car_opponent)

            # обновление экрана
            self.screen.fill((100, 100, 100))
            self.road.draw()
            self.car.update()
            self.car.draw()
            self.car_opponent.update()
            self.car_opponent.draw()
            self.road.update()
            pg.display.flip()
game = Game()