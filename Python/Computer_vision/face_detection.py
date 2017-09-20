import cv2
from cv2 import *
import numpy as np

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

fname='photo.jpg'
img = imread(fname)
gray = imread(fname, CV_LOAD_IMAGE_GRAYSCALE)

gray = np.array(gray, dtype='uint8')

faces=face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

cv2.imshow("Gray",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
