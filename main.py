import sys
from threading import Thread

sys.path.append("./src")
sys.path.append("./src/common")
sys.path.append("./src/helper")
sys.path.append("./src/ui")
sys.path.append("./src/event")
sys.path.append("./src/effect")
sys.path.append("./src/bots")
sys.path.append("./src/deargui")
from config import CFG
from common import utils, const
from helper import wnd_helper, display_helper, cv_helper
import third_capture_helper
import global_data
import event_mgr
import effect_mgr
import attack_bot
import bot_mgr
import pygame


def cmd():
    while 1:
        _input = input('cmd: ')
        print(_input)


def init():
    global_data.EVENT_MGR = event_mgr.EventMgr()
    global_data.EFFECT_MGR = effect_mgr.EffectMgr()
    global_data.DLL_OPT = wnd_helper.WndHelper(const.DLL_PATH, CFG.process_cont, CFG.cls_cont, const.SCREEN_PATH)
    global_data.CLOCK = pygame.time.Clock()


def main():
    init()
    run_game()

def run_game():
    dp = display_helper.DisplayHelper()
    opt = third_capture_helper.ThirdCaptureHelper(CFG.title_cont, CFG.cls_cont)
    # opt = wnd_helper.WndHelper('./dll/back_preview_dll.dll', 'warspear', 'Warspear', const.SCREEN_PATH)
    bot = bot_mgr.BotMgr()
    while not global_data.DONE:
        if global_data.CAPTURE:
            opt.capture()

        bot.tick()
        global_data.EVENT_MGR.update()
        dp.run_once()
        global_data.CLOCK.tick(60)

    print('end')


if __name__ == '__main__':
    main()


