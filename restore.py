# Matthew Johnston - Senior Project Summer 2018
# ==========================
# Imports
# ==========================
import os
clear = lambda: os.system('cls')
clear()

print("Loading packages, please wait.")
import cv2
import numpy as np
import skimage
from skimage import color, data, filters, img_as_float, restoration
from scipy.signal import convolve2d
import sys

clear()

print("==============================")
print("Matthew Johnston")
print("Senior Project Summer 2018")
print("Video Restorer")
print("==============================")

# ==========================
# Parameters
# ==========================
videoName = input('Enter the file name of the video including the file extension (myvideo.mp4): ')
vRes = int(input("Enter the vertical resolution of the video in pixels: "))
hRes = int(input("Enter the horizontal resolution of the video in pixels: "))
duration = int(input('Enter the duration of the video in seconds: '))
framerate = int(input('Enter the frame rate of the video in frames per second: '))
frameSeq = ((duration*framerate)-1)
timeStart = int(input('Enter the start of the corrupted segment (in seconds, enter \"0\" for the beginning of the video): '))
if timeStart == 0:
    frameStart = 0
else:
    frameStart = ((timeStart*framerate)-1)
timeEnd = int(input('Enter the start of the corrupted segment (in seconds, enter \"0\" for the end of the video): '))
if timeEnd == 0:
    frameEnd = frameSeq
else:
    frameEnd = ((timeEnd*framerate)-1)
outFile = input("Enter the output name of the video without a file extension: ")

# Selecting a repair method
print("==============================")
print("Select a repair method by typing only the number: ")
print("==============================")
print("1 - Noise / Artifacting")
print("2 - Blur")
print("==============================")
method = int(input('Your selection: '))
print("==============================")
if method == 1:
    print("Denoising selected.")
elif method == 2:
    print("Debluring selected.")
    psf = (np.ones((5,5)) / 25)
elif method == 3:
    print("Other")

# ==========================
# Setting Up For Repair
# ==========================

# Reporting breakpoints
print("==============================")
print("Capturing frame " + str(frameStart) + " to frame " + str(frameEnd))
print("==============================")

# Takes in an input video
vid = cv2.VideoCapture("input/" + videoName)

# Begin at frameStart
currentFrame = frameStart
vid.set(1,currentFrame)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# Set output file name
out = cv2.VideoWriter('./output/' + outFile + '.avi',fourcc, framerate, (vRes,hRes))

# ==========================
# Filters
# ==========================

# Loop through until the end of the segment
# specified by the user
while(currentFrame <= frameEnd):
    ret, frame = vid.read()

    # Repairs frame and saves it in png file
    # (png is used for its lossless quality)
    progressReport = ("Currently processing frame: " + str(currentFrame))
    print(progressReport, end="\r")

    # Pick filter based on user input
    if method == 1:
        # Denoise/artifacting filter
        fixed = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
    elif method == 2:
        # Deblur filter
        frame = frame.astype(np.float32) / 255.0
        for i in range(frame.shape[-1]):
            frame[:,:,i] = convolve2d(frame[:,:,i], psf, mode='same')
        frame += 0.1 * frame.std() * np.random.standard_normal(frame.shape)
        fixed = np.zeros(frame.shape)
        for i in range(frame.shape[-1]):
            fixed[:,:,i], _ = skimage.restoration.unsupervised_wiener(frame[:,:,i], psf)
        fixed = np.clip(fixed * 255.0,0,255).astype(np.uint8)
    elif method == 3:
        print("other")

    
    out.write(fixed)

    # To stop duplicate images
    currentFrame += 1

# When everything is done, release the capture
print("Restoration complete. Outputting video.")
print("==============================")
vid.release()
out.release()
cv2.destroyAllWindows()