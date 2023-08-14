import base_bot


class State(object):
    IDLE = 0


class DebugBot(base_bot.BotBase):
    def __init__(self):
        super(DebugBot, self).__init__()
        self._state = State.IDLE

    def tick(self):
        pass
