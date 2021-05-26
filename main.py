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
pygame.mouse.set_visible(0)

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


def platform(pGroup, sGroup):
    ground = pygame.image.load("images/platform/platform.gif")
    stair = pygame.image.load("images/platform/stair.gif")

    # Main ground
    world.platformer(ground, x_pos=40, y_pos=515, loopControl=72, axs=True, group=pGroup)
    world.platformer(ground, x_pos=screenwidth / 2 - 50, y_pos=503, loopControl=7, axs=True, group=pGroup)
    # Left first ground
    world.platformer(ground, x_pos=45, y_pos=440, loopControl=12, axs=True, group=pGroup)
    # Right first ground
    world.platformer(ground, x_pos=646, y_pos=440, loopControl=11, axs=True, group=pGroup)
    # Left first stair
    world.platformer(stair, x_pos=100, y_pos=440, loopControl=5, axs=False, group=sGroup)
    # Right first stair
    world.platformer(stair, x_pos=700, y_pos=440, loopControl=5, axs=False, group=sGroup)
    # First left-main floor
    world.platformer(ground, x_pos=172, y_pos=436, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=189, y_pos=432, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=206, y_pos=428, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=223, y_pos=424, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=240, y_pos=420, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=257, y_pos=416, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=274, y_pos=412, loopControl=1, axs=True, group=pGroup)
    # First main floor
    world.platformer(ground, x_pos=291, y_pos=408, loopControl=23, axs=True, group=pGroup)
    # First right-main floor
    world.platformer(ground, x_pos=527, y_pos=412, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=544, y_pos=416, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=561, y_pos=420, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=578, y_pos=424, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=595, y_pos=428, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=612, y_pos=432, loopControl=1, axs=True, group=pGroup)
    world.platformer(ground, x_pos=629, y_pos=436, loopControl=1, axs=True, group=pGroup)
    # Second left-ground floor
    world.platformer(ground, x_pos=40, y_pos=315, loopControl=9, axs=True, group=pGroup)
    # Third left-ground floor
    world.platformer(ground, x_pos=40, y_pos=215, loopControl=9, axs=True, group=pGroup)
    # Fourth left-ground floor
    world.platformer(ground, x_pos=40, y_pos=100, loopControl=9, axs=True, group=pGroup)

platform(platformGroup, stairGroup)


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
        startMessage = font.render("game started", True, white)
        startMessagePos = startMessage.get_rect(centerx=background.get_width() / 2, centery=330)
        screen.blit(startMessage, startMessagePos)
        platformGroup.draw(screen)
        stairGroup.draw(screen)
        player.functions(platformGroup)
        player.move(event)
        player.draw(screen)

    pygame.display.flip()
pygame.quit()
quit()
