import pygame

class Arrows(pygame.sprite.Sprite):
    def __init__(self,pos,speed_x,speed_y,) -> None:
        super().__init__()
        self.original_image = pygame.image.load("sprites/Arrow.png").convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center = pos)
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.direction_flipped = False
          
        

    def update(self):    
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.speed_y < 0:
            self.direction = -1
        elif self.speed_y > 0:
            self.direction = 1
        else:
            self.direction = 0
        if self.speed_x > 0 or self.speed_x < 0:
            self.direction_flipped = False
        
        if self.direction == 1 and not self.direction_flipped:
            self.image = pygame.transform.rotate(self.image, 90)
            self.direction_flipped = True

        elif self.direction == -1 and not self.direction_flipped:
            self.image = pygame.transform.rotate(self.image, -90)
            self.direction_flipped = True