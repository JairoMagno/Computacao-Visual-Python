import math
import cv2 as cv
import numpy as np
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision

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

# Altura e largura que será usada pelo modelo
DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480

image_filenames = ['teste_1.jpg', 'teste_2.jpg']

# Create the options that will be used for ImageSegmenter
base_options = python.BaseOptions(model_asset_path="C:/Users/JairoMagnoCaracciolo/OneDrive - Direction Systems Ltda/Área de Trabalho/Oficina/Projeto_Covid/Computacao_Visual/Aprendizado_MediaPipe/image_segmentation/deeplabv3.tflite")
options = vision.ImageSegmenterOptions(base_options=base_options, output_category_mask=True)

# Blur the image background based on the segmentation mask.

# Create the segmenter
with python.vision.ImageSegmenter.create_from_options(options) as segmenter:

  # Loop through available image(s)
  for image_file_name in image_filenames:

    # Create the MediaPipe Image
    image = mp.Image.create_from_file(image_file_name)

    # Retrieve the category masks for the image
    segmentation_result = segmenter.segment(image)
    category_mask = segmentation_result.category_mask

    # Convert the BGR image to RGB
    image_data = cv.cvtColor(image.numpy_view(), cv.COLOR_BGR2RGB)

    # Apply effects
    blurred_image = cv.GaussianBlur(image_data, (55,55), 0)
    condition = np.stack((category_mask.numpy_view(),) * 3, axis=-1) > 0.1
    output_image = np.where(condition, image_data, blurred_image)

    print(f'Blurred background of {image_file_name}:')
    resize_and_show(output_image)