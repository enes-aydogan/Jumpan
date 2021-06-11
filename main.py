import sys
import pygame
from player import Player
import platformPiece
from bullet import Bullet
from levels import Levels
from world import World

print(platformPiece.__file__)

black = (0, 0, 0)
white = (255, 255, 255)

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Create screen
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))

# Title of the game window
pygame.display.set_caption('Jumpman V1.0')

# mouse disappear
# pygame.mouse.set_visible(0)

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
bullet = Bullet()
levels = Levels()
world = World()
allSprites.add(bullet)
# rect_list = world.platform_rect()

# Clock to limit speed
clock = pygame.time.Clock()

# Game status checking
run = True
initial_screen = True

platformGroup = pygame.sprite.Group()
stairGroup = pygame.sprite.Group()
rampGroupU = pygame.sprite.Group()
rampGroupD = pygame.sprite.Group()
coinGroup = pygame.sprite.Group()
bottomPlatform = pygame.sprite.Group()

mainSound = pygame.mixer.Sound("sounds/main.wav")
mainSound.play(0)

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

def game_finished_screen():
    startMessage = font.render("Game Over", True, white)
    startMessagePos = startMessage.get_rect(centerx=background.get_width() / 2, centery=330)
    screen.blit(startMessage, startMessagePos)


def resetLevel():
    global platformGroup
    global stairGroup
    global rampGroupU
    global rampGroupD
    global coinGroup
    global bottomPlatform

    platformGroup = pygame.sprite.Group()
    stairGroup = pygame.sprite.Group()
    rampGroupU = pygame.sprite.Group()
    rampGroupD = pygame.sprite.Group()
    coinGroup = pygame.sprite.Group()
    bottomPlatform = pygame.sprite.Group()



levels.level1(world, platformGroup, stairGroup, rampGroupU, rampGroupD, bottomPlatform, coinGroup)
gameFinished = False
delay = 1
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


            if not initial_screen:
                mainSound.stop()

    if initial_screen:
        initial_Screen()
    else:
        if not gameFinished:
            point = font.render("Point: " + str(player.point), True, white)
            pointPos = point.get_rect(centerx=600, centery=550)
            screen.blit(point, pointPos)
            level = font.render("Level - " + str(player.level) + "/3", True, white)
            levelPos = level.get_rect(centerx=600, centery=575)
            screen.blit(level, levelPos)
            platformGroup.draw(screen)
            rampGroupU.draw(screen)
            rampGroupD.draw(screen)
            bottomPlatform.draw(screen)
            stairGroup.draw(screen)
            allSprites.draw(screen)
            player.draw(screen)
            coinGroup.draw(screen)
            player.move(event)
            player.functions(platformGroup, stairGroup, rampGroupU, rampGroupD, screen, bottomPlatform, coinGroup)
            player.gravity(platformGroup, rampGroupU, rampGroupD, bottomPlatform)

            if not bullet.rect.colliderect(player.rect):
                if bullet.rect.x < 802 and bullet.rect.y < 602:
                    bullet.list.append(bullet.rect.x)
                    bullet.rect.x += bullet.movex
                    if bullet.rect.x - 16 == player.rect.x:
                        bullet.moveOnlyY = True

                    if bullet.moveOnlyY:
                        bullet.rect.x -= bullet.movey
                        bullet.rect.y += bullet.movey

                    if bullet.rect.x == (bullet.rect.x - bullet.movey):
                        bullet.moveOnlyY = False
            else:
                gameFinished = True

            # levels.level1coin(screen, player.rect.x, player.rect.y, player.rect.w, player.rect.h)
            if player.levelChange:
                resetLevel()
                if player.level == 2:
                    levels.level2(world, platformGroup, stairGroup, bottomPlatform, coinGroup)
                    pygame.time.delay(delay * 500)
                elif player.level == 3:
                    levels.level3(world, platformGroup, stairGroup, rampGroupU, rampGroupD, bottomPlatform, coinGroup)
                    pygame.time.delay(delay * 500)
                else:
                    gameFinished = True

                player.levelChange = False

        else:
            game_finished_screen()

    pygame.display.flip()
pygame.quit()
quit()
