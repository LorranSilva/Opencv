import cv2

path = 'resources/saiba-como-a-educacao-ajuda-voce-a-ser-uma-pessoa-melhor.jpeg'
img = cv2.imread(path)

imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("Original",img)
cv2.imshow("Image",imgHSV)

cv2.waitKey(0)