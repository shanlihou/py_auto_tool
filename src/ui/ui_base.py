import utils


class UIBase(object):
    def __init__(self, win_idx, rect):
        super(UIBase, self).__init__()
        self.win_idx = win_idx
        self.rect = rect
        self.id = 0
        self.is_visible = True

    def set_visible(self, is_visible):
        self.is_visible = is_visible

    def set_id(self, id):
        self.id = id

    def is_pos_in(self, pos):
        _x = pos[0]
        _y = pos[1]

        _rect = utils.get_screen_rect(self.win_idx, self.rect)
        _left = _rect[0]
        _right = _left + _rect[2]
        _top = _rect[1]
        _bottom = _top + _rect[3]

        if _x > _left and _x < _right and _y > _top and _y < _bottom:
            return True

        return False
