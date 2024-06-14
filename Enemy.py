from typing import Any
import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self,player_x=0, player_y=0):
        super().__init__()
        spawn = {-50:50, 500:-50, 1050:50, 500: 950}
        x, y = random.choice(list(spawn.items()))

        self.image = pygame.image.load("sprites/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(center = (x,y))
        self.player_x = player_x
        self.player_y = player_y
    def move_to_player(self,player_x, player_y):
        move_vector = [0,0]
        speed = 3
        if player_x > self.rect.x:
            move_vector[0] += 1
        elif player_x < self.rect.x:
            move_vector[0] -= 1
        elif player_x == self.rect.x:
            self.rect.x += 0
        
        if player_y > self.rect.y:
            move_vector[1] += 1
        elif player_y < self.rect.y:
            move_vector[1] -= 1
        elif player_y == self.rect.y:
            self.rect.y += 0

        if move_vector[0] != 0 and move_vector[1] != 0:
            move_vector[0] *= 0.7071  
            move_vector[1] *= 0.7071

        
        self.rect.x += move_vector[0] * speed
        self.rect.y += move_vector[1] * speed
            
    def update(self,player_x, player_y):
        self.player_x = player_x  
        self.player_y = player_y
        self.move_to_player(player_x, player_y)
        