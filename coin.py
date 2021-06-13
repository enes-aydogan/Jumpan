import pygame
from pygame.sprite import Sprite


class Coin(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = pygame.image.load("images/platform/point.gif")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
