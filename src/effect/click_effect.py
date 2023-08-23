import pygame
import global_data


class ClickEffect(object):
    def __init__(self, effect_id, pos, start_time) -> None:
        self.pos = pos
        self.start_time = start_time
        self.effect_id = effect_id

    def draw(self, draw_ctx):
        cur_time = pygame.time.get_ticks()
        radius = (cur_time - self.start_time) / 1000 * 100
        if radius > 50:
            global_data.EFFECT_MGR.remove_effect(self.effect_id)
            return

        pygame.draw.circle(draw_ctx.screen, (255, 0, 0), self.pos, radius, 1)


