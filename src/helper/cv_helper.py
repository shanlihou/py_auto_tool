import cv2
import numpy as np
import global_data
import const
import utils


def get_target_pos():
    screen_img = cv2.imread('./tmp/current.png')
    target = cv2.imread('./target/test.png')
    res = cv2.matchTemplate(target, screen_img, cv2.TM_SQDIFF_NORMED)
    loc = np.where(res < 0.1)
    pts = []
    for pt in zip(*loc[::-1]):
        # print(pt)
        pts.append(pt)

    return pts

def get_multi_match(target_path, threshold=0.9):
    target = utils.get_cap_target_cv_img(target_path)

    w, h = target.shape[::-1]
    res = cv2.matchTemplate(global_data.SCREEN_IMAGE_CV, target, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)
    pts = []
    for pt in zip(*loc[::-1]):
        pts.append(pt)

    return pts, w, h
