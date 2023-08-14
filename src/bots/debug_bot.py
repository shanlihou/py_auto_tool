import base_bot
import cv_helper
import global_data


class State(object):
    IDLE = 0


class DebugBot(base_bot.BotBase):
    _STATE_CLS = State
    def __init__(self):
        super(DebugBot, self).__init__()
        self._state = State.IDLE

    def idle_act(self):
        ret = cv_helper.get_multi_match(global_data.DEBUG_TARGET, global_data.DEBUG_SIM_RATIO)
        global_data.CV_RESULT = ret
        return

