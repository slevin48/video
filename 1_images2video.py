# 1. Images 2 Video 🎥

# %%
import cv2
import numpy as np
import glob
import os


# %%
folder = 'images/gta1/' # 100 images


# %%
# The first image determines the size of the video to be created
files = os.listdir(folder)
img = cv2.imread(folder+files[0])
img
height, width, layers = img.shape
size = (width,height)
size


# %%
# Build an array of size 
img_array = []
for filename in glob.glob(folder+'*.png'):
    img = cv2.imread(filename)
    # height, width, layers = img.shape
    # size = (width,height)
    img_array.append(img)


# %%
# Create video
video_name = 'gta1'
out = cv2.VideoWriter(video_name+'.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


