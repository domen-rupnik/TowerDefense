import pygame

if __name__ == "__main__":
    pygame.mixer.init()
    pygame.init()
    pygame.display.set_caption('Tower Defence')
    pygame.display.set_icon(pygame.image.load('game_assets/archer-tower/39.png'))
    win = pygame.display.set_mode((1350, 700))
    from MainMenu import MainMenu
    mainMenu = MainMenu(win)
    mainMenu.run()