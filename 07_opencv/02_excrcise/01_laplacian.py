import cv2
import numpy as np

cv2.namedWindow('test', cv2.WINDOW_NORMAL)
img = cv2.imread('07_opencv/img/img1.jpg', cv2.IMREAD_GRAYSCALE)
roi_img = img[600:2000, 3000:4000]
lap_value = cv2.Laplacian(roi_img, cv2.CV_64F).var()
print(f'before gaussian blur: {lap_value}')

for k in [3,7,11,15,19,23]:
    # gaussian blur
    gas_img = cv2.GaussianBlur(roi_img, (k,k), 0)
    lap_value = cv2.Laplacian(gas_img, cv2.CV_64F).var()
    print(f'after gaussian blur __ {k}: {lap_value}')

# 3000-4000, 600-2000
cv2.imshow('test', gas_img)
cv2.waitKey()
cv2.destroyAllWindows()