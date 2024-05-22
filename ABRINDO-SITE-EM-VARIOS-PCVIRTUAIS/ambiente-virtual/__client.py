"""
Author: Flávio Lages Jr.
Project: Projeto cliente conecta no servidor e recebe comandos para abertura de aplicativos ex(abrir uma pagina web)!
Licence: CC BY-NC 4.0
"""


###
import threading
import socket


### VARIAVEIS
#chave identifica de qual para quais o comando vai ser execultado
CHAVE = '90us89d9usdhsd'



### Função principal
def main():
    
    ## CRIA SERVIÇO DE CONEXÃO IPV4(AF.INE) no protocolo TCP(SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## CONECTA AO SERVIDOR IP e PORTA, CASO CONTRARIO MOSTRA MENSAGEM DE ERRO
    try:
        client.connect(('192.168.0.113', 443))
    except:
        return print('\nErro ao conectar!!!\n')
    
    print("\nConectato!!!")



### Função recebe comando
def recebeComando(client):
    while True:
        #RECEBE COMANDO DO SERVIDO
        try:
            comando = client.recv(2048).decode('utf-8')
            print(comando+'\n')
        except:
            #CASO NÃO ESTEJA CONECTADO, SAI DA FUNÇÃO
            print('\nNão foi possivel conectar!!!')
            return

main()
recebeComando()