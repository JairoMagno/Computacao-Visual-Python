import math
import cv2 as cv
import mediapipe as mp

# Perfoma o redimensionamento e mostra a imagem
def resize_and_show(image):
  h, w = image.shape[:2]
  if h < w:
    img = cv.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
  else:
    img = cv.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
  cv.imshow('Image', img)
  cv.waitKey(0)
  cv.destroyAllWindows()

image_filenames = ['teste_1.jpg', 'teste_2.jpg']

# Altura e largura que será usada pelo modelo
DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480

# Preview da imagem(s)
images = {name: cv.imread(name) for name in image_filenames}
for name, image in images.items():
  print(name)            #print do nome da imagem atual no terminal
  resize_and_show(image) #Chamada da função com a imagem como parâmetro
