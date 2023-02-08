import cv2
import numpy as np

#for loop to process all the data in the 'images' folder
import os
path = '/Users/amosam/Documents/School/juniorsem4/SDAIA Hackathon/dataset/dataset/images/'
images = []
for filename in os.listdir(path):
    img = cv2.imread(path+filename)
    if img is not None:
        images.append(img)

#Reading the properties of the images       
for i in range(len(images)):
    if images[i] is None:
        images.pop(i)

#Data formatting
gray_images = []
for i in range(len(images)):
    gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    gray_images.append(gray)

#Data normalization
norm_images = []
for i in range(len(gray_images)):
    img = gray_images[i]/255.0
    norm_images.append(img)

#Data Augmentation
augmented_images = []
for i in range(len(norm_images)):
    img = norm_images[i]
    rows,cols = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    augmented_images.append(cv2.warpAffine(img,M,(cols,rows)))
