import cv2 as cv
import numpy as np
from pathlib import Path

IMG_DIR = Path(__file__).resolve().parents[1] / 'img'

img = cv.imread(str(IMG_DIR / 'pic1.png'), cv.IMREAD_GRAYSCALE)
img_1 = img[0:145, 0:400]
img_2 = img[150:300, 0:400]

cv.imshow('test', img_2)
cv.waitKey()

# SIFT检测器
sift = cv.SIFT_create()
kp1, dp1 = sift.detectAndCompute(img_1, None)
kp2, dp2 = sift.detectAndCompute(img_2, None)

# bf
bf = cv.BFMatcher()

# 使用 KNN 匹配
mtch = bf.knnMatch(dp1, dp2, k=2)

# 应用比率测试，筛选出好的匹配
g_mtch = []

for m, n in mtch:
    if m.distance < 0.75 * n.distance:
        g_mtch.append(m)
print(g_mtch)