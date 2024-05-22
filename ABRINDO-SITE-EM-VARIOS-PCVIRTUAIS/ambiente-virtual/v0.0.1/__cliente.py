'''


'''

### MÓDULO DE COMONICAÇÃO DE REDE BAIXO NÍVEL
import socket



## FUNÇÃO DE CONEXÃO COM SERVIDOR
def conectServer():
    try:
        #CRIA SERVIÇO EM IPv4(AF_INET) com protoloco TCP(SOCK_STREAK)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #CONECTA AO IP E PORTA DO SERVIDOR
        s.connect(('192.168.0.113', 443))
        return s
    except Exception as error:
        print('Erro ao conectar ao servidor!!!!')



conectServer()


## FUNÇÃO PARA CEHCAR E MANTER ABERTA A CONEXÃO
