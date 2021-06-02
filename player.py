import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self):
        self.scale = 1
        Sprite.__init__(self)
        self.image = pygame.image.load("images/jumpman/jumpman.gif")
        self.image_move_left = pygame.image.load("images/jumpman/jumpman_move_left.gif")
        self.image_move_right = pygame.image.load("images/jumpman/jumpman_move_right.gif")
        self.image_jump_left = pygame.image.load("images/jumpman/jumpman_run_left.gif")
        self.image_jump_right = pygame.image.load("images/jumpman/jumpman_run_right.gif")
        #        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale),
        #                                                         int(self.image.get_height() * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.x = 160
        self.rect.y = 405
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
        self.move_left = False
        self.move_right = False
        self.move_down = False
        self.move_up = False
        self.jumping = False
        self.direction = 0
        self.move_x = 5
        self.move_y = 5
        self.vel_x = 0
        self.vel_y = 10
        self.gravity_force = 5

    def functions(self, platformGroup, stairGroup, rampGroupU, rampGroupD):
        if self.move_left:
            if self.rect.x > 0:
                self.rect.x -= self.move_x
                if pygame.sprite.spritecollide(self, platformGroup, False):
                    self.rect.x += self.move_x
                elif pygame.sprite.spritecollide(self, rampGroupU, False):
                    self.rect.y -= self.move_y - 2
                    self.rect.x += self.move_x - 2
                elif pygame.sprite.spritecollide(self, rampGroupD, False):
                    self.rect.y -= self.move_y - 2
                    self.rect.x -= self.move_x - 2
                else:
                    self.rect.x -= self.move_x

        if self.move_right:
            if self.rect.x < self.screenwidth - 32:
                self.rect.x += self.move_x
                if pygame.sprite.spritecollide(self, platformGroup, False):
                    self.rect.x += self.move_x
                elif pygame.sprite.spritecollide(self, rampGroupU, False):
                    self.rect.y -= self.move_y
                    self.rect.x += self.move_x - 2
                    if pygame.sprite.spritecollide(self, platformGroup, False):
                        self.rect.y -= self.move_y + 3
                elif pygame.sprite.spritecollide(self, rampGroupU, False):
                    self.rect.y -= self.move_y - 2
                    self.rect.x += self.move_x - 2
                else:
                    self.rect.x += self.move_x
        if self.move_down:
            if self.rect.y < 565:
                self.rect.y += self.move_y
                if pygame.sprite.spritecollide(self, stairGroup, False):
                    self.rect.y += self.move_y
                else:
                    if pygame.sprite.spritecollide(self, platformGroup, False):
                        self.rect.y -= self.move_y
                    elif pygame.sprite.spritecollide(self, rampGroupU, False):
                        self.rect.y -= self.move_y
                    elif pygame.sprite.spritecollide(self, rampGroupD, False):
                        self.rect.y -= self.move_y
                    else:
                        self.rect.y -= self.move_y

        if self.move_up:
            if self.rect.y > 0:
                self.rect.y -= (self.move_y + 1)
                if pygame.sprite.spritecollide(self, stairGroup, False):
                    self.rect.y -= (self.move_y + 1)
                else:
                    if pygame.sprite.spritecollide(self, platformGroup, False):
                        self.rect.y += self.move_y
                    elif pygame.sprite.spritecollide(self, rampGroupU, False):
                        self.rect.y += self.move_y
                    else:
                        self.rect.y += self.move_y
        if self.jumping:
            self.direction = 2
            self.rect.y -= self.vel_y
            self.vel_y -= 1
            if self.vel_y < -(self.move_y * 2):
                self.jumping = False
                self.vel_y = (self.move_y * 2)

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_left = True
                self.direction = -1

            if event.key == pygame.K_RIGHT:
                self.move_right = True
                self.direction = 1

            if not self.jumping and event.key == pygame.K_LSHIFT:
                if self.move_left:
                    self.jumping = True
                if self.move_right:
                    self.jumping = True

            if event.key == pygame.K_DOWN:
                self.move_down = True

            if event.key == pygame.K_UP:
                self.move_up = True

        if not event.type == pygame.KEYDOWN:
            self.direction = 0
            self.move_left = False
            self.move_right = False
            self.jumping = False
            self.move_up = False
            self.move_down = False

    def gravity(self, platformGroup, rampGroupU, rampGroupD):
        self.rect.y += self.gravity_force
        if pygame.sprite.spritecollide(self, platformGroup, False):
            self.rect.y -= self.gravity_force
        elif pygame.sprite.spritecollide(self, rampGroupU, False):
            self.rect.y -= self.gravity_force
        elif pygame.sprite.spritecollide(self, rampGroupD, False):
            self.rect.y -= self.gravity_force

    def draw(self, screen):
        if self.direction == 0:
            screen.blit(self.image, self.rect)
        if self.direction == 1:
            screen.blit(self.image_move_right, self.rect)
        if self.direction == -1:
            screen.blit(self.image_move_left, self.rect)
        if self.direction == 2:
            if self.move_left:
                screen.blit(self.image_jump_left, self.rect)
            if self.move_right:
                screen.blit(self.image_jump_right, self.rect)
