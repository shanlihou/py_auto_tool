import os
import base_bot
import global_data


class BotMgr(object):
    def __init__(self):
        super(BotMgr, self).__init__()
        self.bot_name = None
        self.bot = None
        self.change_bot('Attack')

    def change_bot(self, bot_name):
        for i in os.listdir('src/bots'):
            sps = i.split('_')
            if len(sps) < 2 or sps[-1] != 'bot.py':
                continue

            if i == 'base_bot.py':
                continue

            mod_name = i[:-3]

            mod = __import__(mod_name)
            
            bot_cls = None
            for _cls in mod.__dict__.values():
                try:
                    is_sub = issubclass(_cls, base_bot.BotBase)
                except TypeError:
                    is_sub = False

                if not is_sub:
                    continue 

                bot_cls = _cls

            if bot_cls is None:
                continue

            print(bot_cls.__name__)
            if bot_cls.__name__ != bot_name:
                continue
        
            self.bot = bot_cls()
            self.bot_name = self.bot.__class__.__name__
            print('filter', mod)
            return

    def tick(self):
        if self.bot is None:
            return

        if global_data.BOT_NAME is not None:
            if global_data.BOT_NAME != self.bot_name:
                self.change_bot(global_data.BOT_NAME)

        self.bot.tick()

