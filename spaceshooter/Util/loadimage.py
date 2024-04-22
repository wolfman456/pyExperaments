import pygame


def load_image(filename):
    try:
        image = pygame.image.load(
            f'/home/bloodwolf/project/python/pyExperaments/spaceshooter/image/{filename}').convert_alpha()
        return image
    except pygame.error:
        print(f'Cannot load image: {filename}')
