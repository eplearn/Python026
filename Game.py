import sys
import pygame
from collections import defaultdict

from Target import Target
from Score import Score


class Game:
    def __init__(self, caption, width, height, background, frame_rate):
        pygame.init()
        self.caption = caption
        self.background = background
        self.frame_rate = frame_rate
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()
        self.game_objects = []
        self.mouse_handlers = defaultdict(list)  # dct = {'pressed': [obj1, obj2], 'moved': [obj1, obj2]}

    def start_game(self):
        pygame.mouse.set_visible(0)
        pygame.mixer.music.load('music/Highway_to_Hell.mp3')
        pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1)
        self.shot_sound = pygame.mixer.Sound('weapons/awp.wav')
        self.shot_sound.set_volume(0.1)

        while True:
            self.handle_events()
            self.surface.fill(self.background)
            self.update()
            self.blit(self.surface)
            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def update(self):
        for obj in self.game_objects:
            obj.update

    def blit(self, surface):
        for obj in self.game_objects:
            obj.blit(surface)

    def handle_events(self):
        for obj in self.game_objects:
            if isinstance(obj, Target):
                target = obj
            if isinstance(obj, Score):
                score = obj
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN):
                for handler in self.mouse_handlers[event.type]:
                    handler(event, target, score)


if __name__ == "__main__":
    pass
