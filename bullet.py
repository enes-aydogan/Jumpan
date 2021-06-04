import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        pass


    def bullet(self, screen, white):
        pygame.draw.rect(screen, white, pygame.Rect(30, 30, 3, 2))