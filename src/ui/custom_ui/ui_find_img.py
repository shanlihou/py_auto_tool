import ui_base
import pygame
import utils
import const
import global_data



class FindImg(ui_base.UIBase):
    def __init__(self):
        super().__init__(1, None)
        self.tgt_img_pos = (0.03, 0.2)

    def draw(self, draw_ctx):
        _pos = utils.get_screen_pos(self.win_idx, self.tgt_img_pos)
        _target_img = utils.get_origin_target_image(global_data.DEBUG_TARGET)
        draw_ctx.screen.blit(_target_img, _pos)

        _text = 'img name: {}'.format(global_data.DEBUG_TARGET)
        _font = utils.get_font(20)
        _text = _font.render(_text, True, const.COLOR_GREEN)
        _text_pos = utils.get_screen_pos(self.win_idx, (0.53, 0.05))
        draw_ctx.screen.blit(_text, _text_pos)
        
