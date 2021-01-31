import pygame

clock = pygame.time.Clock()
class Pause:
    def __init__(self, win):
        self.win = win
        self.unpause = pygame.transform.scale(pygame.image.load('game_assets/td-gui/menu/button_play.png'), (200, 200))
        pygame.mixer.music.pause()

    def run(self):
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if 575 < x < 775 and 250 < y < 450:
                        return
            self.draw()

    def draw(self):
        self.win.blit(self.unpause, (575, 250))
        pygame.display.update()