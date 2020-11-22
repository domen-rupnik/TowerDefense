import pygame


class Shop:
    def __init__(self, x, y, win, items):
        self.x = x
        self.y = y
        self.items = items
        self.bg = pygame.transform.scale(pygame.image.load("shop/bg.png"), (100, 300))
        self.width = self.bg.get_width()
        self.height = self.bg.get_height()
        self.font = pygame.font.SysFont("comicsans", 25)
        self.win = win
        self.clicked = None

    def draw(self):
        self.win.blit(self.bg, (self.x, self.y))
        for item in self.items:
            self.win.blit(item.bg, (item.x, item.y))

    # Če pritisnemo na ShopItem, vrnemo True
    def is_clicked(self, x, y):
        for item in self.items:
            if x > item.x and x < item.x:
                if y > item.y and y < item.y:
                    self.clicked = item
                    return True
        self.clicked = None
        return False
    # Vrnemo pritisnjenega
    def get_clicked(self):
        return self.clicked