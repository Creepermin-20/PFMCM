import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.background = pygame.image.load('/home/aydan/Documents/GitHub/PFMCM/MEDIA/tiles/background.png')
        pygame.display.set_caption("PFMCM")
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            self.screen.fill((0,0,0))
            self.screen.blit(self.background,self.background.get_rect(topleft = (87.5,74)))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()