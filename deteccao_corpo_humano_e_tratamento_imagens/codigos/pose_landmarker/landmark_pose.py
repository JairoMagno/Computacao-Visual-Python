import cv2 as cv
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

capture = cv.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
    while capture.isOpened():
        sucess, image = capture.read()
        image.flags.writeable = False
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        results = pose.process(image)
        #Escreve a anotação da pose na imagem
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec = mp_drawing_styles.get_default_pose_landmarks_style()
        )
        #Inverte a imagem horizontalmente para uma visualização estilo sefie
        cv.imshow('LandMark Pose', cv.flip(image, 1))
        if cv.waitKey(1) == ord('s'):  #apertar o botão s para sair
            break
        
capture.release()