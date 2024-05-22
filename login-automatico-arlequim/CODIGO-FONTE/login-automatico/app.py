'''
IMPORTAÇÕES
'''
from seleniumbase import BaseCase


'''
LEITURA DO ARQUIVO USUARIO
'''
arquivoUsuario = open('usuario.txt', 'r')
dadosUsuario = arquivoUsuario.read().split()



'''
VARIAVEIS
'''
URL = "https://join.arlequim.com/logon/LogonPoint/tmindex.html"
LOGIN = dadosUsuario[0]
PASSWORD = dadosUsuario[1]




'''
INICIO DO PROGRAMA
'''



class Inicio(BaseCase):
    def pagina_login(self):
        # ABRE A PAGINA
        self.open(URL)



print('fim do programa')