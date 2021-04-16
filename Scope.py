import random
import pygame


class Scope:
    def __init__(self):
        self.red = random.randrange(0, 70)
        self.green = random.randrange(128, 255)
        self.blue = random.randrange(128, 255)
        self.linecolor = self.red, self.green, self.blue
        self.xs = 7
        self.ys = 7
        self.x_scope_pos = 0
        self.y_scope_pos = 0
        self.shot_sound = pygame.mixer.Sound('weapons/awp.wav')
        self.shot_sound.set_volume(0.1)
        self.score = 0

    def handle_mouse(self, event, target, score):
        if event.type == pygame.MOUSEMOTION:
            self.x_scope_pos, self.y_scope_pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.shot_sound.play()
                shot = pygame.Rect(self.x_scope_pos, self.y_scope_pos, 1, 1)
                if shot.colliderect(target.get_rect()):
                    self.score += 10
                    score.update(self.score)
                    target.update()

    def blit(self, surface):
        pygame.draw.line(surface, self.linecolor, (self.x_scope_pos - self.xs, self.y_scope_pos),
                         (self.x_scope_pos + self.xs, self.y_scope_pos))
        pygame.draw.line(surface, self.linecolor, (self.x_scope_pos, self.y_scope_pos - self.ys),
                         (self.x_scope_pos, self.y_scope_pos + self.ys))

    def get_score(self):
        return self.score

    def update(self):
        pass


if __name__ == "__main__":
    pass
