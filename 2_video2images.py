# 2. Video 2 images 🖼️

# %%
import cv2
import os


# %%
path = 'videos/tesla2.mp4'
out_folder = 'images/tesla2/'
try:
    os.mkdir(out_folder)
except ValueError:
    print('the output folder already exists')


# %%
def getFrame(out_folder,vidcap,sec,count):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(out_folder+"img_"+str(count)+".png", image)     # save frame as PNG file
    return hasFrames


# %%
vidcap = cv2.VideoCapture(path)
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(out_folder,vidcap,sec,count)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(out_folder,vidcap,sec,count)


