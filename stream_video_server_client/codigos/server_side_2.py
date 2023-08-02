import socket, pickle, struct, imutils
import cv2 as cv

from wireless_adapter import get_wifi_ip

# Criar socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = get_wifi_ip()
print('HOST IP:', host_ip)
port = 8080
socket_address = (host_ip, port)
#vinculando o socket
server_socket.bind(socket_address)
#escutando o socket para alguma conexão
server_socket.listen(5)
print("ESCUTANDO EM:", socket_address)
# Aceitar a conexão do cliente
client_socket, addr = server_socket.accept()
print('CONEXÃO RECEBIDA DE:', addr)

data = b""
payload_size = struct.calcsize("Q")
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('video.avi', fourcc, 20.0, (320, 240))
host_end = True

try:
    while True:
        # Recebe os frames do video do cliente
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K
            if not packet:
                raise ValueError("Cliente encerrou a Conexão.")
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            packet = client_socket.recv(4 * 1024)
            if not packet:
                raise ValueError("Cliente encerrou a Conexão.")
            data += packet

        frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)

        # Mostra o frame do video recebido localmente
        cv.imshow("RECEBENDO VIDEO (CLIENTE)", frame)
        out.write(frame)
        if cv.waitKey(1) == ord('q'):  # Aperte 'q' para sair
            break

except (ConnectionResetError, ValueError):
    host_end = False
    print('Video Chamada encerrada pelo CLIENTE')

cv.destroyAllWindows()
client_socket.close()
server_socket.close()
out.release()
if host_end: print('Vídeochamada encerrada pelo HOST.') #encerrando a chamada pelo lado do host
