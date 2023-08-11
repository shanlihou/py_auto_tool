import json
class Config(object):
    def __init__(self, filename):
        json_data = json.load(open(filename))
        for k, v in json_data.items():
            setattr(self, k, v)


CFG = Config('config.json')


