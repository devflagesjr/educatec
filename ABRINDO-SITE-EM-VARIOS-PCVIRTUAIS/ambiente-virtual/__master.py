"""
Author: Flávio Lages Jr.
Project: Projeto master conecta no servidor e envia comandos para abertura de aplicativos ex(abrir uma pagina web)!
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
    master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## CONECTA AO SERVIDOR IP e PORTA, CASO CONTRARIO MOSTRA MENSAGEM DE ERRO
    try:
        master.connect(('192.168.0.113', 443))
    except:
        return print('\nErro ao conectar!!!\n')
    
    print("\nConectato!!!")

    #CRIA UMA THREAD PARA A FUNÇÃO enviaComando
    threadEnviaComando = threading.Thread(target=enviaComando, args=[master, CHAVE])
    threadEnviaComando.start()



### Função envia comando
def enviaComando(master, chave):
    while True:
        try:
            # Recebe entrada via cmd
            comando = input('\n')
            master.send(f'{chave} {comando}'.encode("utf-8"))
        except:
            # Caso nao sesteja conectado, sai dessa função
            print('\nNão foi possivel conectat!!!')
            return



main()
