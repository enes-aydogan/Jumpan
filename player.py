import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self):
       Sprite.__init__(self)
       self.image = pygame.image.load("images/player.gif")
       self.rect = self.image.get_rect()
       self.rect.x = 200
       self.rect.y = 100
       self.screenheight = pygame.display.get_surface().get_height()
       self.screenwidth = pygame.display.get_surface().get_width()

    def move(self, event):
       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
             if self.rect.x > 0:
                self.rect.x -= 10

          if event.key == pygame.K_RIGHT:
             if self.rect.x < self.screenwidth - 30:
                self.rect.x += 10

