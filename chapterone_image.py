import cv2
print("Package Imported")

img = cv2.imread("resources/saiba-como-a-educacao-ajuda-voce-a-ser-uma-pessoa-melhor.jpeg")

cv2.imshow("Output", img)  #  importando  imagem (nome da janela, arquivo)

cv2.waitKey(0)  # mostrar a imagem (mili segundos), se passar 0 é infinito