import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("Eu.jpg"))

if img is None: sys.exit("Could not read the image.")

cv.imshow("Image Display", img)
k = cv.waitKey(0)

if k == ord("j"): cv.imwrite("Eu.png", img)