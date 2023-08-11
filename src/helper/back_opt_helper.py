import win32api
import global_data
import win32con
import time



def click(pos):
    long_position = win32api.MAKELONG(pos[0], pos[1])#模拟鼠标指针 传送到指定坐标
    win32api.PostMessage(global_data.HWND, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
    win32api.PostMessage(global_data.HWND, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起

