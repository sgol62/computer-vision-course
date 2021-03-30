# -*- coding: utf-8 -*-
"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import cv2

print('aktualna wersja OpenCV=', cv2.__version__)

image = cv2.imread(filename=r'../01_basics/images/nerka 1.bmp')

cv2.imshow(winname='test', mat=image)
cv2.waitKey(delay=0)