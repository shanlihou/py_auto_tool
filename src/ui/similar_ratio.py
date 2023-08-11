import pygame
import global_data


class SimilarRatio(object):
    def __init__(self):
        self.x = 0.85
        self.y = 0.1
        self.w = 0.05
        self.h = 0.8

        global_data.EVENT_MGR.register_cb(pygame.MOUSEBUTTONDOWN, self.on_mouse_down)

    def is_pos_in(self, pos):
        _x = pos[0]
        _y = pos[1]

        _size = global_data.SCREEN_SIZE
        _left = _size[0] * self.x
        _right = _left + _size[0] * self.w
        _top = _size[1] * self.y
        _bottom = _top + _size[1] * self.h

        if _x > _left and _x < _right and _y > _top and _y < _bottom:
            return True

        return False

    def on_mouse_down(self, pos):
        if not self.is_pos_in(pos):
            return

        _size = global_data.SCREEN_SIZE
        _top = _size[1] * self.y
        _bottom = _top + _size[1] * self.h
        _new_ratio = (_bottom - pos[1]) / (_bottom - _top)
        global_data.DEBUG_SIM_RATIO = _new_ratio

    def draw(self, draw_ctx):
        _rect = draw_ctx.rect_by_ratio(self.x, self.y, self.w, self.h)
        pygame.draw.rect(draw_ctx.screen, (0, 255, 0), _rect, 2)

        _top = self.y
        _bottom = self.y + self.h
        
        _h = global_data.DEBUG_SIM_RATIO * self.h
        _y = _bottom - _h

        _rect = draw_ctx.rect_by_ratio(self.x, _y, self.w, _h)
        pygame.draw.rect(draw_ctx.screen, (0, 255, 0), _rect)

