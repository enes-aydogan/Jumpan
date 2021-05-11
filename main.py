import sys
import pygame
from player import Player

black = (0, 0, 0)
white = (255, 255, 255)

# Initialize pygame
pygame.init()

# Create screen
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth,screenheight))

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
allSprites.add(player)

# Clock to limit speed
clock = pygame.time.Clock()

# Game status checking
exit_program = False
initial_screen = True
def platformer(screen, image, x_pos, y_pos, loopControl, axs):
    control = 0
    loopCntrl = loopControl
    stp = x_pos
    axis = axs
    if axis == True:
        while control < loopCntrl:
            imagePos = image.get_rect(centerx=stp, centery=y_pos)
            screen.blit(image, imagePos)
            stp = stp + 10
            control = control + 1
    else:
        stp = y_pos
        while control < loopCntrl:
            imagePos = image.get_rect(centerx=x_pos, centery=stp)
            screen.blit(image, imagePos)
            stp = stp + 15
            control = control + 1

def platform(screen):
    ground = pygame.image.load("images/platform/platform.gif")
    stair = pygame.image.load("images/platform/stair.gif")

    # Main ground
    platformer(screen, ground, x_pos = 10, y_pos=580, loopControl=80, axs=True)
    platformer(screen, ground, x_pos = 300, y_pos=565, loopControl=25, axs=True)
    # Left first ground
    platformer(screen, ground, x_pos = 25, y_pos=380, loopControl=25, axs=True)
    # Right first ground
    platformer(screen, ground, x_pos = 545, y_pos=380, loopControl=25, axs=True)
    # Left first stair
    platformer(screen, stair, x_pos = 50, y_pos=395, loopControl=10, axs=False)

    """"
    control = 0
    base = 10
    while control < 80:
        platform = pygame.image.load("images/platform/platform.gif")
        platformPos = platform.get_rect(centerx=base, centery=580)
        screen.blit(platform, platformPos)
        base = base + 10
        control = control + 1
    control = 0
    base = 300
    while control < 25:
        platform = pygame.image.load("images/platform/platform.gif")
        platformPos = platform.get_rect(centerx=base, centery=567)
        screen.blit(platform, platformPos)
        base = base + 10
        control = control + 1
    """
def initial_Screen():
    title = titleFont.render("JUMPMAN", True, (77, 166, 48))
    titlePos = title.get_rect(centerx=background.get_width() / 2, centery=500)
    screen.blit(title, titlePos)

    startMessage = font.render("press any key to start", True, white)
    startMessagePos = startMessage.get_rect(centerx=background.get_width() / 2, centery=330)
    screen.blit(startMessage, startMessagePos)

    author = authorFont.render("This game completely codded by Muhammet Enes Aydoğan and Hilmi Can Taşkıran", True, white)
    authorPos = author.get_rect(centerx=background.get_width() - author.get_width() / 2 - 10,
                                centery=background.get_height() - author.get_height() / 2 - 10)
    screen.blit(author, authorPos)


# Main program loop
while not exit_program:
    # Limit to 30 fps
    clock.tick(70)
    # Clear the screen
    screen.fill(black)
    # Process the events in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_program = True
            initial_screen = False

    if initial_screen:
        initial_Screen()
    else:
        startMessage = font.render("game started", True, white)
        startMessagePos = startMessage.get_rect(centerx=background.get_width() / 2, centery=330)
        screen.blit(startMessage, startMessagePos)
        platform(screen)
        player.move(event)
        allSprites.draw(screen)

    pygame.display.flip()
pygame.quit()
quit()