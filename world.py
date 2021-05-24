import pygame
from pygame.sprite import Sprite
from platformPiece import Platform

class World:
    def __init__(self):
        pass

    def platformer(self, image, x_pos, y_pos, loopControl, axs, group):
        control = 0
        if axs:
            self.stp = x_pos
            while control < loopControl:
                platform = Platform(image, self.stp, y_pos)
                group.add(platform)
                self.stp += 10
                control += 1
        else:
            self.stp = y_pos
            while control < loopControl:
                platform = Platform(image, x_pos, self.stp)
                group.add(platform)
                self.stp += 15
                control += 1

    """
            def platformer(self, screen, image, x_pos, y_pos, loopControl, axs):
      control = 0
      self.loopCntrl = loopControl
      self.stp = x_pos
      self.axis = axs

      if self.axis == True:
          while control < self.loopCntrl:
              imagePos = image.get_rect(centerx=self.stp, centery=y_pos)
              screen.blit(image, imagePos)
              self.stp = self.stp + 10
              control = control + 1
      else:
          self.stp = y_pos
          while control < self.loopCntrl:
              imagePos = image.get_rect(centerx=x_pos, centery=self.stp)
              screen.blit(image, imagePos)
              self.stp = self.stp + 15
              control = control + 1
        
    def platform_rect(self, screen, image, x_pos, y_pos, loopControl, axs):
      control = 0
      self.loopCntrl = loopControl
      self.stp = x_pos
      self.axis = axs
      rect_list = []
      if self.axis == True:
          while control < self.loopCntrl:
              imagePos = image.get_rect(centerx=self.stp, centery=y_pos)
              rect_list.append(imagePos)
              screen.blit(image, imagePos)
              self.stp = self.stp + 10
              control = control + 1
      else:
          self.stp = y_pos
          while control < self.loopCntrl:
              imagePos = image.get_rect(centerx=x_pos, centery=self.stp)
              rect_list.append(imagePos)
              screen.blit(image, imagePos)
              self.stp = self.stp + 15
              control = control + 1

      return rect_list
    """