from settings import *
from sprites import Sprite

class AllSprites(pygame.sprite.Group):
    def __init__(self, width, height, bg_tile = None):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()
        self.width, self.height = width * TILE_SIZE, height * TILE_SIZE
        
        if bg_tile:
            for col in range(width):
                for row in range(height):
                    x, y = col * TILE_SIZE, row * TILE_SIZE
                    Sprite((x,y), bg_tile, self, -1)
        
    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)
        
        
        
        for sprite in sorted(self, key = lambda sprite: sprite.z):
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, offset_pos)