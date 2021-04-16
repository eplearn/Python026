import pygame

from Scope import Scope


class Score:
    def __init__(self):
        self.score_obj = pygame.font.Font('scootchover-sans.ttf', 12)
        self.score = 0

    def blit(self, surface):
        score_text = self.score_obj.render(f'Score: {self.score}', True, (255, 255, 255))
        surface.blit(score_text, (5, 5))

    def update(self, scope_score):
        self.score = scope_score


if __name__ == "__main__":
    pass
