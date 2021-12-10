import cv2
import numpy as np

img = cv2.imread("resources/math-card-games-make-11.jpg")

width, height = 622, 650
pts1 = np.float32([[240,378],[410,375],[235,587],[415,580]])  #  1 ponto, 2 ponto, 3 ponto, 4 ponto, selecionar 4 pontos desejados (olhar coordenadas paint)
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matriz = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img,matriz,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Image Selected",imgOutput)

cv2.waitKey(0)