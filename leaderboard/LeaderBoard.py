import sys

import pygame

clock = pygame.time.Clock()

pygame.init()
class LeaderBoard:
    def __init__(self, win):
        self.bg = pygame.transform.scale(pygame.image.load('leaderboard/bg.png'), (1350, 700))
        self.rope1 = pygame.transform.scale(pygame.image.load('leaderboard/rope_big.png'), (40, 472))
        self.rope2 = pygame.transform.scale(pygame.image.load('leaderboard/rope_big.png'), (40, 472))
        self.table = pygame.transform.scale(pygame.image.load('leaderboard/window.png'), (524, 332))
        self.name_bg = pygame.transform.scale(pygame.image.load('leaderboard/table_1.png'), (373, 50))
        self.score_bg = pygame.transform.scale(pygame.image.load('leaderboard/table_1.png'), (115, 50))
        self.close = pygame.transform.scale(pygame.image.load('leaderboard/button_close.png'), (63, 63))
        self.font = pygame.font.SysFont("comicsans", 65)

        self.scores = []
        self.win = win

        with open('results.txt', 'r') as f:
            for i in f.readlines():
                i = i.strip()
                self.scores.append((i.split(':')))
        for i in range(len(self.scores)):
            if not self.scores[i][1].isdigit():
                break
            self.scores[i][1] = int(self.scores[i][1])
        self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)[:3]

    def run(self):
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    if x > 880 and x < 943 and y > 165 and y < 228:
                        return
            self.draw()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.table, (431, 184))
        self.win.blit(self.rope1, (460, -245))
        self.win.blit(self.rope2, (850, -245))
        self.win.blit(self.close, (880, 165))

        self.win.blit(self.name_bg, (490, 205))

        self.win.blit(self.font.render('Leaderboard', True, (255,255,255)), (530, 208))

        for i in range(len(self.scores)):
            self.win.blit(self.name_bg, (487, 270 + (i * 80)))
            self.win.blit(self.score_bg, (777, 270 + (i * 80)))
            self.win.blit(self.font.render(self.scores[i][0], True, (255, 255, 255)), (493, 275 + (i * 80)))
            self.win.blit(self.font.render(str(self.scores[i][1]), True, (255, 255, 255)), (783, 275 + (i * 80)))

        pygame.display.update()
