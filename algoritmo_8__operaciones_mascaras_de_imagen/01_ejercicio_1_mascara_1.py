import cv2

img = cv2.imread('ejercicio1.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask_i = cv2.inRange(hsv,(150,0,0),(150,255,255))

mask = cv2.bitwise_not(mask_i)
img_2 = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Imagen original',img)
cv2.imshow('Imagen 1.1. cv2.inRange(hsv,(150,0,0),(150,255,255))', img_2)
cv2.waitKey(0)