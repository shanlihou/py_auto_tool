import pygame
import global_data
import ui_base
import utils


class SimilarRatio(ui_base.UIBase):
    def __init__(self, win_idx, rect):
        super(SimilarRatio, self).__init__(win_idx, rect)
        global_data.EVENT_MGR.register_cb(pygame.MOUSEBUTTONDOWN, self.on_mouse_down)

    def on_mouse_down(self, pos):
        if not self.is_pos_in(pos):
            return

        _rect = utils.get_screen_rect(self.win_idx, self.rect)
        _top = _rect[1]
        _bottom = _top + _rect[3]
        _new_ratio = (_bottom - pos[1]) / (_bottom - _top)
        global_data.DEBUG_SIM_RATIO = _new_ratio

    def draw(self, draw_ctx):
        _rect = utils.get_screen_rect(self.win_idx, self.rect)
        pygame.draw.rect(draw_ctx.screen, (0, 255, 0), _rect, 2)

        _bottom = self.rect[1] + self.rect[3]
        _h = global_data.DEBUG_SIM_RATIO * self.rect[3]
        _y = _bottom - _h

        _new_rect = (self.rect[0], _y, self.rect[2], _h)
        _new_rect = utils.get_screen_rect(self.win_idx, _new_rect)
        pygame.draw.rect(draw_ctx.screen, (0, 255, 0), _new_rect)

