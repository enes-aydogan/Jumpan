import sys
import pygame
from player import Player
import platformPiece
from bullet import Bullet
from secondBullet import SecondBullet
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
authorFont = pygame.font.Font(None, 22)

# Surface
background = pygame.Surface(screen.get_size())

# Sprite Groups
allSprites = pygame.sprite.Group()

# Assignment
player = Player()
bullet = Bullet()
secondBullet = SecondBullet()
levels = Levels()
world = World()
allSprites.add(bullet)
allSprites.add(secondBullet)
# rect_list = world.platform_rect()
jumpman = pygame.image.load("images/jumpman/jumpman.gif")
jumpman = pygame.transform.scale(jumpman, (int(jumpman.get_width() * 1.2), int(jumpman.get_height() * 1.2)))
jumpman_position = [60, 100, 140, 180, 220]

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
    gameOver = titleFont.render("Game Over", True, white)
    gameOverPos = gameOver.get_rect(centerx=background.get_width() / 2, centery=250)
    screen.blit(gameOver, gameOverPos)

    point = font.render("Point: " + str(game_point), True, white)
    pointPos = point.get_rect(centerx=background.get_width() / 2, centery=350)
    screen.blit(point, pointPos)

    press = font.render("Press Enter to restart", True, white)
    pressPos = press.get_rect(centerx=background.get_width() / 2, centery=500)
    screen.blit(press, pressPos)


def game_win_screen():
    gameWin = titleFont.render("Game Win", True, white)
    gameWinPos = gameWin.get_rect(centerx=background.get_width() / 2, centery=250)
    screen.blit(gameWin, gameWinPos)

    point = font.render("Point: " + str(game_point), True, white)
    pointPos = point.get_rect(centerx=background.get_width() / 2, centery=350)
    screen.blit(point, pointPos)

    press = font.render("Press Enter to restart", True, white)
    pressPos = press.get_rect(centerx=background.get_width() / 2, centery=500)
    screen.blit(press, pressPos)


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
gameWin = False
alive = 5
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
        if not (gameFinished or gameWin):
            pointMessage = font.render("Point: ", True, white)
            pointMessagePos = pointMessage.get_rect(centerx=650, centery=560)
            screen.blit(pointMessage, pointMessagePos)
            point = font.render(str(player.point), True, white)
            pointPos = point.get_rect(centerx=725, centery=560)
            screen.blit(point, pointPos)
            level = font.render("Level: " + str(player.level) + "/3", True, white)
            levelPos = level.get_rect(centerx=525, centery=560)
            screen.blit(level, levelPos)
            for position in jumpman_position[0:alive]:
                jumpmanPos = jumpman.get_rect(centerx=position, centery=550)
                screen.blit(jumpman, jumpmanPos)

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
                    bullet.rect.x += bullet.movex
                    if bullet.rect.x - 15 == player.rect.x:
                        bullet.moveOnlyY = True

                    if bullet.moveOnlyY:
                        bullet.rect.x -= bullet.movey
                        bullet.rect.y += bullet.movey + 3

                    if bullet.rect.x == (bullet.rect.x - bullet.movey):
                        bullet.moveOnlyY = False

                elif bullet.rect.x > 801 or bullet.rect.y > 601:
                    bullet = Bullet()
                    allSprites.add(bullet)
                    bullet.rect.x += bullet.movex
                    if bullet.rect.x - 16 == player.rect.x:
                        bullet.moveOnlyY = True

                    if bullet.moveOnlyY:
                        bullet.rect.x -= bullet.movey
                        bullet.rect.y += bullet.movey

                    if bullet.rect.x == (bullet.rect.x - bullet.movey):
                        bullet.moveOnlyY = False


            else:
                alive -= 1
                game_point = player.point
                resetLevel()
                if player.level == 1:
                    levels.level1(world, platformGroup, stairGroup, rampGroupU, rampGroupD, bottomPlatform, coinGroup)
                elif player.level == 2:
                    levels.level2(world, platformGroup, stairGroup, bottomPlatform, coinGroup)
                elif player.level == 3:
                    levels.level3(world, platformGroup, stairGroup, rampGroupU, rampGroupD, bottomPlatform, coinGroup)

                allSprites.empty()
                player = Player()
                bullet = Bullet()
                allSprites.add(bullet)
                secondBullet = SecondBullet()
                allSprites.add(secondBullet)
                gameFinished = False
                if alive == 0:
                    gameFinished = True

            if not secondBullet.rect.colliderect(player.rect):
                if secondBullet.rect.x < 802 and secondBullet.rect.y < 602:
                    secondBullet.rect.y += secondBullet.movey
                    if secondBullet.rect.y - 15 == player.rect.y:
                        secondBullet.moveOnlyY = True

                    if secondBullet.moveOnlyY:
                        secondBullet.rect.y -= secondBullet.movey
                        secondBullet.rect.x += secondBullet.movex

                    if secondBullet.rect.y == (secondBullet.rect.y - secondBullet.movey):
                        secondBullet.moveOnlyY = False

                elif secondBullet.rect.x > 801 or secondBullet.rect.y > 601:
                    secondBullet = SecondBullet()
                    allSprites.add(secondBullet)
                    secondBullet.rect.x += secondBullet.movex
                    if secondBullet.rect.x - 15 == player.rect.x:
                        secondBullet.moveOnlyY = True

                    if secondBullet.moveOnlyY:
                        secondBullet.rect.x -= secondBullet.movey
                        secondBullet.rect.y += secondBullet.movey + 3

                    if secondBullet.rect.x == (secondBullet.rect.x - secondBullet.movey):
                        secondBullet.moveOnlyY = False

            else:
                alive -= 1
                game_point = player.point
                resetLevel()
                if player.level == 1:
                    levels.level1(world, platformGroup, stairGroup, rampGroupU, rampGroupD, bottomPlatform, coinGroup)
                elif player.level == 2:
                    levels.level2(world, platformGroup, stairGroup, bottomPlatform, coinGroup)
                elif player.level == 3:
                    levels.level3(world, platformGroup, stairGroup, rampGroupU, rampGroupD, bottomPlatform, coinGroup)
                allSprites.empty()
                player = Player()
                bullet = Bullet()
                allSprites.add(bullet)
                secondBullet = SecondBullet()
                allSprites.add(secondBullet)
                gameFinished = False
                if alive == 0:
                    gameFinished = True

            # levels.level1coin(screen, player.rect.x, player.rect.y, player.rect.w, player.rect.h)
            if player.levelChange:
                resetLevel()
                if player.level == 2:
                    allSprites.empty()
                    bullet = Bullet()
                    allSprites.add(bullet)
                    secondBullet = SecondBullet()
                    allSprites.add(secondBullet)
                    levels.level2(world, platformGroup, stairGroup, bottomPlatform, coinGroup)
                    pygame.time.delay(delay * 500)
                elif player.level == 3:
                    allSprites.empty()
                    bullet = Bullet()
                    allSprites.add(bullet)
                    secondBullet = SecondBullet()
                    allSprites.add(secondBullet)
                    levels.level3(world, platformGroup, stairGroup, rampGroupU, rampGroupD, bottomPlatform, coinGroup)
                    pygame.time.delay(delay * 500)
                elif player.level == 4:
                    gameWin = True
                else:
                    gameFinished = True

                player.levelChange = False

        if gameFinished:
            game_finished_screen()
            resetLevel()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    alive = 5
                    levels.level1(world, platformGroup, stairGroup, rampGroupU, rampGroupD, bottomPlatform, coinGroup)
                    allSprites.empty()
                    player = Player()
                    bullet = Bullet()
                    secondBullet = SecondBullet()
                    allSprites.add(secondBullet)
                    allSprites.add(bullet)
                    gameFinished = False
        if gameWin:
            game_win_screen()
            resetLevel()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    alive = 5
                    levels.level1(world, platformGroup, stairGroup, rampGroupU, rampGroupD, bottomPlatform, coinGroup)
                    allSprites.empty()
                    player = Player()
                    bullet = Bullet()
                    allSprites.add(bullet)
                    secondBullet = SecondBullet()
                    allSprites.add(secondBullet)
                    gameFinished = False
                    gameWin = False
    pygame.display.flip()
pygame.quit()
quit()
