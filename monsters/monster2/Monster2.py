import pygame
class Monster2(pygame.sprite.Sprite):
    def __init__(self, win):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64, 64))
        self.images_left = []
        self.images_right = []
        for i in range(20):
            self.images_left.append(pygame.transform.scale(pygame.transform.flip(pygame.image.load("monsters/monster2/" + str(i + 1) + ".png"), True, False), (64, 64)))
            self.images_right.append(pygame.transform.scale(pygame.image.load("monsters/monster2/" + str(i + 1) + ".png"), (64, 64)))

        self.walk_count = 0
        self.x = 0
        self.y = 0
        self.path = []
        self.win = win
        self.left = False
        self.walk_number = 0
        self.image_number = 0
        self.previous_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def set_path(self, path, st):
        for i in range(st * 200):
            self.path.append((-100, -100))
        for i in path:
            for j in i:
                self.path.append(j)

    def walk(self):
        self.x, self.y = self.path[self.walk_count]
        self.walk_count += 3
        self.walk_number += 1
        if sum(self.previous_x)/len(self.previous_x) <= self.x:
            self.left = False
        else:
            self.left = True
        self.previous_x.append(self.x)
        self.previous_x = self.previous_x[1:]

    def draw(self):
        # Na vsakih pet main loope prikažemo novo sliko
        if self.walk_number > 5:
            self.walk_number = 0
            self.image_number += 1

        # Imamo samo 10 slik za hojo enega monsterja
        if self.image_number >= len(self.images_right):
            self.image_number = 0

        # Če se premika levo ali desno izberemo sliko iz primerne tabele slik
        if self.left:
            self.win.blit(self.images_left[self.image_number], (self.x - 50, self.y - 32))
        else:
            self.win.blit(self.images_right[self.image_number], (self.x - 32, self.y - 32))

    def finished(self):
        if len(self.path) <= self.walk_count:
            return True
        return False