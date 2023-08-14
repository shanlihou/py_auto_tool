import functools
import cv2
import global_data
import pygame


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
def get_origin_target_image(filename):
    filename = 'target/{}.png'.format(filename)
    return pygame.image.load(filename)


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


def is_pos_in_screen(pos):
    x, y = pos
    w, h = global_data.SCREEN_SIZE
    return 0 <= x < w and 0 <= y < h

def screen_pos_to_image_pos(pos):
    _size = global_data.SCREEN_SIZE
    _back_size = global_data.SCREEN_IMAGE_SIZE

    x = int(pos[0] * _back_size[0] / _size[0])
    y = int(pos[1] * _back_size[1] / _size[1])
    return x, y


def get_screen_pos(win_idx, pos_ratio):
    x, y = pos_ratio
    s_w, s_h = global_data.SCREEN_SIZE

    x = int(x * s_w)
    y = int(y * s_h)

    x += win_idx * s_w
    return x, y


def get_screen_rect(win_idx, rect_ratio):
    x, y, w, h = rect_ratio
    s_w, s_h = global_data.SCREEN_SIZE

    x = int(x * s_w)
    y = int(y * s_h)
    w = int(w * s_w)
    h = int(h * s_h)

    x += win_idx * s_w
    return x, y, w, h

@functools.lru_cache(maxsize=1)
def get_font(font_size):
    return pygame.font.Font('res/Teko-Bold.ttf', font_size)

