import ui_base
import utils
import pygame
import const
import global_data


class Choicer(ui_base.UIBase):
    def __init__(self, win_idx, rect, choices, is_horizontal=True):
        super(Choicer, self).__init__(win_idx, rect)
        self.win_idx = win_idx
        self.rect = rect
        self.choices = choices
        self.choice_idx = 0
        global_data.EVENT_MGR.register_cb(pygame.MOUSEBUTTONDOWN, self.on_mouse_down)

        self.on_choice_changed = None
        self.is_horizontal = is_horizontal

    def on_mouse_down(self, pos):
        if not self.is_pos_in(pos):
            return

        _rect = utils.get_screen_rect(self.win_idx, self.rect)
        x, y, w, h = _rect
        _num = len(self.choices)
        _choice_width = w / _num
        _choice_idx = int((pos[0] - x) / _choice_width)
        if _choice_idx < 0 or _choice_idx >= _num:
            return

        if self.choice_idx != _choice_idx:
            self.choice_idx = _choice_idx

            if self.on_choice_changed is not None:
                _choice = self.choices[self.choice_idx]
                self.on_choice_changed(_choice)

    def draw(self, draw_ctx):
        _num = len(self.choices)
        _rect = utils.get_screen_rect(self.win_idx, self.rect)
        
        x, y, w, h = _rect
        x = int(x)
        _choice_width = int(w / _num)

        _radius = 10
        
        for i in range(_num):
            if self.is_horizontal:
                _rect_choice = (x + i * _choice_width, y, _choice_width, h)
            else:
                _rect_choice = (x, y + i * _choice_width, w, _choice_width)

            border_top_left_radius = -1
            border_top_right_radius = -1
            border_bottom_left_radius = -1
            border_bottom_right_radius = -1

            if self.is_horizontal:
                if i == 0:
                    border_top_left_radius = _radius
                    border_bottom_left_radius = _radius

                if i == _num - 1:
                    border_top_right_radius = _radius
                    border_bottom_right_radius = _radius
            else:
                if i == 0:
                    border_top_left_radius = _radius
                    border_top_right_radius = _radius

                if i == _num - 1:
                    border_bottom_left_radius = _radius
                    border_bottom_right_radius = _radius

            _is_selected = i == self.choice_idx
            _wrap_width = 0 if _is_selected else 1
            pygame.draw.rect(
                draw_ctx.screen, 
                const.COLOR_GREEN, 
                _rect_choice, 
                _wrap_width,
                border_top_left_radius=border_top_left_radius,
                border_top_right_radius=border_top_right_radius,
                border_bottom_left_radius=border_bottom_left_radius,
                border_bottom_right_radius=border_bottom_right_radius
            )
            
            self._draw_text(_is_selected, i, _rect_choice, draw_ctx)

    def _draw_text(self, is_selected, idx, rect, draw_ctx):
        x, y, w, h = rect
        _font_color = const.COLOR_BG if is_selected else const.COLOR_GREEN
        _bg_color = const.COLOR_GREEN if is_selected else const.COLOR_BG

        _content = self.choices[idx]
        _font_size = int(h / 2)

        _text = utils.get_font(_font_size).render(_content, True, _font_color, _bg_color)
        _text_size = _text.get_size()
        _text_x = x + (w - _text_size[0]) / 2
        _text_y = y + (h - _text_size[1]) / 2
        draw_ctx.screen.blit(_text, (_text_x, _text_y))
            

