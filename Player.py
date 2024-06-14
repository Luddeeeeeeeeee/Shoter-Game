from typing import Any
import pygame
from Arrows import Arrows
class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        
        self.image = pygame.image.load("sprites/Player.png").convert_alpha()
        
        self.rect = self.image.get_rect(center = (500,450))
        self.fliped = pygame.transform.flip(self.image, True, False)
        self.speed = 6
        self.direction = ""

        self.arrwos = pygame.sprite.Group()
        self.ready = True
        self.arrwos_time = 0
        self.arrwos_cooldown = 600
        self.arrwos_direction_x = 6
        self.arrwos_direction_y = 0
        self.amount_of_arrwos = 10


    def move(self):
        keys = pygame.key.get_pressed()
        move_vector = [0,0]
        if keys[pygame.K_w]:
            move_vector[1] -= 1
            self.arrwos_direction_x = 0
            self.arrwos_direction_y = -6
            
        if keys[pygame.K_s]:
            move_vector[1] += 1
            self.arrwos_direction_x = 0
            self.arrwos_direction_y = 6

        if keys[pygame.K_a]:
            move_vector[0] -= 1
            self.arrwos_direction_x = -6
            self.arrwos_direction_y = 0
            self.image = pygame.image.load("sprites/Player.png").convert_alpha()


        if keys[pygame.K_d]:
            move_vector[0] += 1
            self.arrwos_direction_x = 6
            self.arrwos_direction_y = 0
            self.image = self.fliped


        if move_vector[0] != 0 and move_vector[1] != 0:
            move_vector[0] *= 0.7071  
            move_vector[1] *= 0.7071

        
        self.rect.x += move_vector[0] * self.speed
        self.rect.y += move_vector[1] * self.speed


        if keys[pygame.K_SPACE] and self.ready and self.amount_of_arrwos != 0:
            self.Shoot()
            self.ready =False
            self.arrwos_time = pygame.time.get_ticks()
            self.amount_of_arrwos -= 1



    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.arrwos_time >= self.arrwos_cooldown:
                self.ready =True

    def Shoot(self):
        self.arrwos.add(Arrows(self.rect.center,self.arrwos_direction_x,self.arrwos_direction_y))


    def update(self):
        self.move()
        self.recharge()
        self.arrwos.update()
        