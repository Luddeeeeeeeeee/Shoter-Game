import pygame

class Droped_arrows(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        
        self.image = pygame.image.load("sprites/droped_arrow.png").convert_alpha()
        
        self.rect = self.image.get_rect(center = (x,y))