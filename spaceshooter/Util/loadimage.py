import pygame


def loadimage(filename):
    image = pygame.image.load(
        f'/home/bloodwolf/project/python/pyExperaments/spaceshooter/image/{filename}').convert_alpha()
    return image
