import heapq
import time



class TimerObj(object):
    def __init__(self, end_time, callback):
        self.callback = callback
        self.end_time = end_time

    def __lt__(self, other):
        return self.end_time < other.end_time


class Timer(object):
    def __init__(self):
        self.timer_heap = []

    def add_timer(self, delay, callback):
        end_time = time.time() + delay
        timer_obj = TimerObj(end_time, callback)
        heapq.heappush(self.timer_heap, timer_obj)

    def update(self):
        pass
        
