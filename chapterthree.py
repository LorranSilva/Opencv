import cv2
import numpy as np

img = cv2.imread("resources/applecar-418x235.jpg")
print(img.shape)  #  encontrar o tamanho da imagem (height, width, channels BGR)

imgResize = cv2.resize(img,(350,200))
print(imgResize.shape)  #  encontrar o tamanho da imagem (height, width, channels BGR)

imgCropped = img[0:200,200:500]

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)