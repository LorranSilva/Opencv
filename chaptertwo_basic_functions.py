import cv2
import numpy as np

img = cv2.imread("resources/saiba-como-a-educacao-ajuda-voce-a-ser-uma-pessoa-melhor.jpeg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2. GaussianBlur(imgGray,(11,11),0)  #  A tupla so aceita numeros impares
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)


cv2.waitKey(0)