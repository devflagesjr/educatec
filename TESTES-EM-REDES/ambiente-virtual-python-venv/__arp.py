#arp.py

"""

ARP é o protocolo que pergunta na rede quem tem o endereço IP que deseja identificar!


"""
from scapy.layers.l2 import Ether, ARP
from scapy.sendrecv import srp1 # MANDA 1 PACOTE E ESPERA 1 PACOTE


## ESSE MEU MAC
MAC = "38:D5:7A:CD:07:51"


## ENVIA PACOTE PARA O MAC BROADCAST
BROADCAST = "ff:ff:ff:ff:ff:ff"



## CRIA O PACOTE COM O ENDEREÇO IP DE DESTINO
pacote = ARP(pdst='192.168.0.1')

## ETHER TRANSFORMA O PACOTE EM FRAME(BINARIO PARA TRAFEGAR NO MEIO FISICO) É O ULTIMO ESTAGIO DA CAMADA DE REDE
frame = Ether(src=MAC, dst=BROADCAST)


## CRIAMOS UM PACOTE FINAL ONDE O FRAME CARREGA O PACOTE QUE CONTEM O ENDEREÇO IP DE DESTINO
pacoteFinal = frame / pacote


resposta = srp1(pacoteFinal)
resposta.show()
