from game.Game import Game
import pygame
import os

# Dodamo start button, ozadje in logotip igre za začetni meni
start_button = pygame.image.load(os.path.join("game_assets/td-gui/menu", "button_play.png")).convert_alpha()
bg = pygame.image.load(os.path.join("game_assets/td-gui/menu", "bg.png"))
logo = pygame.image.load(os.path.join("game_assets/td-gui/menu", "logo.png"))

class MainMenu:
    def __init__(self, win):
        self.width = 1350
        self.height = 700
        self.bg = bg
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.btn = (self.width/2 - start_button.get_width()/2, 350, start_button.get_width(), start_button.get_height())

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                # Izhod iz programa, če pritisnemo križec
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # check if hit start btn
                    x, y = pygame.mouse.get_pos()

                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Game(self.win, 0)
                            game.run()
                            del game
            self.draw()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(logo, (self.width / 2 - logo.get_width() / 2, 0))
        self.win.blit(start_button, (self.btn[0], self.btn[1]))
        pygame.display.update()