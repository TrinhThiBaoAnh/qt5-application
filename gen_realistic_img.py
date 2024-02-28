import cv2
import numpy as np

# Đọc ảnh đầu vào và chuyển đổi sang ảnh xám
img = cv2.imread('input/input1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng bộ lọc trung bình để làm mờ và giảm nhiễu
blur = cv2.blur(gray, (5, 5))

# Tạo ma trận biến đổi projective để bẻ cong ảnh
rows, cols = gray.shape
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
pts2 = np.float32([[0, 0], [cols - 1, 0], [cols * 0.1, rows - 1], [cols * 0.9, rows - 1]])
M = cv2.getPerspectiveTransform(pts1, pts2)

# Áp dụng ma trận biến đổi vào ảnh
result1 = cv2.warpPerspective(img, M, (cols, rows))

# Đọc ảnh đầu vào và chuyển đổi sang ảnh xám
img = cv2.imread('input/input2.jpg')
img = cv2.rotate(img,cv2.ROTATE_180)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng bộ lọc trung bình để làm mờ và giảm nhiễu
blur = cv2.blur(gray, (5, 5))

# Tạo ma trận biến đổi projective để bẻ cong ảnh
rows, cols = gray.shape
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
pts2 = np.float32([[0, 0], [cols - 1, 0], [cols * 0.1, rows - 1], [cols * 0.9, rows - 1]])
M = cv2.getPerspectiveTransform(pts1, pts2)

# Áp dụng ma trận biến đổi vào ảnh
result2 = cv2.warpPerspective(img, M, (cols, rows))
result2 = cv2.rotate(result2,cv2.ROTATE_180)
# Concatenate the two images vertically
concatenated_img = cv2.vconcat([result1, result2])
# concatenated_img = cv2.resize(concatenated_img,(800,800))
# Display the concatenated image
# cv2.imshow('Concatenated Image', concatenated_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('Image2.jpg', concatenated_img)

# img = cv2.imread('Image2.jpg')

img = concatenated_img
background = cv2.imread('input/bg.jpg')
background = cv2.resize(background,(img.shape[1],img.shape[0]))
# Convert the image with object to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a mask
_, mask = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

# Find contours in the mask
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the largest area
largest_contour = max(contours, key=cv2.contourArea)

# Create a mask for the contour
mask = np.zeros(img.shape[:2], np.uint8)
cv2.drawContours(mask, [largest_contour], -1, 255, -1)

# Crop the object from the original image
object_crop = cv2.bitwise_and(img, img, mask=mask)

# Create a mask for the background
background_mask = cv2.bitwise_not(mask)

# Crop the background from the background image
background_crop = cv2.bitwise_and(background, background, mask=background_mask)

# Combine the object crop and the background crop
result = cv2.add(object_crop, background_crop)

# # Show the result
# cv2.imshow('Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# Add noise
noise = np.zeros(result.shape, np.uint8)
cv2.randn(noise, 0, 20)
noisy_img = cv2.add(result, noise)

# Reduce color saturation
hsv = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2HSV)
hsv[..., 1] = hsv[..., 1] * 0.5
aged_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imwrite('output/Result.jpg', aged_img)