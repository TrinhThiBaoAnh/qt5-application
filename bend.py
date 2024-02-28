import cv2
import numpy as np

# load image
img = cv2.imread('input.jpg')
img  = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
# get image shape
height, width = img.shape[:2]

# create map_x and map_y arrays
map_x = np.zeros((height, width), np.float32)
map_y = np.zeros((height, width), np.float32)

# fill map_x array
for i in range(height):
    for j in range(width):
        map_x[i,j] = j

# fill map_y array
for i in range(height):
    for j in range(width):
        map_y[i,j] = i + 10 * np.sin(j * 2 * np.pi / 180)

# apply remap function to bend image vertically
bent_img = cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR)

# display the result
cv2.imshow('Bent Image', bent_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
