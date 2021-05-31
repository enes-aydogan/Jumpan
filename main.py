import sys
import pygame
from player import Player
from world import World
import platformPiece

print(platformPiece.__file__)

black = (0, 0, 0)
white = (255, 255, 255)

# Initialize pygame
pygame.init()

# Create screen
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))

# Title of the game window
pygame.display.set_caption('Jumpman V1.0')

# mouse disappear
#pygame.mouse.set_visible(0)

# Font
font = pygame.font.Font("font/RetroGaming.ttf", 20)
titleFont = pygame.font.Font("font/RetroGaming.ttf", 90)
authorFont = pygame.font.Font(None, 18)

# Surface
background = pygame.Surface(screen.get_size())

# Sprite Groups
allSprites = pygame.sprite.Group()

# Assignment
player = Player()
world = World()
# rect_list = world.platform_rect()

# Clock to limit speed
clock = pygame.time.Clock()

# Game status checking
run = True
initial_screen = True

platformGroup = pygame.sprite.Group()
stairGroup = pygame.sprite.Group()
rampGroupU = pygame.sprite.Group()

def platform(pGroup, sGroup, rGroupU):
    ground = pygame.image.load("images/platform/platform.gif")
    ground = pygame.transform.scale(ground, (int(ground.get_width() * 0.5), int(ground.get_height() * 0.5)))
    stair = pygame.image.load("images/platform/stair.gif")
    ivy = pygame.image.load("images/platform/ivy.gif")
    coin = pygame.image.load("images/platform/point.gif")

    # Main ground
    world.platformer(ground, x_pos=40, y_pos=515, loopControl=72, axs=True, group=pGroup)
    world.platformer(ground, x_pos=screenwidth / 2 - 50, y_pos=503, loopControl=7, axs=True, group=pGroup)
    # Left first ground
    world.platformer(ground, x_pos=45, y_pos=440, loopControl=11, axs=True, group=pGroup)
    # Right first ground
    world.platformer(ground, x_pos=636, y_pos=440, loopControl=11, axs=True, group=pGroup)
    # Left first stair
    world.platformer(stair, x_pos=100, y_pos=440, loopControl=5, axs=False, group=sGroup)
    # Right first stair
    world.platformer(stair, x_pos=680, y_pos=440, loopControl=5, axs=False, group=sGroup)
    # First left-main floor
    world.platformer(ground, x_pos=162, y_pos=436, loopControl=1, axs=True, group=rGroupU)
    world.platformer(ground, x_pos=179, y_pos=432, loopControl=1, axs=True, group=rGroupU)
    world.platformer(ground, x_pos=196, y_pos=428, loopControl=1, axs=True, group=rGroupU)
    world.platformer(ground, x_pos=213, y_pos=424, loopControl=1, axs=True, group=rGroupU)
    world.platformer(ground, x_pos=230, y_pos=420, loopControl=1, axs=True, group=rGroupU)
    world.platformer(ground, x_pos=247, y_pos=416, loopControl=1, axs=True, group=rGroupU)
    world.platformer(ground, x_pos=264, y_pos=412, loopControl=1, axs=True, group=rGroupU)
    # First main floor
    world.platformer(ground, x_pos=281, y_pos=408, loopControl=23, axs=True, group=pGroup)
    # First right-main floor
    world.platformer(ground, x_pos=517, y_pos=412, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=534, y_pos=416, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=551, y_pos=420, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=568, y_pos=424, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=585, y_pos=428, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=602, y_pos=432, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=619, y_pos=436, loopControl=1, axs=True, group=pGroup)
    # Second left-ground floor
    world.platformer(ground, x_pos=40, y_pos=315, loopControl=9, axs=True, group=pGroup)
    # Third left-ground floor
    world.platformer(ground, x_pos=40, y_pos=215, loopControl=9, axs=True, group=pGroup)
    # Fourth left-ground floor
    world.platformer(ground, x_pos=40, y_pos=100, loopControl=9, axs=True, group=pGroup)
    world.platformer(ground, x_pos=137, y_pos=104, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=154, y_pos=108, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=171, y_pos=104, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=188, y_pos=100, loopControl=11, axs=True, group=pGroup)
    world.platformer(ground, x_pos=305, y_pos=96, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=322, y_pos=92, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=339, y_pos=88, loopControl=1, axs=True, group=pGroup)
    # Fourth right-ground floor
    world.platformer(ground, x_pos=646, y_pos=100, loopControl=9, axs=True, group=pGroup)
    world.platformer(ground, x_pos=629, y_pos=104, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=612, y_pos=108, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=595, y_pos=104, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=478, y_pos=100, loopControl=11, axs=True, group=pGroup)
    world.platformer(ground, x_pos=461, y_pos=96, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=444, y_pos=92, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=427, y_pos=88, loopControl=1, axs=True, group=pGroup)
    # Right third-ground floor
    world.platformer(ground, x_pos=656, y_pos=315, loopControl=9, axs=True, group=pGroup)
    # Right second-ground floor
    world.platformer(ground, x_pos=656, y_pos=215, loopControl=9, axs=True, group=pGroup)
    # Third main-ground floor
    world.platformer(ground, x_pos=281, y_pos=315, loopControl=23, axs=True, group=pGroup)
    # Third left-piece ground
    world.platformer(ground, x_pos=194 , y_pos=315, loopControl=3, axs=True, group=pGroup)
    # Third right-piece ground
    world.platformer(ground, x_pos=568 , y_pos=315, loopControl=3, axs=True, group=pGroup)
    # Third main floor
    world.platformer(ground, x_pos=205 , y_pos= 200, loopControl=7, axs=True, group=pGroup)
    world.platformer(ground, x_pos=281 , y_pos=204, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=298 , y_pos=208, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=315 , y_pos=212, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=332 , y_pos=216, loopControl=12, axs=True, group=pGroup)
    world.platformer(ground, x_pos=459, y_pos=212, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=476, y_pos=208, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=493, y_pos=204, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=510, y_pos=200, loopControl=7, axs=True, group=pGroup)
    # First main ground-stair
    world.platformer(stair, x_pos=306, y_pos=311, loopControl=6, axs=False, group=sGroup)
    world.platformer(stair, x_pos=477, y_pos=311, loopControl=6, axs=False, group=sGroup)
    world.platformer(stair, x_pos=390, y_pos=218, loopControl=6, axs=False, group=sGroup)
    # Left Last stair
    world.platformer(stair, x_pos=95, y_pos=90, loopControl=16, axs=False, group=sGroup)
    world.platformer(stair, x_pos=230, y_pos=103, loopControl=6, axs=False, group=sGroup)
    # Right last stair
    world.platformer(stair, x_pos=680, y_pos=90, loopControl=16, axs=False, group=sGroup)
    world.platformer(stair, x_pos=540, y_pos=103, loopControl=6, axs=False, group=sGroup)
    # Left IVY
    world.platformer(ivy, x_pos=207, y_pos=337, loopControl=2, axs=False, group=sGroup)
    # Rigth IVY
    world.platformer(ivy, x_pos=575, y_pos=337, loopControl=2, axs=False, group=sGroup)
    # Coins
    world.platformer(coin, x_pos=40, y_pos=85, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=40, y_pos=175, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=40, y_pos=500, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=315, y_pos=450, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=450, y_pos=450, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=750, y_pos=500, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=725, y_pos=175, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=725, y_pos=85, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=425, y_pos=74, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=340, y_pos=74, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=200, y_pos=275, loopControl=1, axs=False, group=sGroup)
    world.platformer(coin, x_pos=585, y_pos=275, loopControl=1, axs=False, group=sGroup)


platform(platformGroup, stairGroup, rampGroupU)


def initial_Screen():
    title = titleFont.render("JUMPMAN", True, (77, 166, 48))
    titlePos = title.get_rect(centerx=background.get_width() / 2, centery=250)
    screen.blit(title, titlePos)

    startMessage = font.render("press any key to start", True, white)
    startMessagePos = startMessage.get_rect(centerx=background.get_width() / 2, centery=330)
    screen.blit(startMessage, startMessagePos)

    author = authorFont.render("Authors: Muhammet Enes Aydoğan and Hilmi Can Taşkıran", True, white)
    authorPos = author.get_rect(centerx=background.get_width() / 2, centery=575)
    screen.blit(author, authorPos)


# Main program loop
while run:
    # Limit to 30 fps
    clock.tick(30)
    # Clear the screen
    screen.fill(black)
    # Process the events in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            initial_screen = False

    if initial_screen:
        initial_Screen()
    else:
        platformGroup.draw(screen)
        rampGroupU.draw(screen)
        stairGroup.draw(screen)
        player.functions(platformGroup, stairGroup, rampGroupU)
        player.move(event)
        player.gravity(platformGroup, rampGroupU)
        player.draw(screen)

    pygame.display.flip()
pygame.quit()
quit()
