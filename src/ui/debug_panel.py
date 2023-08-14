import pygame
import global_data
import utils
import ui_base


class DebugPanel(ui_base.UIBase):
    def __init__(self):
        super(DebugPanel, self).__init__(0, None)

    def draw(self, draw_ctx):
        font = utils.get_font(20)

        text = font.render('ratio:{}'.format(global_data.DEBUG_SIM_RATIO), True, (0, 0, 255), (0, 255, 0))
        draw_ctx.screen.blit(text, (0, 0))


