# importar openCV para lidar com imagens
import cv2

# ler a imagem
img = cv2.imread('grizzly.jpg')
print(img.shape)

# selecionar o valor para a constande de redução 'k'
k = 5
width = int((img.shape[1])/k)
height = int((img.shape[0])/k)

# resize() função do openCV para alterar o tamanho da imagem
scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
print(scaled.shape)

# mostrar a imagem com imshow()
cv2.imshow("Output", scaled)
cv2.waitKey(500)
cv2.destroyAllWindows()

# criando o arquivo com o tamanho reduzido.
cv2.imwrite('resized_output_image.jpg', scaled)