import cv2

# Get parameters from user
videoName = input('Enter the file name of the video including the file extension (myvideo.mp4): ')
framerate = input('Enter the frame rate of the video: ')
timeStart = input('Enter the start of the corrupted segment (in seconds, enter \"0\" for the beginning of the video): ')
frameStart = int(timeStart)*int(framerate)
timeEnd = input('Enter the start of the corrupted segment (in seconds, enter \"-1\" for the end of the video): ')
frameEnd = int(timeEnd)*int(framerate)

#print("The start of the corrupted segment is frame " + str(frameStart))
#print("The end of the corrupted segment is frame " + str(frameEnd))

# Takes in an input video and coverts it to a sequence of png images.
#currentFrame = 0
#vid = cv2.VideoCapture("input.mp4")

#while(True):
    # Capture frame-by-frame
#    ret, frame = vid.read()

    # Saves image of the current frame in png file
    # png is used for its lossless quality
#    name = './output/frame' + str(currentFrame) + '.png'
#    print ('Creating...' + name)
#    cv2.imwrite(name, frame)

    # To stop duplicate images
#    currentFrame += 1

# When everything is done, release the capture
#vid.release()
#cv2.destroyAllWindows()

# Take an image and apply a cleaning filter to it.
