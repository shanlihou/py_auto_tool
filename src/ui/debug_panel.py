import pygame
import global_data
import utils
import ui_base
import const


class DebugPanel(ui_base.UIBase):
    def __init__(self):
        super(DebugPanel, self).__init__(0, None)

    def draw(self, draw_ctx):
        x = 0
        y = 210
        font = utils.get_font(20)
        font_color = const.COLOR_BLUE

        i = 0
        text = font.render('ratio:{}'.format(global_data.DEBUG_SIM_RATIO), True, font_color)
        draw_ctx.screen.blit(text, (x, y))

        i += 1
        text = font.render('bot:{}'.format(global_data.BOT_NAME), True, font_color)
        draw_ctx.screen.blit(text, (x, y + 25 * i))

        i += 1
        text = font.render('fps:{}'.format(global_data.CLOCK.get_fps()), True, font_color)
        draw_ctx.screen.blit(text, (x, y + 25 * i))
