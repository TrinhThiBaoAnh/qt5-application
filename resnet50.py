# import cv2

# img_to_insert = cv2.imread('input/avt.png')

# height, width = img_to_insert.shape[:2]

# angle = -9.46
# rotation_matrix = cv2.getRotationMatrix2D((int(width), int(height)), angle, 1)
# img_rotated = cv2.warpAffine(img_to_insert, rotation_matrix, (int(width*1.5), int(height*1.5)))
# height, width = img_rotated.shape[:2]

# (x,y) = (80, 375)
# img_target = cv2.imread('phoi/photo1682182014.jpeg')
# img_target = cv2.resize(img_target, (960//2, 1280//2))
# roi = img_target[y:y+height, x:x+width]

# img2gray = cv2.cvtColor(img_rotated,cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)

# img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
# img2_fg = cv2.bitwise_and(img_rotated,img_rotated,mask=mask)

# dst = cv2.add(img1_bg,img2_fg)
# img_target[y:y+height, x:x+width] = dst

# cv2.imshow('Result', img_rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import cv2
import numpy as np

# Load image
img = cv2.imread('phoi/photo1682182014.jpeg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find edges
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Find contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find largest contour
max_area = 0
best_cnt = None
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > max_area:
        max_area = area
        best_cnt = cnt

# Approximate contour as a rectangle
perimeter = cv2.arcLength(best_cnt, True)
approx = cv2.approxPolyDP(best_cnt, 0.02 * perimeter, True)
pts1 = np.float32([approx[0], approx[1], approx[3], approx[2]])

# Compute destination points
w = max(np.linalg.norm(pts1[0] - pts1[1]), np.linalg.norm(pts1[2] - pts1[3]))
h = max(np.linalg.norm(pts1[0] - pts1[3]), np.linalg.norm(pts1[1] - pts1[2]))
pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

# Compute perspective transform matrix and warp image
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (int(w), int(h)))

# Display result
cv2.imshow('Original Image', img)
cv2.imshow('Straightened Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
