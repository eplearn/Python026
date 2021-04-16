import pygame

from Game import Game
from Scope import Scope
from Target import Target
from Score import Score


class ShootingGallery(Game):
    def __init__(self):
        super().__init__('Shooting Gallery', 640, 480, (0, 0, 0), 60)
        self.scope = None
        self.target = None
        self.score = None
        self.create_objects()

    def create_objects(self):
        self.create_target()
        self.create_scope()
        self.create_score()

    def create_scope(self):
        scope = Scope()
        self.scope = scope
        self.mouse_handlers[pygame.MOUSEMOTION].append(scope.handle_mouse)
        self.mouse_handlers[pygame.MOUSEBUTTONDOWN].append(scope.handle_mouse)
        self.game_objects.append(self.scope)

    def create_target(self):
        target = Target()
        self.target = target
        self.game_objects.append(self.target)

    def create_score(self):
        score = Score()
        self.score = score
        self.game_objects.append(self.score)


if __name__ == '__main__':
    ShootingGallery().start_game()
