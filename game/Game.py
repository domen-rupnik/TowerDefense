import pygame
import random
import time
from datetime import datetime
from playground.playground import PlayGround
from game.Pause import Pause
from monsters.monster1.Monster1 import Monster1
from monsters.monster2.Monster2 import Monster2
from monsters.monster3.Monster3 import Monster3
from monsters.monster4.Monster4 import Monster4
from towers.ArcherTower.ArcherTower import ArcherTower
from towers.ArcherTower2.ArcherTower2 import ArcherTower2
from towers.ArcherTower3.ArcherTower3 import ArcherTower3
from shop.Shop import Shop
from shop.ShopItem import ShopItem

pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
path_array = []
white = (255, 255, 255)

# Število monsterjev glede na round
rounds = [[10, 5, 1, 1],
          [20, 5, 0, 0],
          [30, 5, 0, 0],
          [30, 20, 0, 0],
          [50, 40, 0, 0],
          [100, 30, 0, 0]]


class Game:
    def __init__(self, win, playground, music, sound, player):
        self.wait = datetime.now()
        self.player = player
        self.enemies = []
        self.towers = []
        self.life = 100
        self.round = -1
        self.selected_tower = None
        self.pause = False
        self.money = 100
        self.win = win
        self.monsters = []
        self.towers = []
        self.playgrounds = [PlayGround(1)]
        self.playground = self.playgrounds[playground]
        self.bg = self.playground.background
        self.round_finished = True
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.life_text = self.life_font.render(str(self.life), True, white)
        self.menu = Shop(1200, 200, self.win, [ShopItem(1210, 210, "shop/archer_tower.png", "archer", 100),
                                               ShopItem(1210, 310, "shop/stone_tower.png", "archer2", 300),
                                               ShopItem(1210, 410, "shop/magic_tower.png", "archer3", 600)])
        self.is_tower_selected = False
        self.life_image = pygame.transform.scale(pygame.image.load("game_assets/life/heart.png"), (30, 30))
        self.failed_image = pygame.transform.scale(pygame.image.load("game_assets/failed/header_failed.png"),
                                                   (300, 150))
        pygame.mixer.stop()
        self.music = music
        self.sound = sound
        if self.music:
            pygame.mixer.music.load("sounds/in_game.wav")
            pygame.mixer.music.play(-1, 0)
        self.left = pygame.transform.scale(pygame.image.load("game_assets/td-gui/failed/button_left.png"), (75, 75))
        self.end = False
        self.points = 0
        self.star = pygame.transform.scale(pygame.image.load("game_assets/td-gui/upgrade/star.png"), (30, 30))
        self.money = 100
        self.moneyText = self.life_font.render(str(self.money), True, white)
        self.pohitritev = 0
        self.pointsImg = pygame.transform.scale(pygame.image.load('game_assets/td-gui/win/zip.png'), (30, 30))
        self.pause_btn = pygame.transform.scale(pygame.image.load("game_assets/td-gui/interface_game/button_pause.png"), (75, 75))

    # Glavna zanka igre
    def run(self):
        while True:
            clock.tick(60)
            self.events()
            self.update()
            self.draw()
            self.display()
            if self.end:
                f = open('results.txt', 'a+')
                f.write(self.player + ":" + str(self.points) + "\n")
                f.close()
                return

    # Dogodki
    def events(self):
        for event in pygame.event.get():
            # Zapremo igro, če pritisnemo križec
            if event.type == pygame.QUIT:
                f = open('results.txt', 'a+')
                f.write(self.player + ":" + self.points + "\n")
                f.close()
                raise SystemExit

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_tower_selected:
                    self.is_tower_selected = False
                    self.selected_tower.set()

                # path_array.append(pygame.mouse.get_pos())
                x, y = pygame.mouse.get_pos()
                # V meniju kupimo nov tower
                if self.menu.is_clicked(x, y):
                    item = self.menu.get_clicked()
                    self.is_tower_selected = True
                    if item.tower == "archer":
                        if self.money >= 100:
                            self.selected_tower = ArcherTower(self.win)
                            self.selected_tower.move(x, y)
                            self.towers.append(self.selected_tower)
                            self.money -= 100
                        else:
                            self.is_tower_selected = False
                            self.selected_tower = None
                    elif item.tower == "archer2":
                        if self.money >= 300:
                            self.selected_tower = ArcherTower2(self.win)
                            self.selected_tower.move(x, y)
                            self.towers.append(self.selected_tower)
                            self.money -= 400
                        else:
                            self.is_tower_selected = False
                            self.selected_tower = None

                    elif item.tower == "archer3":
                        if self.money >= 600:
                            self.selected_tower = ArcherTower3(self.win)
                            self.selected_tower.move(x, y)
                            self.towers.append(self.selected_tower)
                            self.money -= 1000
                        else:
                            self.is_tower_selected = False
                            self.selected_tower = None
                    self.menu.unclick()

                if 1250 < x < 1325 and 25 < y < 100:
                    self.end = True
                    pygame.mixer.music.stop()

                if 1250 < x < 1325 and 110 < y < 185:
                    Pause(self.win).run()
                    if self.music:
                        pygame.mixer.music.unpause()

    # Posodobi elemente
    def update(self):
        self.moneyText = self.life_font.render(str(self.money), True, white)
        remove = []
        for monster in self.monsters:
            if monster.finished():
                self.life -= monster.damage
                self.life_text = self.life_font.render(str(self.life), True, white)
                if self.life <= 0:
                    self.win.blit(self.bg, (0, 0))
                    self.win.blit(self.failed_image, (1350 / 2 - 150, 700 / 2 - 75))
                    points_t = self.life_font.render(str(self.points), True, white)
                    pointsRect = points_t.get_rect()
                    pointsRect.center = (675, 600)
                    imgPoints = self.pointsImg.get_rect()
                    imgPoints.center = (620, 600)
                    self.win.blit(points_t, pointsRect)
                    self.win.blit(self.pointsImg, imgPoints)
                    self.display()
                    time.sleep(5)
                    self.end = True
                    break
                remove.append(monster)
                continue
            monster.walk(self.sound)
        for i in remove:
            self.monsters.remove(i)
        if len(self.monsters) == 0:
            self.round += 1
            self.new_round()

        # Premikamo stolp, če imamo izbran tower
        if self.is_tower_selected:
            x, y = pygame.mouse.get_pos()
            self.selected_tower.move(x, y)
        remove_monster = []

        # Ustrelimo stolpe
        if len(self.monsters) > 0:
            for i in self.towers:
                i.shoot(self.monsters)
        for monster in self.monsters:
            if monster.death():
                self.points += monster.points
                self.money += monster.points // 2
                remove_monster.append(monster)
        for i in remove_monster:
            self.monsters.remove(i)

    # Nariši elemente
    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for monster in self.monsters:
            monster.draw()
        for tower in self.towers:
            tower.draw()
        self.menu.draw()

        # Narišemo življenje igralca
        textRect = self.life_text.get_rect()
        textRect.center = (1200, 50)
        imgLife = self.life_image.get_rect()
        imgLife.center = (1150, 50)
        imgStar = self.star.get_rect()
        imgStar.center = (1150, 100)
        moneyRect = self.moneyText.get_rect()
        moneyRect.center = (1200, 100)
        self.win.blit(self.life_image, imgLife)
        self.win.blit(self.life_text, textRect)
        self.win.blit(self.star, imgStar)
        self.win.blit(self.moneyText, moneyRect)
        self.win.blit(self.left, (1250, 25))
        self.win.blit(self.pause_btn, (1250, 110))

        points_t = self.life_font.render(str(self.points), True, white)
        pointsRect = points_t.get_rect()
        pointsRect.center = (1200, 150)
        imgPoints = self.pointsImg.get_rect()
        imgPoints.center = (1150, 150)
        self.win.blit(points_t, pointsRect)
        self.win.blit(self.pointsImg, imgPoints)

    # Prikaži elemente
    def display(self):
        pygame.display.update()

    # Nova runda
    def new_round(self):
        # Če je runda končana, dodaj monsterje iz naslednje runde
        if (datetime.now() - self.wait).total_seconds() < 5:
            self.round -= 1
            return
        self.money += 20
        self.points += 20
        # Seštej moč igralca
        power = 0
        for i in self.towers:
            power += i.power
        power += 2**self.round
        if self.round % 10 == 0:
            self.pohitritev += 1
        # Dodajaj pošasti dokler moč ni izenačena
        while power > 0:
            posasti = [Monster1(self.win), Monster1(self.win), Monster1(self.win), Monster1(self.win), Monster2(self.win), Monster2(self.win), Monster2(self.win), Monster3(self.win), Monster4(self.win)]
            posast = random.choice(posasti)
            if power - posast.damage < -10:
                continue
            power -= posast.damage
            posast.speed += self.pohitritev
            self.monsters.append(posast)
        st = 0
        for monster in self.monsters:
            path_number = random.randint(0, len(self.playground.path) - 1)
            monster.set_path(self.playground.path[path_number], st)
            st += 1
