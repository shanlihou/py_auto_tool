import pygame
import sys

sys.path.append("./src")
sys.path.append("./src/common")
sys.path.append("./src/helper")
sys.path.append("./src/ui")
sys.path.append("./src/event")
sys.path.append("./src/effect")
sys.path.append("./src/bots")
from common import utils, const
from helper import wnd_helper, display_helper, cv_helper
import third_capture_helper
import global_data
import event_mgr
import effect_mgr
import attack_bot


def test_dll():
    opt = wnd_helper.WndHelper('./dll/back_preview_dll.dll', 'Telegram', 'Qt5159QWindowIcon', './tmp/current.png')
    opt.capture()      


def init():
    global_data.EVENT_MGR = event_mgr.EventMgr()
    global_data.EFFECT_MGR = effect_mgr.EffectMgr()
    global_data.DLL_OPT = wnd_helper.WndHelper('./dll/back_preview_dll.dll', 'warspear', 'Warspear', const.SCREEN_PATH)


def main():
    init()
    run_game()

def run_game():
    dp = display_helper.DisplayHelper()
    opt = third_capture_helper.ThirdCaptureHelper('Warspear', 'Warspear')
    # opt = wnd_helper.WndHelper('./dll/back_preview_dll.dll', 'warspear', 'Warspear', const.SCREEN_PATH)
    bot = attack_bot.Attack()
    while not global_data.DONE:
        opt.capture()
        bot.tick()
        global_data.EVENT_MGR.update()
        dp.run_once()


if __name__ == '__main__':
    main()


