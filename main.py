import sys
import pygame

#initilize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((800,600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    pygame.display.update()
