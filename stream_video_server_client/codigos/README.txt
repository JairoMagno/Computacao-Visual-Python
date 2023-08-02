Existem 4 códigos principais, o conjunto (server_side.py, client_side.py) e o (server_side_2.py, client_side_2.py).

1) O primeiro conjunto é onde o servidor será responsável por gravar o vídeo da sua câmera e ENVIAR em tempo real para o cliente. 
No final da chamada o vídeo terá sido gravado e armazenado no diretório atual onde o script do servidor está localizado.

2) O segundo conjunto é onde o servidor será responsável por RECEBER o vídeo da câmera do cliente em tempo real. Assim com o primeiro
conjunto, o vídeo também será gravado e armazenado no diretório atual onde o script do servidor está localizado.

3) O quinto códido é o wireless_adapter. Ele é um módulo que é utilizado nos outros 4 scripts afim de obter o endereço IP da rede wi-fi.
Foi criado a parte com o intuito de deixar os códigos principais mais enxutos e modularizados.