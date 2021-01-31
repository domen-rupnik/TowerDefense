import sys

import pygame

clock = pygame.time.Clock()

pygame.init()
class Login:
    def __init__(self, win):
        self.player = ""
        self.bg = pygame.transform.scale(pygame.image.load('login/bg.png'), (1350, 700))
        self.bg.get_rect().center = (675, 350)
        self.header = pygame.transform.scale(pygame.image.load('login/header_registration.png'), (236, 97))
        self.header.get_rect().center = (675, 205)
        self.rope1 = pygame.transform.scale(pygame.image.load('login/rope_big.png'), (40, 472))
        self.rope1.get_rect().center = (408, 22)
        self.rope2 = pygame.transform.scale(pygame.image.load('login/rope_big.png'), (40, 472))
        self.rope2.get_rect().center = (870, 22)
        self.create_btn = pygame.transform.scale(pygame.image.load('login/button_create.png'), (192, 103))
        self.create_btn.get_rect().center = (375, 503)
        self.table = pygame.transform.scale(pygame.image.load('login/window.png'), (524, 332))
        self.table.get_rect().center = (675, 350)
        self.name_bg = pygame.transform.scale(pygame.image.load('login/table_1.png'), (373, 50))
        self.header.get_rect().center = (675, 382)
        self.base_font = pygame.font.SysFont("comicsans", 65)
        # Polje: Insert name
        self.name_rect = pygame.Rect(395, 271, 280, 45)
        # Polje za vnos imena
        self.player_rect = pygame.Rect(320, 347, 355, 35)
        self.win = win

    def run(self):
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        try:
                            self.player = self.player[:-1]
                        finally:
                            pass
                    else:
                        self.player += event.unicode

                    if event.key == pygame.K_RETURN:
                        if self.player != "":
                            return self.player

                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    if 579 < x < 771 and 451 < y < 554:
                        if self.player != "":
                            return self.player
            self.draw()

    def draw(self):
        text_surface = self.base_font.render(self.player, True, (255, 255, 255))
        insert_text = self.base_font.render("Insert name", True, (255, 255, 255))
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.table, (431, 184))
        self.win.blit(self.header, (557, 156))
        self.win.blit(self.rope1, (460, -450))
        self.win.blit(self.rope2, (850, -450))
        self.win.blit(self.name_bg, (488, 357))
        self.win.blit(self.create_btn, (579, 451))

        self.win.blit(insert_text, (538, 293))
        self.win.blit(text_surface, (493, 362))

        pygame.display.update()
