import pygame
import global_data


class DebugPanel(object):
    def __init__(self):
        pass

    def draw(self, draw_ctx):
        font = pygame.font.Font('res/Teko-Bold.ttf', 20)

# 2.通过字体创建文字对象
# 字体对象.render(文字内容,True,文字颜色,背景颜色=None)
        text = font.render('ratio:{}'.format(global_data.DEBUG_SIM_RATIO), True, (0, 0, 255), (0, 255, 0))
        draw_ctx.screen.blit(text, (0, 0))
