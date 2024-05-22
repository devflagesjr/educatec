'''

Author: Flávio Lages Jr
Licence: 

'''
#### MÓDULO DE COMUNICAÇÃO DE REDE BAIXO NÍVEL
import socket


### CRIA SERVIÇO EM IPv4(AF_INET) com protoloco TCP(SOCK_STREAK)
servico = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


### ENDEREÇO IP LOCAL E PORTA
servico.bind(('', 2024)) 


### QUANTIDADE DE CONEXÃO PERMITIDA
servico.listen(500)



### LOOP INFINIDO MONITORANDO CONEXÕES
while True:

    #ACCEPT aceita uma conexão, CONN objeto para enviar e receber dados, ADDRESS endereço da outra extremidade da conexão
    conn, address = servico.accept()
    