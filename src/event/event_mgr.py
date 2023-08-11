import global_data
import pygame


class EventMgr(object):
    def __init__(self) -> None:
        self.cbs = {}

    def register_cb(self, event_type, cb):
        self.cbs.setdefault(event_type, []).append(cb)

    def trigger(self, event_type, *args, **kwargs):
        for cb in self.cbs.get(event_type, []):
            cb(*args, **kwargs)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global_data.DONE = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                _pos = pygame.mouse.get_pos()
                self.trigger(pygame.MOUSEBUTTONDOWN, _pos)


