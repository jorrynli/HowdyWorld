import pygame
from settings import *
from player import Player
from sprites import Generic
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()

        self.setup()

    def setup(self):
        self.player = Player((640,360), self.all_sprites)
        Generic(
            pos = (0,0),
            surf = pygame.image.load('../graphics/world/ground.png').convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS[''])

    def run(self, dt):
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def customize_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)