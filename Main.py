import pygame
pygame.init()
from Player import Player
from Enemy import Enemy


class Game():
    def __init__(self):
        pygame.init()
        self.Clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1000,900))




        player_sprite = Player()
        self.player = pygame.sprite.GroupSingle(player_sprite)
        enemy_sprite = Enemy()
        self.enemy = pygame.sprite.Group(enemy_sprite)

    def collison(self):
        for arrwos in self.player.sprite.arrwos:
            if pygame.sprite.spritecollide(arrwos, self.enemy, True):
                arrwos.kill()
                self.enemy.add(Enemy())
        for enemy in self.enemy:
            if pygame.sprite.spritecollide(enemy,self.player, True):
                self.player.kill()
        
    def run(self):
        run = True
        while run:
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.screen.fill((0,153,0))
        
            self.player.draw(self.screen)
            self.enemy.draw(self.screen)
            self.player.sprite.arrwos.draw(self.screen)
            player_rect = self.player.sprite.rect  
            self.player.update()
            self.enemy.update(player_rect.x,player_rect.y)
            self.collison()

            
            pygame.display.flip()
            self.Clock.tick(60)

    

        

if __name__ == "__main__":
    game = Game()
    game.run()
