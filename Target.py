import random
import pygame


class Target:
    def __init__(self):
        self.img = pygame.image.load('DK.bmp')
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(0, 600)
        self.rect.y = random.randint(0, 452)

    def get_rect(self):
        return self.rect

    def update(self):
        self.rect.x = random.randint(0, 600)
        self.rect.y = random.randint(0, 452)

    def blit(self, surface):
        surface.blit(self.img, self.rect)


if __name__ == "__main__":
    pass
