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
    world.platformer(ground, x_pos=10, y_pos=580, loopControl=80, axs=True, group=pGroup)
    world.platformer(ground, x_pos=300, y_pos=565, loopControl=25, axs=True, group=pGroup)
    # Left first ground
    world.platformer(ground, x_pos=25, y_pos=380, loopControl=25, axs=True, group=pGroup)
    # Right first ground
    world.platformer(ground, x_pos=545, y_pos=380, loopControl=25, axs=True, group=pGroup)
    # Left first stair
    world.platformer(stair, x_pos=50, y_pos=380, loopControl=10, axs=False, group=sGroup)

    # print(world.platform_rect(screen, ground, x_pos=10, y_pos=580, loopControl=80, axs=True))


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
