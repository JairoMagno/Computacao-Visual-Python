import socket, pickle, struct
import cv2 as cv

# Criar Socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '172.19.224.1' #Bote seu IP ADDRESS aqui!
port = 8080
client_socket.connect((host_ip, port)) # Uma tupla
data = b""
payload_size = struct.calcsize("Q")

while True:

	while len(data) < payload_size:
		packet = client_socket.recv(4*1024) # 4K
		if not packet: break
		data += packet
		
	packed_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack("Q",packed_msg_size)[0]
	
	while len(data) < msg_size:
		data += client_socket.recv(4*1024)
		
	frame_data = data[:msg_size]
	data  = data[msg_size:]
	frame = pickle.loads(frame_data)
	cv.imshow("RECEBENDO VIDEO",frame)
	if cv.waitKey(1) == ord('q'): #clique no botão 'q' para sair
		break
	
client_socket.close()
cv.destroyAllWindows()