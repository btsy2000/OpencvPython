import cv2
import numpy as np
print("Package Imported")

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

myColors = [[5, 136, 123, 26, 255, 255],
            [83, 74, 0, 136, 189, 255],
            [163, 74, 0, 179, 189, 255]]
myColorsValues = [[102,178,255], [255,0,0], [0,0,255]]  ##BGR
myPoints = [] ##  [x, y, myColorId]

def findColors(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        # result = cv2.bitwise_and(img, img, mask=mask)
        # cv2.imshow(str(color[0]), result)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorsValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h,count = 0,0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def drawOnCanvas(myPoints, myColorsValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorsValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColors(img, myColors)
    if len(newPoints) !=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) !=0:
        drawOnCanvas(myPoints,myColorsValues)
    cv2.imshow("Image", imgResult)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

