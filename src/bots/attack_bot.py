import utils
import cv_helper
import global_data
import back_opt_helper as BOH


class State(object):
    IDLE = 0
    ATTACKING = 1


class Attack(object):
    def __init__(self):
        self._state = State.IDLE

    def tick(self):
        _name = utils.get_state_name(State, self._state)
        _func_name = _name.lower() + "_act"
        func = getattr(self, _func_name, None)
        if func:
            func()

    def idle_act(self):
        ret = cv_helper.get_multi_match('die_jingling', global_data.DEBUG_SIM_RATIO)
        global_data.CV_RESULT = ret
        return

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


