import numpy as np
import cv2

image = cv2.imread("img_1.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
kontur,b = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_ITALIC


for i in kontur:
    e = 0.01*cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i,e,True)
    cv2.drawContours(image,[approx],0,(0,0,255),2)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    print(len(approx))

    if len(approx) ==3:
            cv2.putText(image,"TRIANGLE",(x,y),font,1,(0,0,0),4)
    elif len(approx) == 4:
            cv2.putText(image, "QUADRANGLE", (x, y), font, 1, (0, 0, 0), 4)
    elif len(approx) == 5:
            cv2.putText(image, "PENTAGON", (x, y), font, 1, (0, 0, 0), 4)
    else:
            cv2.putText(image,"CIRCLE",(x,y),font,1,(0,0,0),4)

cv2.imshow("sekiller",image)
cv2.waitKey(0)
cv2.destroyAllWindows()