import pygame


def load_image(filename):
    image = pygame.image.load(
        f'/home/bloodwolf/project/python/pyExperaments/spaceshooter/image/{filename}').convert_alpha()
    return image
