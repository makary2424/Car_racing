import pygame as pg
from car import Car
from car_opponent import Car_opponent
from  time import sleep
# from lines import Line

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.running = True
        self.car = Car(self)
        # self.road = Line(self)
        self.cars = pg.sprite.Group()
        self.boom = pg.mixer.Sound("imgs/crash.mp3")
        self.boom.set_volume(0.3)
        self.background = pg.mixer.Sound("imgs/background.mp3")
        self.background.set_volume(0.3)
        self.background.play()
        self.cars_count = 6

    def _cars_update(self):
        self.cars.update()
        if len(self.cars) < self.cars_count:
            self.cars.add(Car_opponent(game))
        for car in self.cars:
            if car.rect.top > self.screen.get_height():
                self.cars.remove(car)
    def run_game(self):
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
                    if event.key == pg.K_SPACE:
                        self.car.turbo = not self.car.turbo

                if event.type == pg.KEYUP:
                    if event.key == pg.K_d:
                        self.car.move_right = False
                    if event.key == pg.K_a:
                        self.car.move_left = False
                if pg.sprite.spritecollideany(self.car, self.cars):
                    self.boom.play()


            # обновлениеd
            self.screen.fill((100, 100, 100))
            # self.road.draw()
            # self.road.update()
            self.car.update()
            self.car.draw()
            self._cars_update()
            self.cars.draw(self.screen)
            pg.display.flip()
game = Game()
game.run_game()