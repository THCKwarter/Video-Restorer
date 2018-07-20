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

# Selecting a repair method
# method = input('Select a repair method by typing the number. 1 - Denoise, 2 - Deblur')

# Reporting breakpoints
print("=====")
print("Capturing frame " + str(frameStart) + " to frame " + str(frameEnd))
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
    print ('Repairing frame ' + str(currentFrame))
    fixed = cv2.fastNlMeansDenoisingColored(frame,None,10,10,7,21)
    name = './output/frame' + str(currentFrame) + '.png'
    cv2.imwrite(name, fixed)

    # To stop duplicate images
    currentFrame += 1

# When everything is done, release the capture
vid.release()
cv2.destroyAllWindows()