# Matthew Johnston - Senior Project Summer 2018

import cv2
import numpy as np

print("=====")
print("Video Restorer, Matthew Johnston")
print("=====")

# Get parameters from user
# input.mp4 parameters: 24fps, 0:36 duration
videoName = input('Enter the file name of the video including the file extension (myvideo.mp4): ')
duration = input('Enter the duration of the video in seconds: ')
framerate = input('Enter the frame rate of the video in frames per second: ')
frameSeq = ((int(duration)*int(framerate))-1)
timeStart = input('Enter the start of the corrupted segment (in seconds, enter \"0\" for the beginning of the video): ')
if int(timeStart) == 0:
    frameStart = 0
else:
    frameStart = ((int(timeStart)*int(framerate))-1)
timeEnd = input('Enter the start of the corrupted segment (in seconds, enter \"0\" for the end of the video): ')
if int(timeEnd) == 0:
    frameEnd = frameSeq
else:
    frameEnd = ((int(timeEnd)*int(framerate))-1)

# Reporting breakpoints
print("=====")
print("Capturing frame " + str(frameStart+1) + " to frame " + str(frameEnd+1))
print("=====")

# Takes in an input video
vid = cv2.VideoCapture("input/" + videoName)

# Begin at frameStart
currentFrame = frameStart
vid.set(1,currentFrame)

# Loop through until the end of the segment
# specified by the user
while(currentFrame <= frameEnd):
    ret, frame = vid.read()

    # Repairs frame and saves it in png file
    # (png is used for its lossless quality)
    name = './output/frame' + str(currentFrame) + '.png'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything is done, release the capture
vid.release()
cv2.destroyAllWindows()

# Take an image and apply a cleaning filter to it.
