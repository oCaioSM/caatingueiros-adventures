import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size, image, groups):
        super().__init__(groups)
        self.groups = groups
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), size)