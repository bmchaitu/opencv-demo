import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#EROSION
img = cv.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv.erode(img,kernel,iterations = 1)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.savefig('./Morphology/Erosion.jpg')


#DILATION
img = cv.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
dilute = cv.dilate(img,kernel, iterations=1)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilute),plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.savefig('./Morphology/Dilation.jpg')

#IMAGE OPENING(EROSION+DILUTION) OPERATION
img = cv.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(opening),plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.savefig('./Morphology/Image_opening.jpg')


#CLOSING(DILUTION+EROSION) OPERATIONS
img = cv.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(closing),plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.savefig('./Morphology/ImageClosing.jpg')

#MORPHOLOGICAL GRADIENT
img = cv.imread('j.png',0)
kernel = np.ones((5,5),np.uint8)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gradient),plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.savefig('./Morphology/MorphologicalGradient.jpg')


