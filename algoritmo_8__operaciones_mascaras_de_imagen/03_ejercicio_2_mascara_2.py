import cv2

img = cv2.imread('camara_2.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask_i = cv2.inRange(hsv,(64,250,166),(68,254,170))

mask = cv2.bitwise_not(mask_i)
img_2 = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Imagen original',img)
cv2.imshow('Imagen 2.2. cv2.inRange(hsv,(64,250,166),(68,254,170))', img_2)
cv2.waitKey(0)