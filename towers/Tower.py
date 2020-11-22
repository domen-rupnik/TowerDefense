import pygame

class Tower(pygame.sprite.Sprite):
    def __init__(self, win):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0
        self.level = 1
        self.range = 100
        self.upgrade_cost = 0
        self.sell_cost = 0
        self.selected = False
        self.menu = None