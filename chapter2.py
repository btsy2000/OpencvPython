import cv2
import numpy as np
print("Package Imported")


img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
# imgBlur = cv2.blur(imgGray, (9,9), 0)
imgCanny = cv2.Canny(img, 100, 100)
imgCanny2 = cv2.Canny(img, 150, 200)
imgDilation = cv2.dilate(imgCanny2, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow( "GRAY IMAGE" ,imgGray)
cv2.imshow( "BLUR IMAGE" ,imgBlur)
cv2.imshow( "Canny IMAGE" ,imgCanny)
cv2.imshow( "Canny2 IMAGE" ,imgCanny2)
cv2.imshow( "Dilation IMAGE" ,imgDilation)
cv2.imshow( "Eroded IMAGE" ,imgEroded)
cv2.waitKey(0)