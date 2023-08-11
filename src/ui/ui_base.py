import utils


class UIBase(object):
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
