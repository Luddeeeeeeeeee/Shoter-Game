import pygame
pygame.init()
from Player import Player


class Game():
    def __init__(self) -> None:
        player_sprite = Player()
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.draw(screen)
        self.player.draw(screen)
        self.player.sprite.arrwos.draw(screen)
        self.player.update()
        
run = True
Clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,900))
game = Game()
while run:
    
    for event in pygame.event.get():
         
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0,153,0))
    game.run()
    pygame.display.flip()
    Clock.tick(60)