# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 13:45:37 2017

@author: Bortolaso
"""

import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = mpimg.imread('d:/exit-ramp.jpg')
plt.imshow(image)

gray=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
plt.imshow(gray, cmap="gray")

###Applying Gaussian Filter
kernel=5
gray_blur=cv2.GaussianBlur(gray,(kernel,kernel),0)
#plt.imshow(gray_blur, cmap="gray")

###Applying Canny 
low_threshold=70
high_threshold=170
edges=cv2.Canny(gray_blur,low_threshold,high_threshold)
plt.imshow(edges,cmap="Greys_r")

###Hough Space funtion
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 5
max_line_gap = 10
line_image = np.copy(image)*0 #creating a blank to draw lines on

# Run Hough on edge detected image
lines = cv2.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)


# Iterate over the output "lines" and draw lines on the blank
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

# Create a "color" binary image to combine with line image
color_edges = np.dstack((edges, edges, edges)) 

# Draw the lines on the edge image
combo = cv2.addWeighted(color_edges, 0.5, line_image, 1, 0) 
plt.imshow(combo)







