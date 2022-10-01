import pygame as pg
from car import Car
from car_opponent import Car_opponent
from  time import sleep
# from lines import Line
from random import choice

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.running = True
        self.car = Car(self)
        # self.road = Line(self)
        self.cars = pg.sprite.Group()
        self.boom = pg.mixer.Sound("imgs/crash.mp3")
        self.boom.set_volume(0.1)
        self.background = pg.mixer.Sound("imgs/background.mp3")
        self.background.set_volume(0.1)
        self.background.play()
        self.cars_count = 6
        self.car_width = 100
        self.lines_count = self.screen.get_width() // self.car_width
        self.health = 3
        self.count_cars = 0
        self.speed_up = 1


    def _cars_update(self):
        self.cars.update()
        vacant = [line for line in range(self.lines_count)]
        for car in self.cars:
            vacant.remove(car.line_number)
            if car.rect.y > self.screen.get_height():
                self.count_cars += 1
                print(self.count_cars)
                self.cars.remove(car)



        if len(self.cars) < self.cars_count:
            self.cars.add(Car_opponent(game, choice(vacant)))

    def draw_healths(self):
        health_image = pg.transform.scale(pg.image.load("imgs/health.png"), (30, 30))
        for a in range(self.health):
            self.screen.blit(health_image, ((0 + health_image.get_width()+ 5) * a, 0))

    def run_game(self):
        while True:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        exit()
                    if event.key == pg.K_d:
                        self.car.move_right = True
                    if event.key == pg.K_a:
                        self.car.move_left = True
                    if event.key == pg.K_SPACE:
                        self.car.turbo = not self.car.turbo
                    if event.key == pg.K_r:
                        self.health = 3
                        self.running = True
                    if event.key == pg.K_p:
                        self.running = not self.running

                if event.type == pg.KEYUP:
                    if event.key == pg.K_d:
                        self.car.move_right = False
                    if event.key == pg.K_a:
                        self.car.move_left = False
            if self.health < 0:
                self.running = False
            if self.running:
                # обновлениеd
                crashed_car = pg.sprite.spritecollideany(self.car, self.cars)
                if crashed_car:
                    self.boom.play()
                    self.cars.remove(crashed_car)
                    self.health -= 1
                self.screen.fill((100, 100, 100))
                # self.road.draw()
                # self.road.update()
                self.car.update()
                self.car.draw()
                self._cars_update()
                self.cars.draw(self.screen)
                self.draw_healths()
                pg.display.flip()
game = Game()
game.run_game()