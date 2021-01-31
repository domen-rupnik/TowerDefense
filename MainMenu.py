from game.Game import Game
import pygame
import os
from login.Login import Login
from leaderboard.LeaderBoard import LeaderBoard

# Dodamo start button, ozadje in logotip igre za začetni meni
start_button = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-gui/menu", "button_play.png")).convert_alpha(), (250, 250))
bg = pygame.image.load(os.path.join("game_assets/td-gui/menu", "bg.png"))
logo = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-gui/menu", "logo.png")), (500, 250))
music_on = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-gui/menu", "button_music.png")), (150, 150))
music_off = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-gui/menu", "button_music_off.png")), (150, 150))
sound_on = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-gui/menu", "button_sound.png")), (150, 150))
sound_off = pygame.transform.scale(pygame.image.load(os.path.join("game_assets/td-gui/menu", "button_sound_off.png")), (150, 150))
leaderboard = pygame.transform.scale(pygame.image.load("game_assets/td-gui/menu/button_menu.png"), (150, 150))
class MainMenu:
    def __init__(self, win):
        self.width = 1350
        self.height = 700
        self.bg = bg
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.btn = (self.width/2 - start_button.get_width()/2, 350, start_button.get_width(), start_button.get_height())
        self.play()
        self.music = True
        self.sound = True

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
                            igralec = Login(self.win).run()
                            game = Game(self.win, 0, self.music, self.sound, igralec)
                            game.run()
                            if self.music:
                                self.play()
                    if x > 50 and x < 200 and y > 50 and y < 200:
                        if self.music :
                            pygame.mixer.music.pause()
                        else :
                            pygame.mixer.music.unpause()
                            if not pygame.mixer.get_busy():
                                self.play()
                        self.music = not self.music
                    if x > 250 and x < 400 and y > 50 and y < 200:
                        self.sound = not self.sound
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if x > 1200 and x < 1350 and y > 50 and y < 200:
                        LeaderBoard(self.win).run()
            self.draw()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(logo, (self.width / 2 - logo.get_width() / 2, 90))
        self.win.blit(start_button, (self.btn[0], self.btn[1]))
        if self.music:
            self.win.blit(music_on, (50, 50))
        else:
            self.win.blit(music_off, (50, 50))
        if self.sound:
            self.win.blit(sound_on, (250, 50))
        else:
            self.win.blit(sound_off, (250, 50))
        self.win.blit(leaderboard, (1200, 50))
        pygame.display.update()
    def play(self):
        pygame.mixer.music.load("sounds/open_sound.wav")
        pygame.mixer.music.play(-1, 0)