import cv2
import numpy as np
import matplotlib.pyplot as plt
img1 = cv2.imread('lena.jpg')
img_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
blank_img = np.zeros(shape=(img_rgb.shape[0],img_rgb.shape[1],3), dtype=np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,
            text='DO NOT COPY',
            org=(img_rgb.shape[1]//8, img_rgb.shape[0]//2),
            fontFace=font,
            fontScale= 2,color=(255,125,0),
            thickness=5,
            lineType=cv2.LINE_4)
blended = cv2.addWeighted(src1=img_rgb,alpha=0.7,src2=blank_img,beta=1, gamma = 0)
cv2.imwrite('./WaterMark/watermark.jpg', blended)

