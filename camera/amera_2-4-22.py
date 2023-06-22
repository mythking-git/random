# importing cv2 and numpy library
import cv2
import numpy as np

lower = np.array([160,30,170],np.uint8)
upper = np.array([180,160,255],np.uint8)

def empty(i):
    pass

#cv2.namedWindow("Values")
#cv2.resizeWindow("Values", 640, 240)

#cv2.createTrackbar("Hue Min", "Values", 125, 180, empty)
#cv2.createTrackbar("Hue Max", "Values", 180, 180, empty)
#cv2.createTrackbar("Sat Min", "Values", 25, 255, empty)
#cv2.createTrackbar("Sat Max", "Values", 255, 255, empty)
#cv2.createTrackbar("Val Min", "Values", 0, 255, empty)
#cv2.createTrackbar("Val Max", "Values", 255, 255, empty)


# defining the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #hue_min = cv2.getTrackbarPos("Hue Min", "Values")
    #hue_max = cv2.getTrackbarPos("Hue Max", "Values")
    #sat_min = cv2.getTrackbarPos("Sat Min", "Values")
    #sat_max = cv2.getTrackbarPos("Sat Max", "Values")
    #val_min = cv2.getTrackbarPos("Val Min", "Values")
    #val_max = cv2.getTrackbarPos("Val Max", "Values")

    #lower = np.array([hue_min, sat_min, val_min])
    #upper = np.array([hue_max, sat_max, val_max])

    mask = cv2.inRange(hsv, lower, upper)
    blur = cv2.GaussianBlur(mask, (11,11), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    output = cv2.dilate(thresh, None, iterations=3)

    contours, hierachy = cv2.findContours(output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 700:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 3)
                    #cv2.putText(frame,"Area: "+str(int(cv2.contourArea(contour))), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7 , (0,255,0),2)




    cv2.imshow('original frame', frame)
    cv2.imshow('eroded image', output)

    # stop camera with wait key

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
