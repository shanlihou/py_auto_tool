import utils


class BotBase(object):
    def tick(self):
        _name = utils.get_state_name(self._STATE_CLS, self._state)
        _func_name = _name.lower() + "_act"
        func = getattr(self, _func_name, None)
        if func:
            func()

