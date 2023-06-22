import cv2
import numpy as np
import time
# Create a VideoCapture object
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# Capture a frame ret, img = cap.read()
# Release the capture cap.release()
nframes = 3400
interval = 180

for i in range(nframes):
    # capture
    ret, img = cap.read()
    # save file
    cv2.imwrite('./Timelapse/'+str(i).zfill(4)+'.png', img)
    print(str(i).zfill(4)+'.png - '+str(nframes-(i+1))+" remaining ("+str((nframes-(i+1))*interval)+"seconds).")
    # wait (interval) seconds
    time.sleep(interval)
