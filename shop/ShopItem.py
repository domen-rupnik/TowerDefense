import pygame

class ShopItem:
    def __init__(self, x, y, img, tower_name, item_cost):
        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.item_cost = item_cost
        self.items = 0
        self.bg = pygame.transform.scale(pygame.image.load(img), (80, 80))
        self.tower = tower_name

    def get_tower(self):
        return self.tower

