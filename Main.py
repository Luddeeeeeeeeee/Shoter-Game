import pygame
pygame.init()
from Player import Player
from Enemy import Enemy


class Game():
    def __init__(self) -> None:
        player_sprite = Player()
        self.player = pygame.sprite.GroupSingle(player_sprite)
        enemy_sprite = Enemy()
        self.enemy = pygame.sprite.Group(enemy_sprite)

    def collison(self):
        for arrwos in self.player.sprite.arrwos:
            if pygame.sprite.spritecollide(arrwos, self.enemy, True):
                arrwos.kill()
        
    def run(self):
        self.player.draw(screen)
        self.enemy.draw(screen)
        self.player.sprite.arrwos.draw(screen)
        player_rect = self.player.sprite.rect  
        self.player.update()
        self.enemy.update(player_rect.x,player_rect.y)
        self.collison()

    

        
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