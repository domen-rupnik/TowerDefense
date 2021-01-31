import math
import pygame
import numpy as np
import random
import os


class PlayGround(pygame.sprite.Sprite):
    def __init__(self, num):
        pygame.sprite.Sprite.__init__(self)
        self.background = pygame.Surface((1350, 700))
        self.background = pygame.transform.scale(pygame.image.load("playground/playground_" + str(num) + ".png").convert_alpha(), (1350, 700))
        self.rect = self.background.get_rect()
        self.path = []
        # Preberemo vse poti po katerih lahko potujejo monsterji
        lines = []
        st = 0
        with open('playground/paths_' + str(num)) as fp:
            dat = fp.read().splitlines()
            for i in dat:
                lines.append([])
                a = str(i).replace(" ", "").replace(", ", " ").replace("(", "").replace(")", "")
                a = a.split(";")
                for val in a:
                    xy = val.split(",")
                    lines[st].append((int(xy[0]), int(xy[1])))
                st += 1


        # Izračunamo točke na poti
        for j in lines:
            self.path.append([])
            for i in range(len(j[:-1])):
                x = int(j[i][0])
                y = int(j[i][1])

                x2 = int(j[i + 1][0])
                y2 = int(j[i + 1][1])

                # Izracunamo razdaljo med točkama
                d = int(math.sqrt(math.pow(x2 - x, 2) + math.pow(y2 - y, 2))) * 3
                xes = np.linspace(x, x2, d + 1)
                yes = np.linspace(y, y2, d + 1)
                path = []
                for i in range(d + 1):
                    path.append((int(xes[i]), int(yes[i])))
                self.path[-1].append(path)


