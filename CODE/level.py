import pygame
from settings import *
from tile import Tile
from tile2 import Tile2
from player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        
        self.visible_sprites = YSortCameraGroup()
        self.obstical_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstical_sprites])
                if col == 'y':
                    Tile2((x,y),[self.visible_sprites,self.obstical_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstical_sprites)

    def run(self):
        self.visible_sprites.custom_draw()
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//4.5
        self.half_hiegth = self.display_surface.get_size()[1]//4.5
        self.offset = pygame.math.Vector2(self.half_width,self.half_hiegth)

    def custom_draw(self):
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image,offset_pos)