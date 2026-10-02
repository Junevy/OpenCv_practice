# rotated template match

import cv2 as cv
import numpy as np
from pathlib import Path

IMG_DIR = Path(__file__).resolve().parents[1] / 'img'
import matplotlib.pyplot as plt

img = cv.imread(str(IMG_DIR / 'cards.png'), cv.IMREAD_GRAYSCALE)
tmp_img = cv.imread(str(IMG_DIR / 'poker.png'), cv.IMREAD_GRAYSCALE)

roi = img[120:250, 333:420]
tmp_resize = cv.resize(tmp_img, (roi.shape[1], roi.shape[0]))

def rotate_img(img, angle):
    h, w = img.shape[:2]
    # 原图中心
    cx, cy = w / 2, h / 2
    # 旋转矩阵
    M = cv.getRotationMatrix2D((cx, cy), angle, 1.0)
    # 取旋转矩阵中的 cos、sin
    cos = abs(M[0, 0])
    sin = abs(M[0, 1])
    # 计算旋转后的新画布大小
    new_w = int(h * sin + w * cos)
    new_h = int(h * cos + w * sin)
    # 修正平移量，让旋转后的图像位于新画布中心
    M[0, 2] += new_w / 2 - cx
    M[1, 2] += new_h / 2 - cy
    rotated = cv.warpAffine(img, M, (new_w, new_h))
    msk = np.full((h, w), 255, dtype=np.uint8)
    rotated_msk = cv.warpAffine(msk, M, (new_w, new_h), flags=cv.INTER_NEAREST, borderValue=0)
    return rotated, rotated_msk

def match(img, t_img, score):
    h, w = t_img.shape[:2]
    ret = cv.matchTemplate(img, t_img, cv.TM_CCOEFF_NORMED)
    loc = np.where(ret > score)

    for pt in zip(*loc[::-1]):
        for pt in zip(*loc[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0))
    return None

# tt_img = rotate_img(tmp_resize, 160)
# plt.imshow(tt_img)

# scr = 0.4
# agl = [a for a in range(0,180)]

# for a in agl:
#     r_img = rotate_img(tmp_resize, a)
#     ret = match(img, r_img, scr)
# plt.imshow(img, cmap='gray')

scores = []

# r_img, r_msk = rotate_img(tmp_resize, 30)
# cv.imshow('test', r_msk)
# cv.waitKey()

for angle in range(360):
    r_img, r_msk = rotate_img(tmp_resize, angle)

    ret = cv.matchTemplate(
        img,
        r_img,
        cv.TM_CCOEFF_NORMED,
        r_msk
    )
    scores.append((angle, ret.max()))

scores.sort(key=lambda x: x[1], reverse=True)

print(scores[:20])
