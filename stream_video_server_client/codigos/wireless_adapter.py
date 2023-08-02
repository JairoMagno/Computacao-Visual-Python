import socket

def get_wifi_ip():

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    
    except socket.error as e:
        print("Erro ao obter o IP do adaptador de rede sem fio (Wi-Fi):", e)
        return None
