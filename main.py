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


def initial_Screen():
    title = titleFont.render("JUMPMAN", True, (77, 166, 48))
    titlePos = title.get_rect(centerx=background.get_width() / 2, centery=250)
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
        player.move(event)
        allSprites.draw(screen)

    pygame.display.flip()
pygame.quit()
quit()