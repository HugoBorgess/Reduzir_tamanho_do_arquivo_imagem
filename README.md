# Redimensionamento de Imagem usando OpenCV

Este script em Python utiliza o OpenCV para redimensionar uma imagem para um tamanho menor.

## Pré-requisitos

- Python 3.x
- OpenCV (cv2)

Certifique-se de ter o OpenCV instalado antes de executar este script.

## Utilização

1. Certifique-se de ter a imagem "grizzly.jpg" no mesmo diretório que o script. 
2. Execute o script em um ambiente Python.
3. O script lerá a imagem "grizzly.jpg" e exibirá sua forma (dimensões) original.
4. Defina um valor para a constante de redução 'k'. Quanto maior o valor de 'k', maior será a redução da imagem.
5. O script redimensionará a imagem usando a função resize() do OpenCV, de acordo com o valor de 'k', e exibirá a forma da imagem redimensionada.
6. Uma janela pop-up será exibida mostrando a imagem redimensionada usando a função imshow().
7. A imagem redimensionada será salva em um arquivo chamado "resized_output_image.jpg" no diretório.

Certifique-se de ajustar o valor de 'k' de acordo com suas necessidades para obter o tamanho desejado na imagem redimensionada.

## Observação

Certifique-se de ter o arquivo "grizzly.jpg" no mesmo diretório do script antes de executá-lo. Você também pode modificar o código para ler outras imagens fornecendo o caminho correto para a imagem desejada.

Certifique-se de ter instalado corretamente o OpenCV para que o script possa importar o módulo cv2.

Ao usar imagens de terceiros, respeite os direitos autorais e os termos de uso aplicáveis.
