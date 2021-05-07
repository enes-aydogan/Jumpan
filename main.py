import sys
import pygame

# Initialize pygame
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

# Create screen
screen = pygame.display.set_mode((800,600))

# Title of the game window
pygame.display.set_caption('Jumpman V1.0')

# Font
font = pygame.font.Font("font/RetroGaming.ttf", 20)
titleFont = pygame.font.Font("font/RetroGaming.ttf", 90)
authorFont = pygame.font.Font(None, 18)

# Surface
background = pygame.Surface(screen.get_size())

# Clock to limit speed
clock = pygame.time.Clock()

def initial_Screen():
    title = titleFont.render("JUMPMAN", True, (77,166,48))
    titlePos = title.get_rect(centerx=background.get_width() / 2, centery=250)
    screen.blit(title, titlePos)


exit_program = False
initial_screen = True

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

    pygame.display.flip()
pygame.quit()
quit()