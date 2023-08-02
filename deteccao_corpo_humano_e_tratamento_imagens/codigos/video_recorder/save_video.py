import cv2 as cv

cap = cv.VideoCapture(0)
# Define o codec e cria um VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Teste.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame_rgb = cap.read()
    if not ret:
        print("Não foi possível receber do frame_rgb (fim da stream ?). Saindo ...")
        break
    #Inverte a Imagem para uma visualização de selfie
    frame_rgb = cv.cvtColor(cv.flip(frame_rgb, 1), cv.COLOR_BGR2RGB)
    frame_rgb = cv.cvtColor(frame_rgb, cv.COLOR_RGB2BGR) #Garantia da conversão para RGB
    # Escreve no frame_rgb
    out.write(frame_rgb)
    cv.imshow('Rec...', frame_rgb)
    if cv.waitKey(1) == ord('s'): break  #Clica no botão 's' para parar a gravação
# Libera tudo se o vídeo for terminado

cap.release()
out.release()
cv.destroyAllWindows()