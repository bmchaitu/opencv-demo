import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#CONVOLUTION USING A KERNAL
img = cv.imread('lena.jpg')
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.savefig('./Image_filter/convolution.jpg')

#IMAGE BLURRING
img = cv.imread('lena.jpg')
blur = cv.blur(img,(5,5))
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.savefig('./Image_filter/Image_blur.jpg')

#GAUSSIAN BLURRING: USING A SPECIAL KERNEL
img = cv.imread('lena.jpg')
blur = cv.GaussianBlur(img,(5,5),0)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.savefig('./Image_filter/Gauss_blur.jpg')

#MEDIAN BLURRING
img = cv.imread('lena.jpg')
median = cv.medianBlur(img,5)
plt.subplot(121), plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.savefig('./Image_filter/median_blur.jpg')

#BILATERAL FILTERING
img = cv.imread('lena.jpg')
blur = cv.bilateralFilter(img,9,75,75)
plt.subplot(121), plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.savefig('./Image_filter/bilateral.jpg')
