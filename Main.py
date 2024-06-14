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
        
        self.enemy = pygame.sprite.Group(Enemy())
        self.my_font = pygame.font.SysFont("Jacquard 12", 39)
        self.enemy.add(Enemy())
        self.amount_of_enemys = 1
        self.run2 = False
        self.score = 0

    def collison(self):
        
        for arrwos in self.player.sprite.arrwos:
            if pygame.sprite.spritecollide(arrwos, self.enemy, True):
                arrwos.kill()
                self.player.sprite.amount_of_arrwos += 1
                self.amount_of_enemys += 0.25
                self.score += 1

                
        for enemy in self.enemy:
            if pygame.sprite.spritecollide(enemy,self.player, False):
                self.run2 = False
                self.enemy.empty()
                self.player.sprite.amount_of_arrwos = 10
                self.score = 0
                self.amount_of_enemys = 1
                self.player.rect = 500,450

        

        if len(self.enemy.sprites()) < self.amount_of_enemys:
            self.enemy.add(Enemy())

        

    def text(self):
        text_surface = self.my_font.render("arrows "+ str(self.player.sprite.amount_of_arrwos), False, (255, 255, 255))
        text_surface2 = self.my_font.render("Score "+ str(self.score), False, (255, 255, 255))
        self.screen.blit(text_surface, (850,0))
        self.screen.blit(text_surface2, (50,0))


    def start_screen(self):
        text = self.my_font.render("Press E to start", False, (255, 255, 255))
        self.screen.blit(text, (360,350))
        
    def run(self):
        run = True
        while run:
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.run2 = True
                        

            self.screen.fill((0,153,0))
            self.start_screen()
            
            if self.run2 == True:
                self.screen.fill((0,153,0))
                self.player.draw(self.screen)
                self.enemy.draw(self.screen)
                self.player.sprite.arrwos.draw(self.screen)
                player_rect = self.player.sprite.rect  
                self.player.update()
                self.enemy.update(player_rect.x,player_rect.y)
                self.collison()
                self.text()
            
            pygame.display.flip()
            self.Clock.tick(60)

    

        
if __name__ == "__main__":
    
    game = Game()
    game.run()
