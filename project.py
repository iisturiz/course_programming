"""
This script is for image analysis
"""
from readlif.reader import LifFile
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import cv2

# Reading a LIF file
 new = LifFile('/Users/iisturizpetitj/Desktop/20211223_P1_MCF7 #1.lif')
 im =new.get_image(0)
#Image info
 new.get_image()

#for loop that still does not work for all channels, so it's commented

# name=['channel_1','channel_2','channel_3']
# for i in range(3):
#  name[i]=im.get_frame(0,0,i,0)

# get_frame(z=0, t=0, c=0, m=0)
# z (int) – z position
# t (int) – time point
# c (int) – channel
# m (int) – mosaic image
 #print(i)
  
#Example with one channel
imm=im.get_frame(0,0,2,0)
channel_1 = plt.imshow(imm)
plt.show()
#read image into matrix.
m =  cv2.imread(channel_1)

# # get image properties.
# h,w,bpp = np.shape(m)

# # print pixel value
# y = 1
# x = 1
# print (m[y][x])
