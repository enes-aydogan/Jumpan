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
