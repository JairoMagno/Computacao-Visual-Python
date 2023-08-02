import socket, pickle, struct
import cv2 as cv

from wireless_adapter import get_wifi_ip

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = get_wifi_ip()  # IP do servidor
port = 8080
client_socket.connect((host_ip, port))  # Conectar com o servidor

video = cv.VideoCapture(0)
while True:
    ret, frame = video.read()
    frame = cv.resize(frame, (320, 240))
    frame = cv.cvtColor(cv.flip(frame, 1), cv.COLOR_BGR2RGB) #invertendo a imagem para perspectiva de selfie
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    data = pickle.dumps(frame)
    message = struct.pack('Q', len(data)) + data
    client_socket.sendall(message)
    
    cv.imshow('TRANSMITINDO VIDEO', frame)
    if cv.waitKey(1) == ord('q'):  # Press 'q' para parar a transmissão
        break

# libera os recurso e fecha o socket
video.release()
cv.destroyAllWindows()
client_socket.close()