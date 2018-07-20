import cv2

# Denoise image
image = cv2.imread("noisy.png")
dst = cv2.fastNlMeansDenoisingColored(image,None,10,10,31,63)
cv2.imwrite("output/denoised0.png", dst)