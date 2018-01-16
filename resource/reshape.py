import cv2

img = cv2.imread('./bird.jpg')
img = cv2.resize(img, (32, 32))
cv2.imwrite('./bird_ss.jpg', img)
