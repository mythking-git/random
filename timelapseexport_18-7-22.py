import cv2
import numpy as np
import glob

fps = float(input("What fps?: "))

img_array = []
for filename in glob.glob('C:/Users/mikey/OneDrive/Documents/Coding/Python/CV2/Timelapse/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)


out = cv2.VideoWriter(f'timelapse-{str(fps)}fps.mov',cv2.VideoWriter_fourcc(*'MJPG'), fps, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
