import pygame
from Settings import *

def Draw_Grid(size):
    Xmax, Ymax = round(screen_w/ size), round(screen_h/ size)
    for i in range (0, Xmax):
        for k in range (0,  Ymax):
            pygame.draw.rect(screen, "purple", ( i * size, k * size, size - 2, size -2 ))

class Map():
    def __init__(self):
        self.screen = pygame.display.get_surface()
        Tiles_Map['3;3'] = [3, 3, "Grey"]
        Tiles_Map['4;3'] = [4, 3, "Black"]
        Tiles_Map['3;4'] = [3, 4, "Grey"]
        Tiles_Map['4;4'] = [4, 4, "Black"]
    def Draw(self, size):
        for i in Tiles_Map:
            pygame.draw.rect(self.screen, Tiles_Map[i][2], (Tiles_Map[i][0] * size, Tiles_Map[i][1] * size, size, size))
