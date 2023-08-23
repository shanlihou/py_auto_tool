import ui_base
import global_data
import pygame
import utils
import const
import cv_helper



class CustomAna(ui_base.UIBase):
    def __init__(self):
        super().__init__(1, None)
        global_data.EVENT_MGR.register_cb(pygame.MOUSEBUTTONDOWN, self.on_mouse_down)

        self.press_text_pos = (0.03, 0.15)
        self.press_pos = None
        self.image_pos = None

        self.color_disp_pos = (0.53, 0.03)
        self.press_color = None

        self.draw_color_rect = (0.53, 0.15, 0.4, 0.1)

        self.color_count_pos = (0.03, 0.2)

    def on_mouse_down(self, pos):
        if not utils.is_pos_in_screen(pos):
            return
        print(pos)
        self.press_pos = pos
        self.image_pos = utils.screen_pos_to_image_pos(pos)
        _color = cv_helper.get_pos_color(self.image_pos)
        self.press_color = _color

    def draw(self, draw_ctx):
        font_size = 20
        font = utils.get_font(font_size)
        _text = '{}->{}'.format(self.press_pos, self.image_pos)
        text = font.render(_text, True, const.COLOR_GREEN, const.COLOR_BG)
        _pos = utils.get_screen_pos(self.win_idx, self.press_text_pos)
        draw_ctx.screen.blit(text, _pos)
        
        # draw pos color
        _text = 'color:{}'.format(self.press_color)
        text = font.render(_text, True, const.COLOR_GREEN, const.COLOR_BG)
        _pos = utils.get_screen_pos(self.win_idx, self.color_disp_pos)
        draw_ctx.screen.blit(text, _pos)

        # draw color
        if self.press_color is None:
            return

        color_rect = utils.get_screen_rect(self.win_idx, self.draw_color_rect)
        pygame.draw.rect(draw_ctx.screen, self.press_color, color_rect)

        _count = 0
        for pos in cv_helper.get_color_poses(self.press_color):
            _pos = utils.back_pos_to_screen(pos)
            _rect = (_pos[0], _pos[1], 1, 1)
            pygame.draw.rect(draw_ctx.screen, const.COLOR_RED, _rect)
            _count += 1

        _text = 'count:{}'.format(_count)
        text = font.render(_text, True, const.COLOR_GREEN)
        _pos = utils.get_screen_pos(self.win_idx, self.color_count_pos)
        draw_ctx.screen.blit(text, _pos)


