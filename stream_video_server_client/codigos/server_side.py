import socket, pickle, struct, imutils
import ffmpeg_streaming as fs 
import cv2 as cv

from wireless_adapter import get_wifi_ip

#Criando socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
#host_ip = get_wifi_ip()
print('HOST IP:', host_ip)
port = 8080
socket_address = (host_ip, port)
#vinculando o socket
server_socket.bind(socket_address)
#escutando o socket
server_socket.listen(5)
print("ESCUTANDO EM:", socket_address)
#aceitando o socket
host_end = True
while True:
    client_socket, addr = server_socket.accept()
    print('CONEXÃO RECEBIDA DE:', addr)
    if client_socket:
        video = cv.VideoCapture(0)  #video começa a ser capturado quando o socket for aceito
        print('Pressione "q" para sair!')
        fourcc = cv.VideoWriter_fourcc(*'XVID') 
        out = cv.VideoWriter('Teste.avi', fourcc, 20.0, (320, 240))

        while(video.isOpened()):
            img, frame = video.read()
            frame = imutils.resize(frame, width=320, height=240)
            frame = cv.cvtColor(cv.flip(frame, 1), cv.COLOR_BGR2RGB) #invertendo a imagem para perspectiva de selfie
            frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
            a = pickle.dumps(frame)
            message = struct.pack('Q', len(a)) + a
            try:
                client_socket.sendall(message)
            except ConnectionAbortedError:                           #Encerrando a chamada pelo lado do cliente
                host_end = False
                print('Videochamada encerrada pelo cliente.')
                break
            
            cv.imshow('TRASMITINDO VIDEO', frame)
            out.write(frame)

            if cv.waitKey(1) == ord('q'): #Clique no botã q para sair
                break

        video.release()
        out.release()
        client_socket.close()
        cv.destroyAllWindows()
        if host_end: print('Vídeochamada encerrada pelo host.') #encerrando a chamada pelo lado do host
        break