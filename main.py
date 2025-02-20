import pygame
import settings

from classes.Tile import Tile
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 960, 540
screen = pygame.display.set_mode((width, height))

visible_objects = pygame.sprite.Group()
collidable_objects = pygame.sprite.Group()

 

while True:
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
    for y, row in enumerate(settings.MAP):
        for x, tile in enumerate(row):
            pos_x = x * settings.TILE_SIZE
            pos_y = y * settings.TILE_SIZE
            
            Tile((pos_x, pos_y), (settings.TILE_SIZE, settings.TILE_SIZE), "C:\\Users\\20241034010004\\Documents\\caatingueiros-adventures-main\\assets\\img\\grass.png    ", (visible_objects))
            
    
    visible_objects.update()
    collidable_objects.update()
    visible_objects.draw(screen)
    
    
    pygame.display.flip()
    fpsClock.tick(settings.FPS)