from datetime import datetime

import pygame
import math
import numpy as np
from operator import itemgetter

class ArcherTower(pygame.sprite.Sprite):
    def __init__(self, win):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.height = 141
        self.width = 120
        self.level = 1
        self.ranges = [250, 250, 270]
        self.range = self.ranges[self.level - 1]
        self.upgrade_cost = 0
        self.sell_cost = 0
        self.selected = False
        self.menu = None
        self.win = win
        self.images_archers = []
        for i in range(1, 7):
            self.images_archers.append(pygame.transform.scale(pygame.image.load('towers/ArcherTower/archer_1_' + str(i) + '.png'), (35, 35)))
        self.images_tops = [pygame.transform.scale(pygame.image.load('towers/ArcherTower/tower_1_1.png'), (86, 26))]
        self.images_tower = [pygame.transform.scale(pygame.image.load('towers/ArcherTower/tower_1_2.png'), (120, 115))]
        self.img_count = 0
        self.count = 0
        self.power = 25
        self.arr = pygame.transform.scale(pygame.image.load('towers/ArcherTower/arrow_1.png'), (31, 10))
        self.arrow = self.arr
        self.target = None
        self.arrow_pos = [self.x, self.y]
        self.arrow_count = 0
        self.x_path = []
        self.y_path = []
        self.setted = False
        self.shoted = datetime.now()

    def move(self, x, y):
        self.x = x - (self.width // 2)
        self.y = y - ((self.height - 26) // 2)

    def draw(self):
        self.win.blit(self.images_tops[self.level - 1], (self.x + 5, self.y - 20))
        self.win.blit(self.images_tower[self.level - 1], (self.x, self.y))
        if self.target:
            if self.count > 60:
                self.count = 0
            self.img_count = 0
            if self.count > 10:
                self.img_count = 1
            if self.count > 20:
                self.img_count = 2
            if self.count > 30:
                self.img_count = 3
            if self.count > 40:
                self.img_count = 4
            if self.count > 50:
                self.img_count = 5
            if self.x > self.target.x:
                self.win.blit(pygame.transform.flip(self.images_archers[self.img_count], 1, 0), (self.x + 30, self.y - 25))
            else:
                self.win.blit(self.images_archers[self.img_count], (self.x + 30, self.y - 25))
            self.count += 1
        else:
            self.win.blit(self.images_archers[0], (self.x + 30, self.y - 25))
        self.win.blit(self.arrow, (self.arrow_pos[0] - int(self.arrow.get_width()), self.arrow_pos[1] - int(self.arrow.get_width())))

    def shoot(self, monsters):
        if not self.setted:
            return
        if not self.target:
            if (datetime.now() - self.shoted).total_seconds() < 0.5:
                return
            self.shoted = datetime.now()
            range_to_monster = ()
            for monster in monsters:
                x = monster.x
                y = monster.y
                # Evklidska razdalja stolpa do pošasti
                range = math.sqrt(math.pow((self.x - x), 2) + math.pow((self.y - y), 2))
                if range < self.range:
                    range_to_monster += ((monster, range),)
            if range_to_monster:
                urejen = sorted(range_to_monster, key=itemgetter(1))
                self.target = urejen[-1][0]
                self.arrow_count = 0
                self.arrow_pos = [self.x + 50, self.y]
                self.calculate_angle()
        else:
            self.calculate_angle()
            self.arrow_count += 1
            self.x_path = np.linspace(self.arrow_pos[0], self.target.x, 400)
            self.y_path = np.linspace(self.arrow_pos[1], self.target.y, 400)
            self.arrow_pos[0] = self.x_path[self.arrow_count]
            self.arrow_pos[1] = self.y_path[self.arrow_count]
            self.is_hit()

    def is_hit(self):
        if self.arrow_pos[0] + 32 > self.target.x > self.arrow_pos[0] - 32 and self.arrow_pos[1] + 32 > self.target.y > \
                self.arrow_pos[1] - 32:
            self.target.hit(self.power)
            self.target = None
            self.arrow_pos = [-100, -100]
        else:
            range = math.sqrt(math.pow((self.arrow_pos[0] - self.target.x), 2) + math.pow((self.arrow_pos[1] - self.target.y), 2))
            if self.range < range:
                self.target = None
                self.arrow_pos = [-100, -100]

    def calculate_angle(self):
        deltax = self.arrow_pos[0] - self.target.x
        deltay = self.arrow_pos[1] - self.target.y
        self.arrow = pygame.transform.rotate(self.arr, math.degrees(math.atan2(deltax, deltay)) + 90)

    def get_target(self):
        return self.target

    def set(self):
        self.setted = True