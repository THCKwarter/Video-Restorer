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
# Get parameters from user
# vid.mp4 parameters: 1920x1080, 24fps, 0:36 duration
videoName = input('Enter the file name of the video including the file extension (myvideo.mp4): ')
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
#vRes = int(input("Enter the vertical resolution of the video in pixels: "))
#hRes = int(input("Enter the horizontal resolution of the video in pixels: "))
#outFile = input("Enter the output name of the video without a file extension: ")

# Selecting a repair method
print("==============================")
print("Select a repair method by typing only the number: ")
print("==============================")
print("1 - Denoise")
print("2 - Deblur")
print("==============================")
method = int(input('Your selection: '))
print("==============================")
if method == 1:
    print("Denoising selected.")
elif method == 2:
    print("Debluring selected.")
    #unsharp_strength = 0.8
    #blur_size = 8 # Standard deviation in pixels
    psf = np.ones((5,5)) / 25
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

# Get output file name
#filename = input("Enter the output file name without the file extension: ")
out = cv2.VideoWriter('./output/restored.avi',fourcc, 24.0, (1920,1080))
#out = cv2.VideoWriter('./output/' + outFile + '.avi',fourcc, 24.0, (vRes,hRes))

# ==========================
# Filters
# ==========================

# Loop through until the end of the segment
# specified by the user
while(currentFrame <= frameEnd):
    ret, frame = vid.read()

    # Repairs frame and saves it in png file
    # (png is used for its lossless quality)
    progressReport = ("Processing frame: " + str(currentFrame))
    print(progressReport, end="\r")

    # Pick filter based on user input
    if method == 1:
        # Denoise filter
        fixed = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
    elif method == 2:
        # Deblur filter
        #gass = cv2.GaussianBlur(frame, (9,9), 10.0)
        #fixed = cv2.addWeighted(frame, 1.5, gass, -0.5, 0, frame)
        #Scikit Image method
        #frame = img_as_float(frame)
        #blurred = skimage.filters.gaussian(frame, blur_size)
        #highpass = frame - unsharp_strength * blurred
        #fixed = frame + highpass

        frame = color.rgb2gray
        frame = convolve2d(frame, psf, 'same')
        frame += 0.1 * frame.std() * np.random.standard_normal(frame.shape)
        fixed = skimage.restoration.unsupervised_wiener(frame, psf)
    elif method == 3:
        print("other")

    
    out.write(fixed)

    # Individual image writing (Troubleshooting)
    #name = './output/frame' + str(currentFrame) + '.png'
    #cv2.imwrite(name, fixed)

    # To stop duplicate images
    currentFrame += 1

# When everything is done, release the capture
print("Restoration complete. Outputting video.")
print("==============================")
vid.release()
out.release()
cv2.destroyAllWindows()