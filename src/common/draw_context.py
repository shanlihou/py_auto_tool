
class DrawContext(object):
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size

    def rect_by_ratio(self, x, y, w, h):
        return (x * self.size[0], y * self.size[1], w * self.size[0], h * self.size[1])

