import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pygame.image.load("images/platform/bullet.png")
        self.rect = self.image.get_rect()
        self.fireSound = pygame.mixer.Sound("sounds/fireSound.wav")
        self.rect.x = 20
        self.rect.y = 20
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.movex = 2
        self.movey = 2

    def bullet(self, playerX, playerY):
        if self.rect.x < 802:
            self.rect.x += self.movex
            self.fireSound.play(0)
            if self.rect.x - 16 == playerX:
                self.fireSound.play(0)
                print("done")
                self.rect.x -= self.movey
                self.rect.y += self.movey
