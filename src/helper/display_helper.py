import pygame
from helper import cv_helper
import const
import ui_mgr
import draw_context
import global_data


class DisplayHelper(object):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        global_data.SCREEN_SIZE = (700, 500)
        _size = (1400, 500)
        # screen = pygame.display.set_mode(_size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
        screen = pygame.display.set_mode(_size)

        pygame.display.set_caption("My Game")

        self.screen = screen
        self._ui_mgr = ui_mgr.UIMgr()
        global_data.UI_MGR = self._ui_mgr

    def on_mouse_down(self, pos):
        global_data.EFFECT_MGR.add_click_effect(pos)

    def draw_capture(self):
        self.screen.blit(global_data.SCREEN_IMAGE_GAME, (0, 0))

    def draw_analyze(self):
        if global_data.CV_RESULT is None:
            return

        _size = global_data.SCREEN_IMAGE_SIZE
        pts, w, h = global_data.CV_RESULT
        fix_w = w * global_data.SCREEN_SIZE[0] / _size[0]
        fix_h = h * global_data.SCREEN_SIZE[1] / _size[1]
        for pt in pts:
            fix_x = pt[0] * global_data.SCREEN_SIZE[0] / _size[0]
            fix_y = pt[1] * global_data.SCREEN_SIZE[1] / _size[1]
            pygame.draw.rect(self.screen, (255, 0, 0), (fix_x, fix_y, fix_w, fix_h), 1)

    def run_once(self):
        # 填充窗口颜色
        self.screen.fill(const.COLOR_BG)
        
        self.draw_capture()
        self.draw_analyze()
        _ctx = draw_context.DrawContext(self.screen, global_data.SCREEN_SIZE)
        self._ui_mgr.draw(_ctx)
        global_data.EFFECT_MGR.draw(_ctx)
        # 更新窗口
        pygame.display.update()


