import pygame
from pygame.sprite import Sprite


class platformPiece(Sprite):
    def __init__(self, image, x, y):
        Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
