import pygame
import random
from playground.playground import PlayGround
from monsters.monster1.Monster1 import Monster1
from monsters.monster2.Monster2 import Monster2
from shop.Shop import Shop
from shop.ShopItem import ShopItem
pygame.font.init()
pygame.init()
clock = pygame.time.Clock()
path_array = []
# Število monsterjev glede na round
rounds = [[10, 5, 0, 0],
          [100, 5, 0, 0],
          [30, 5, 0, 0],
          [30, 20, 0, 0]]


class Game:
    def __init__(self, win, playground):
        self.enemies = []
        self.towers = []
        self.live = 1000
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
        self.menu = Shop(1200, 200, self.win, [ShopItem(1210, 210, "shop/archer_tower.png", "archer", 0), ShopItem(1210, 310, "shop/stone_tower.png", "stone", 0), ShopItem(1210, 410, "shop/magic_tower.png", "magic", 0)])
        self.is_tower_selected = False

    # Glavna zanka igre
    def run(self):
        while True:
            clock.tick(60)
            self.events()
            self.update()
            self.draw()
            self.display()
    # Dogodki
    def events(self):
        for event in pygame.event.get():
            # Zapremo igro, če pritisnemo križec
            if event.type == pygame.QUIT:
                raise SystemExit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_tower_selected:
                    self.is_tower_selected = False
                #path_array.append(pygame.mouse.get_pos())
                x, y = pygame.mouse.get_pos()
                # V meniju kupimo nov tower
                if self.menu.is_clicked(x, y):
                    item = self.menu.get_clicked()
                    self.selected_tower = item.get_tower()
                    self.is_tower_selected = True
                    self.towers.append("")

    # Posodobi elemente
    def update(self):
        remove = []
        for monster in self.monsters:
            if monster.finished():
                remove.append(monster)
                continue
            monster.walk()
        for i in remove:
            self.monsters.remove(i)
        if len(self.monsters) == 0:
            self.round += 1
            self.new_round()

    # Nariši elemente
    def draw(self):
        self.win.blit(self.bg, (0, 0))
        for monster in self.monsters:
            monster.draw()
        self.menu.draw()


    # Prikaži elemente
    def display(self):
        pygame.display.update()

    # Nova runda
    def new_round(self):
        # Če je runda končana, dodaj monsterje iz naslednje runde
        for j in range(rounds[self.round][0]):
            self.monsters.append(Monster1(self.win))
        for j in range(rounds[self.round][1]):
            self.monsters.append(Monster2(self.win))
        st = 0
        for monster in self.monsters:
            path_number = random.randint(0, len(self.playground.path) - 1)
            monster.set_path(self.playground.path[path_number], st)
            st += 1