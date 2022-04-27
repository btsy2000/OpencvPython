import cv2
import numpy as np
print("Package Imported")

img = cv2.imread("Resources/lambo.png")
print(img.shape)
imgResize = cv2.resize(img, (1000,800))
print(imgResize.shape)
imgCropped = img[0:200, 200:500]
print(imgCropped.shape)
cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)