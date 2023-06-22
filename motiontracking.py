import cv2
import numpy as np
import time
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 854)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
while True:
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        if cv2.contourArea(contour) > 2000:
            x, y, w, h = cv2.boundingRect(contour)

            now = datetime.now()

            cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
            #cv2.drawContours(frame1, contours, -1, (255,0,0), 3)
            cv2.putText(frame1,"Area: "+str(int(cv2.contourArea(contour))), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.3 , (0,255,0),2)
            image = cap.read()
            cv2.imwrite(f'C:/Users/mikey/OneDrive/Documents/Coding/Python/CV2/MotionTracking/{now.strftime("%b-%d-%Y %H;%M;%S")}.png', frame1)


    image = cv2.resize(frame1, (1280,720))
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    key = cv2.waitKey(300)

    if key == ord('q'):
        break




cv2.destroyAllWindows()
cap.release()
