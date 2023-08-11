import functools
import cv2
import global_data


def bit_set(value, bit):
    return value | (1 << bit)

def bit_clear(value, bit):
    return value & ~(1 << bit)

def get_state_name(state_cls, state):
    for k, v in state_cls.__dict__.items():
        if v == state:
            return k

    return None

@functools.lru_cache(maxsize=1024)
def get_cap_target_cv_img(filename):
    filename = 'target/{}.png'.format(filename)
    return cv2.imread(filename, cv2.IMREAD_GRAYSCALE)


def back_pos_to_screen(pos):
    _size = global_data.SCREEN_SIZE
    _back_size = global_data.SCREEN_IMAGE_SIZE

    x = int(pos[0] * _size[0] / _back_size[0])
    y = int(pos[1] * _size[1] / _back_size[1])
    return x, y

