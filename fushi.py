import cv2
import numpy as np
from PIL import Image

kernel1= cv2.getStructuringElement(cv2.MORPH_RECT, (14,14))#以14*20的核做腐蚀
kernel2 =cv2.getStructuringElement(cv2.MORPH_RECT, (10 , 7))#背景膨胀核
kernel3 =cv2.getStructuringElement(cv2.MORPH_RECT, (2 , 2))#文字膨胀核
for threshold in range(100, 240, 20):
    img = cv2.imread('G:\\'+str(threshold)+'.png')
    iFushi = cv2.morphologyEx(img,cv2.MORPH_DILATE, kernel1)#腐蚀
    iPengzhang =cv2.morphologyEx(iFushi, cv2.MORPH_DILATE, kernel2)#膨胀背景
    jian = np.abs(iPengzhang - img)#和原图相减
    iWenzi =cv2.morphologyEx(jian, cv2.MORPH_DILATE, kernel3)#膨胀文字
    cv2.imwrite('G:\\fs'+str(threshold)+'.png', iWenzi)
