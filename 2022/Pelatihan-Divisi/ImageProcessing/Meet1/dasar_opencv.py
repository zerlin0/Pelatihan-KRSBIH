import cv2 as cv
import numpy as np # matematik matrix

gmbr = cv.imread('1.jpg')
print(gmbr)
cv.imshow('Gambar Bola BGR', gmbr)

img_gray = cv.cvtColor(gmbr, cv.COLOR_BGR2GRAY)
cv.imshow('Gambar Bola HITAM PUTIH', img_gray)

img_xyz = cv.cvtColor(gmbr, cv.COLOR_BGR2XYZ)
cv.imshow('Gambar Bola XYZ', img_xyz)

cv.waitKey(0)
cv.destroyAllWindows()
