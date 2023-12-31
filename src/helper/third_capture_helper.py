from PyQt5.QtWidgets import QApplication
import win32gui
import win32con
import const
import pygame
import global_data
import cv2


class ThirdCaptureHelper(object):
    def __init__(self, title, cls_name) -> None:
        super().__init__()
        self._title = title
        self._cls_name = cls_name
        self._hwnd = None

        self.app = QApplication(['WindowCapture'])
        self.screen = QApplication.primaryScreen()

        self.get_wnd()

    def get_wnd(self):
        _desk = win32gui.GetDesktopWindow()
        _next = win32gui.GetWindow(_desk, win32con.GW_CHILD) # 获取桌面第一个子窗口句柄
        _hwnd = None
        while 1:
            if not _next:
                break

            _text = win32gui.GetWindowText(_next) # 获取窗口标题
            _class_name = win32gui.GetClassName(_next) # 获取窗口类名
            if self._title in _text and self._cls_name in _class_name: # 判断窗口标题和类名是否符合
                _hwnd = _next
                break

            _next = win32gui.GetWindow(_next, win32con.GW_HWNDNEXT) # 从上一个窗口句柄开始，获取下一个窗口句柄

        print(_hwnd)
        # 
        self._hwnd = _hwnd
        global_data.HWND = _hwnd

    def capture(self):
        self.screen.grabWindow(self._hwnd).save(const.SCREEN_PATH, 'png')
        cur_img = pygame.image.load(const.SCREEN_PATH)
        global_data.SCREEN_IMAGE_SIZE = cur_img.get_size()
        global_data.ORIGIN_IMAGE = cur_img
        global_data.SCREEN_IMAGE_GAME = pygame.transform.scale(cur_img, global_data.SCREEN_SIZE)

        screen_img = cv2.imread(const.SCREEN_PATH)
        global_data.SCREEN_IMAGE_CV = cv2.cvtColor(screen_img, cv2.COLOR_BGR2GRAY)


def main():
    pass



if __name__ == '__main__':
    main()
