import utils
import cv_helper
import global_data
import back_opt_helper as BOH
import base_bot
import const
import time


class State(object):
    IDLE = 0
    ATTACKING = 1
    PICK = 2
    NEXT_PAGE = 3
    WAIT_PICK_MISS = 4
    AFTER_DIE = 5
    WAIT_DIE_MISS = 6


class Attack(base_bot.BotBase):
    _STATE_CLS = State
    def __init__(self):
        super(Attack, self).__init__()
        self._state = State.IDLE
        self._flag_time = 0

    def idle_act(self):
        print('idle_act')
        ret = cv_helper.get_multi_match('jingling', 0.9)
        global_data.CV_RESULT = ret

        pts, w, h = ret
        if not pts:
            return
        print(pts[0])

        x = int(pts[0][0] + w / 2)
        y = int(pts[0][1] + h / 2)
        BOH.click((x, y))
        # global_data.DLL_OPT.click(x, y)

        screen_pos = utils.back_pos_to_screen((x, y))
        global_data.EFFECT_MGR.add_click_effect(screen_pos)
        self._state = State.ATTACKING
        self._flag_time = time.time()

    def attacking_act(self):
        print('attacking_act')
        ret = cv_helper.get_multi_match('in_attack', 0.9)
        global_data.CV_RESULT = ret

        pts, w, h = ret
        if pts:
            self._flag_time = time.time()

        if time.time() - self._flag_time > 2:
            self._state = State.AFTER_DIE
            self._flag_time = time.time()

    def after_die_act(self):
        print('after_die_act')
        ret = cv_helper.get_multi_match('next_page', 0.9)
        next_pts, w, h = ret
        if next_pts:
            self._state = State.PICK
            self._flag_time = time.time()
            return

        if time.time() - self._flag_time > 5:
            self._state = State.IDLE
            self._flag_time = time.time()
            return

        ret = cv_helper.get_multi_match('hand', 0.9)
        global_data.CV_RESULT = ret

        pts, w, h = ret
        if not pts:
            ret = cv_helper.get_multi_match('die', 0.9)
            global_data.CV_RESULT = ret

            pts, w, h = ret

        if not pts:
            return

        x = int(pts[0][0] + w / 2)
        y = int(pts[0][1] + h / 2)
        BOH.click((x, y))

        screen_pos = utils.back_pos_to_screen((x, y))
        global_data.EFFECT_MGR.add_click_effect(screen_pos)
        
    def wait_die_miss_act(self):
        print('wait_die_miss_act')
        ret = cv_helper.get_multi_match('die', 0.9)
        global_data.CV_RESULT = ret

        pts, w, h = ret
        if pts:
            self._flag_time = time.time()

        if time.time() - self._flag_time > 5:
            self._state = State.IDLE

    def pick_act(self):
        print('pick_act')
        ret = cv_helper.get_multi_match('next_page', 0.9)
        global_data.CV_RESULT = ret

        pts, w, h = ret
        if not pts:
            if time.time() - self._flag_time > 5:
                self._state = State.WAIT_DIE_MISS
                self._flag_time = time.time()
            return

        x = int(pts[0][0] + w / 2)
        y = int(pts[0][1] + h / 2)
        BOH.click((x, y))

        screen_pos = utils.back_pos_to_screen((x, y))
        global_data.EFFECT_MGR.add_click_effect(screen_pos)
        self._state = State.IDLE



