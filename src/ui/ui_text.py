import ui_base
import utils
import pygame
import const


class Text(ui_base.UIBase):
    def __init__(self, win_idx, rect):
        super(Text, self).__init__(win_idx, rect)
        self.lines = []

    def draw(self, draw_ctx):
        _rect = utils.get_screen_rect(self.win_idx, self.rect)
        pygame.draw.rect(draw_ctx.screen, const.COLOR_GREEN, _rect, 1, border_radius=10)

        x, y, w, h = _rect
        off = 5
        for i, _line in enumerate(self.lines):
            _text = utils.get_font(20).render(_line, True, const.COLOR_GREEN, const.COLOR_BG)
            draw_ctx.screen.blit(_text, (x + off, y + i * 20 + off))



