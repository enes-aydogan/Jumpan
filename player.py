import pygame
from pygame.sprite import Sprite

class Player(Sprite):
      def __init__(self):
       scale = 1
       Sprite.__init__(self)
       self.image = pygame.image.load("images/jumpman/jumpman.gif")
       self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
       self.rect = self.image.get_rect()
       self.rect.x = 200
       self.rect.y = 200
       self.screenheight = pygame.display.get_surface().get_height()
       self.screenwidth = pygame.display.get_surface().get_width()
       self.jumping = False
       self.movex = 5
       self.movey = 5
       self.vel_x = 0
       self.vel_y = 2
       self.gravity = 1.2


      def move(self, event, platformGroup):
       if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
             if self.rect.x > 0:
                self.rect.x -= self.movex
                if pygame.sprite.spritecollide(self, platformGroup, False):
                    self.rect.x += self.movex

          if event.key == pygame.K_RIGHT:
             if self.rect.x < self.screenwidth - 32:
                self.rect.x += self.movex
                if pygame.sprite.spritecollide(self, platformGroup, False):
                    self.rect.x -= self.movex

          if self.jumping is False and event.key == pygame.K_LSHIFT:
             self.jumping = True

          if self.jumping == True:
             self.rect.y -= self.vel_y
             self.vel_y -= 1
             if self.vel_y < -(self.movey*2):
                self.jumping = False
                self.vel_y = (self.movey*2)

          if event.key == pygame.K_DOWN:
              if self.rect.y < 565:
                  self.rect.y += self.movey
                  if pygame.sprite.spritecollide(self, platformGroup, False):
                      self.rect.y -= self.movey

          if event.key == pygame.K_UP:
              if self.rect.y > 0:
                  self.rect.y -= self.movey
                  if pygame.sprite.spritecollide(self, platformGroup, False):
                      self.rect.y += self.movey



       def gravity (self):
           self.rect.y += 3.2
