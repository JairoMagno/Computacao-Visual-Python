"""
1. Necessário ter o openCV baixado
2. Necessário ter o MediaPipe baixado
"""
import cv2 as cv
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands

capture = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Teste_Mao.avi', fourcc, 20.0, (640, 480)) #Salvando o vídeo
hands = mphands.Hands()

while True:
    data, image = capture.read()
    #Inverter a imagem
    image = cv.cvtColor(cv.flip(image, 1), cv.COLOR_BGR2RGB)
    #Armazenando os resultados
    result = hands.process(image)
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    out.write(image)
    if result.multi_hand_landmarks:
        for hand_landamarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landamarks,
                mphands.HAND_CONNECTIONS)
    cv.imshow('Reconhecimento Gestos Mao', image)
    if cv.waitKey(1) == ord('s'): break                           #apertar a tecla 's' para sair

capture.release()
out.release()
    