"""
@author: krakowiakpawel9@gmail.com
@site: e-smartdata.org
"""

import cv2
import numpy as np

original_img = cv2.imread(filename=r'C:\Users\User\PycharmProjects\computer-vision-course\01_basics\images\nerka 1.bmp')
img = original_img.copy()

# cv2.imshow(winname='logo', mat=img)
# cv2.waitKey(0)
# #informacja o pliku
height, width = img.shape[:2]
print(f'Wysokość: {height}px')
print(f'Szerokość: {width}px')
print(f'Rozmiar pliku: {img.size/1000}kB')

# ----------
# ---line---
# ----------

# partition = 108 # parametr podziału
# xWidth = width/partition
# xstepWidth = int((xWidth - int(xWidth//1))*partition/2) # wyśrodkowanie po X
# yHeight = height/partition
# ystepHeight = int((yHeight - int(yHeight//1))*partition/2)# wyśrodkowanie po Y
# print(f'podział={partition}px\nprzesunięcie po X={xstepWidth}px\nprzesunięcie po Y={ystepHeight}px')
# for i in range(1+int(xWidth//1)):
#     cv2.line(img=img, pt1=(xstepWidth+partition*i, 0), pt2=(xstepWidth+partition*i, height), color=(0, 0, 0), thickness=1, lineType=16)
# for i in range(1+int(yHeight//1)):
#     cv2.line(img=img, pt1=(0, ystepHeight+partition*i), pt2=(width, ystepHeight+partition*i), color=(0, 0, 0), thickness=1, lineType=16)
#
# cv2.imshow(winname='logo', mat=img)
# cv2.waitKey(0)

# ---------------
# ---rectangle---
# ---------------

# img = original_img.copy()
# cv2.rectangle(img=img, pt1=(200, 50), pt2=(400, 230), color=(255, 0, 0), thickness=3)
# cv2.imshow('logo', img)
# cv2.waitKey(0)

# ------------
# ---circle---
# ------------
# img = original_img.copy()
# cv2.circle(img=img, center=(300, 140), radius=90, color=(0, 0, 255), thickness=3)
# cv2.imshow('logo', img)
# cv2.waitKey(0)

# -------------
# ---polygon---
# -------------
# img = original_img.copy()
# pts = np.array([[300, 140], [200, 200], [200, 50], [300, 50]], dtype='int32').reshape((-1, 1, 2))
# cv2.polylines(img=img, pts=[pts], isClosed=False, color=(0, 255, 0), thickness=3)
# cv2.imshow('logo', img)
# cv2.waitKey(0)

# -------------
# ---polygon---
# -------------
# img = original_img.copy()
# pts = np.array([[300, 140], [200, 200], [200, 50], [300, 50]], dtype='int32').reshape((-1, 1, 2))
# cv2.polylines(img=img, pts=[pts], isClosed=True, color=(0, 255, 0), thickness=3)
# cv2.imshow('logo', img)
# cv2.waitKey(0)

# ----------
# ---text---
# ----------
import os
img = original_img.copy()
cv2.putText(
    img=img,
    text='Python nerka1',
    org=(20, 40),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1.5,
    color=(0, 0, 0),
    thickness=2
)

cv2.imshow('logo', img)
directory = r'C:\Users\User\PycharmProjects\computer-vision-course\01_basics\images'
os.chdir(directory) #dostęp do katalogu
cv2.imwrite('zapis.bmp', img) # zapis pliku
print(os.listdir(directory))
cv2.waitKey(0)
