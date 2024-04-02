from typing import Any
import pygame
from Arrows import Arrows
class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("sprites/Player.png").convert_alpha()
        self.rect = self.image.get_rect(center = (500,450))
        self.arrwos = pygame.sprite.Group()
        self.ready = True
        self.arrwos_time = 0
        self.arrwos_cooldown = 600
        self.arrwos_direction_x = 6
        self.arrwos_direction_y = 0
        self.flip = True


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 5
            self.arrwos_direction_x = 0
            self.arrwos_direction_y = -6
            self.flip = True
            
        if keys[pygame.K_s]:
            self.rect.y += 5
            self.arrwos_direction_x = 0
            self.arrwos_direction_y = 6
            self.flip = True

        if keys[pygame.K_a]:
            self.rect.x -= 5
            self.arrwos_direction_x = -6
            self.arrwos_direction_y = 0
            self.flip = False

        if keys[pygame.K_d]:
            self.rect.x += 5
            self.arrwos_direction_x = 6
            self.arrwos_direction_y = 0
            self.flip = False


        if keys[pygame.K_SPACE] and self.ready:
            self.Shoot()
            self.ready =False
            self.arrwos_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.arrwos_time >= self.arrwos_cooldown:
                self.ready =True

    def Shoot(self):
        self.arrwos.add(Arrows(self.rect.center,self.arrwos_direction_x,self.arrwos_direction_y, self.flip))


    def update(self):
        self.move()
        self.recharge()
        self.arrwos.update()
        