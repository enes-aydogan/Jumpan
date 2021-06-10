import pygame
from coin import Coin


class Levels():
    def __init__(self):
        self.coinImage = pygame.image.load("images/platform/point.gif")
        self.ground = pygame.image.load("images/platform/newplatform.png")
        self.ground = pygame.transform.scale(self.ground,
                                             (int(self.ground.get_width() * 0.5), int(self.ground.get_height() * 0.5)))
        self.stair = pygame.image.load("images/platform/stair.gif")
        self.ivy = pygame.image.load("images/platform/ivy.gif")

        self.totalCoin = 0

    def level1(self, world, pGroup, sGroup, rGroupU, rGroupD, bottomPlatform, coinGroup):
        # Main ground
        world.platformer(self.ground, x_pos=40, y_pos=515, loopControl=72, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=800 / 2 - 50, y_pos=503, loopControl=7, axs=True, group=pGroup)
        # Left first ground
        world.platformer(self.ground, x_pos=45, y_pos=440, loopControl=11, axs=True, group=pGroup)
        # Right first ground
        world.platformer(self.ground, x_pos=636, y_pos=440, loopControl=11, axs=True, group=pGroup)
        # Left first stair
        world.platformer(self.stair, x_pos=100, y_pos=423, loopControl=5, axs=False, group=sGroup)
        # Right first stair
        world.platformer(self.stair, x_pos=680, y_pos=423, loopControl=5, axs=False, group=sGroup)
        # First left-main floor
        world.platformer(self.ground, x_pos=162, y_pos=436, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=179, y_pos=432, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=196, y_pos=428, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=213, y_pos=424, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=230, y_pos=420, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=247, y_pos=416, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=264, y_pos=412, loopControl=1, axs=True, group=rGroupU)

        # First main floor
        world.platformer(self.ground, x_pos=281, y_pos=408, loopControl=23, axs=True, group=bottomPlatform)
        # First right-main floor
        world.platformer(self.ground, x_pos=517, y_pos=412, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=534, y_pos=416, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=551, y_pos=420, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=568, y_pos=424, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=585, y_pos=428, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=602, y_pos=432, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=619, y_pos=436, loopControl=1, axs=True, group=rGroupD)
        # Second left-ground floor
        world.platformer(self.ground, x_pos=40, y_pos=315, loopControl=4, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=86, y_pos=315, loopControl=5, axs=True, group=bottomPlatform)

        # Third left-ground floor
        world.platformer(self.ground, x_pos=40, y_pos=215, loopControl=9, axs=True, group=pGroup)
        # Fourth left-ground floor
        world.platformer(self.ground, x_pos=40, y_pos=100, loopControl=9, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=137, y_pos=104, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=154, y_pos=108, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=171, y_pos=104, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=188, y_pos=100, loopControl=11, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=305, y_pos=96, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=322, y_pos=92, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=339, y_pos=88, loopControl=1, axs=True, group=rGroupU)
        # Fourth right-ground floor
        world.platformer(self.ground, x_pos=646, y_pos=100, loopControl=9, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=629, y_pos=104, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=612, y_pos=108, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=595, y_pos=104, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=478, y_pos=100, loopControl=11, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=461, y_pos=96, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=444, y_pos=92, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=427, y_pos=88, loopControl=1, axs=True, group=rGroupD)
        # Right third-ground floor
        world.platformer(self.ground, x_pos=656, y_pos=315, loopControl=9, axs=True, group=bottomPlatform)
        # Right second-ground floor
        world.platformer(self.ground, x_pos=656, y_pos=215, loopControl=9, axs=True, group=pGroup)
        # Third main-ground floor
        world.platformer(self.ground, x_pos=281, y_pos=315, loopControl=10, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=387, y_pos=315, loopControl=5, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=437, y_pos=315, loopControl=8, axs=True, group=pGroup)

        # Third left-piece ground
        world.platformer(self.ground, x_pos=194, y_pos=315, loopControl=3, axs=True, group=pGroup)
        # Third right-piece ground
        world.platformer(self.ground, x_pos=568, y_pos=315, loopControl=3, axs=True, group=pGroup)
        # Third main floor
        world.platformer(self.ground, x_pos=205, y_pos=200, loopControl=7, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=281, y_pos=204, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=298, y_pos=208, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=315, y_pos=212, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=332, y_pos=216, loopControl=12, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=459, y_pos=212, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=476, y_pos=208, loopControl=1, axs=True, group=rGroupU)
        world.platformer(self.ground, x_pos=493, y_pos=204, loopControl=1, axs=True, group=rGroupD)
        world.platformer(self.ground, x_pos=510, y_pos=200, loopControl=7, axs=True, group=bottomPlatform)
        # First main ground-stair
        world.platformer(self.stair, x_pos=306, y_pos=301, loopControl=6, axs=False, group=sGroup)
        world.platformer(self.stair, x_pos=477, y_pos=301, loopControl=6, axs=False, group=sGroup)
        world.platformer(self.stair, x_pos=390, y_pos=208, loopControl=6, axs=False, group=sGroup)
        # Left Last stair
        world.platformer(self.stair, x_pos=95, y_pos=88, loopControl=14, axs=False, group=sGroup)
        world.platformer(self.stair, x_pos=230, y_pos=93, loopControl=6, axs=False, group=sGroup)
        # Right last stair
        world.platformer(self.stair, x_pos=680, y_pos=88, loopControl=14, axs=False, group=sGroup)
        world.platformer(self.stair, x_pos=540, y_pos=93, loopControl=6, axs=False, group=sGroup)
        # Left IVY
        world.platformer(self.ivy, x_pos=202, y_pos=328, loopControl=2, axs=False, group=sGroup)
        # Right IVY
        world.platformer(self.ivy, x_pos=570, y_pos=328, loopControl=2, axs=False, group=sGroup)
        # Coins
        coinCoordinates = [
            [40, 85],
            [40, 175],
            [40, 500],
            [315, 450],
            [450, 450],
            [750, 500],
            [725, 175],
            [725, 85],
            [425, 74],
            [340, 74],
            [200, 275],
            [585, 275]
        ]

        self.createCoin(coinGroup, coinCoordinates)

    def level2(self, world, pGroup, sGroup, bottomPlatform, coinGroup):
        # Left First Ground
        world.platformer(self.ground, x_pos=122, y_pos=515, loopControl=15, axs=True, group=pGroup)
        # Right First Ground
        world.platformer(self.ground, x_pos=500, y_pos=515, loopControl=15, axs=True, group=pGroup)
        # Left First Ground Stair: First
        world.platformer(self.stair, x_pos=122, y_pos=423, loopControl=5, axs=False, group=sGroup)
        # Left First Ground Stair: Second
        world.platformer(self.stair, x_pos=246, y_pos=423, loopControl=5, axs=False, group=sGroup)
        # Right First Ground Stair: First
        world.platformer(self.stair, x_pos=500, y_pos=423, loopControl=5, axs=False, group=sGroup)
        # Right First Ground Stair: Second
        world.platformer(self.stair, x_pos=624, y_pos=423, loopControl=5, axs=False, group=sGroup)
        # Left Second Ground: First
        world.platformer(self.ground, x_pos=40, y_pos=438, loopControl=3, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=70, y_pos=438, loopControl=7, axs=True, group=pGroup)
        # Left Second Ground: Second
        world.platformer(self.ground, x_pos=323, y_pos=438, loopControl=3, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=253, y_pos=438, loopControl=7, axs=True, group=pGroup)
        # Right Second Ground: First
        world.platformer(self.ground, x_pos=426, y_pos=438, loopControl=3, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=456, y_pos=438, loopControl=7, axs=True, group=pGroup)
        # Right Second Ground: Second
        world.platformer(self.ground, x_pos=700, y_pos=438, loopControl=3, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=630, y_pos=438, loopControl=7, axs=True, group=pGroup)
        # Left Second Ground Stair: First
        world.platformer(self.stair, x_pos=40, y_pos=346, loopControl=5, axs=False, group=sGroup)
        # Left Second Ground Stair: Second
        world.platformer(self.stair, x_pos=327, y_pos=286, loopControl=9, axs=False, group=sGroup)
        # Right Second Ground Stair: First
        world.platformer(self.stair, x_pos=426, y_pos=286, loopControl=9, axs=False, group=sGroup)
        # Right Second Ground Stair: Second
        world.platformer(self.stair, x_pos=704, y_pos=346, loopControl=5, axs=False, group=sGroup)
        # Left Third Ground
        world.platformer(self.ground, x_pos=120, y_pos=361, loopControl=3, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=40, y_pos=361, loopControl=8, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=150, y_pos=361, loopControl=12, axs=True, group=pGroup)
        # Right Third Ground
        world.platformer(self.ground, x_pos=620, y_pos=361, loopControl=3, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=500, y_pos=361, loopControl=12, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=650, y_pos=361, loopControl=8, axs=True, group=pGroup)
        # Left Third Ground Stair
        world.platformer(self.stair, x_pos=122, y_pos=209, loopControl=9, axs=False, group=sGroup)
        # Right Third Ground Stair
        world.platformer(self.stair, x_pos=624, y_pos=209, loopControl=9, axs=False, group=sGroup)
        # Left Fourth Ground
        world.platformer(self.ground, x_pos=126, y_pos=298, loopControl=22, axs=True, group=pGroup)
        # Right Fourth Ground
        world.platformer(self.ground, x_pos=426, y_pos=298, loopControl=22, axs=True, group=pGroup)
        # Left Fifth Ground
        world.platformer(self.ground, x_pos=240, y_pos=222, loopControl=3, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=40, y_pos=222, loopControl=20, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=270, y_pos=222, loopControl=5, axs=True, group=pGroup)
        # Right Fifth Ground
        world.platformer(self.ground, x_pos=500, y_pos=222, loopControl=3, axs=True, group=bottomPlatform)
        world.platformer(self.ground, x_pos=460, y_pos=222, loopControl=4, axs=True, group=pGroup)
        world.platformer(self.ground, x_pos=530, y_pos=222, loopControl=21, axs=True, group=pGroup)
        # Left Fifth Ground Stair
        world.platformer(self.stair, x_pos=246, y_pos=130, loopControl=5, axs=False, group=sGroup)
        # Right Fifth Ground Stair
        world.platformer(self.stair, x_pos=500, y_pos=130, loopControl=5, axs=False, group=sGroup)
        # Sixth Ground
        world.platformer(self.ground, x_pos=246, y_pos=144, loopControl=28, axs=True, group=pGroup)
        # Level-2 Coins
        coinCoordinates = [
            [340, 125], [425, 125],

            [310, 205], [460, 205], [40, 205], [725, 205],

            [200, 280], [565, 280],

            [200, 345], [565, 345],

            [295, 420], [470, 420],

            [170, 500], [570, 500]
        ]

        self.createCoin(coinGroup, coinCoordinates)

    def level3(self):
        pass

    def createCoin(self, coinGroup, coinCoordinates):
        for rect in coinCoordinates:
            coinGroup.add(Coin(rect[0], rect[1]))
