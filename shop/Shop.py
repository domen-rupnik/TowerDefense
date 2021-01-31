import pygame


class Shop:
    def __init__(self, x, y, win, items):
        self.x = x
        self.y = y
        self.items = items
        self.bg = pygame.transform.scale(pygame.image.load("shop/bg.png"), (100, 310))
        self.star = pygame.transform.scale(pygame.image.load("game_assets/td-gui/upgrade/star.png"), (20, 20))
        self.width = self.bg.get_width()
        self.height = self.bg.get_height()
        self.font = pygame.font.SysFont("comicsans", 25)
        self.win = win
        self.clicked = None

    def draw(self):
        self.win.blit(self.bg, (self.x, self.y))
        for item in self.items:
            self.win.blit(item.bg, (item.x, item.y))
            self.win.blit(self.star, (item.x + 5, item.y + 73))
            costText = self.font.render(str(item.item_cost), True, (255, 255, 255))
            costRect = costText.get_rect()
            costRect.center = (item.x + 40, item.y + 83)
            self.win.blit(costText, costRect)

    # Če pritisnemo na ShopItem, vrnemo True
    def is_clicked(self, x, y):
        for item in self.items:
            if x > item.x and x < item.x + 80:
                if y > item.y and y < item.y + 80:
                    self.clicked = item
                    return True
        self.clicked = None
        return False

    # Vrnemo pritisnjenega
    def get_clicked(self):
        return self.clicked

    def unclick(self):
        self.clicked = False