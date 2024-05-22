'''
Autor: Flávio Lages Jr
Projeto: EDUCATEC
Inicio: 29/04/2024
Fim: 4/05/2024

Licença: CC BY-NC 4.0 DEED
'''


import time
import pyautogui







################################################################
#
#           ARQUIVOS DE CONFIGURAÇÃO
#
################################################################

#################################################################
##### DADOS DE LOGIN
arquivoUsuario = open('usuario.txt', 'r')
dadosLogin = arquivoUsuario.read().split()


################################################################
##### CONFIGURAÇÂO TEMPO DE TELA
arquivoTemporizador = open('temporizador.txt', 'r')
tempo = arquivoTemporizador.read()


################################################################
##### POSIÇÃO MOUSE ICONE RELOGIO
arquivoPosicao = open('arquivoPosicao.txt', 'r')
posicao = arquivoPosicao.read().split()






################################################################
#
#           INICIALIZAÇÃO
#
################################################################

#################################################################
##### INTRODUÇÃO
print("INICIANDO AUTOMATIZAÇÃO PC VIRTUAL...  ", tempo, "Segundos")
time.sleep(int(tempo))
##### CLICK ICONE LADO DO RELOGIO
pyautogui.click(int(posicao[0]), int(posicao[1]))
time.sleep(2)
##### CLICK TELA PROGRAMA
pyautogui.click(1250, 770)
print("______________________")
print("ABRINDO PROGRAMA")
time.sleep(int(tempo))
###################################################################










################################################################
#
#           ATUALIZANDO O APP
#
################################################################

#################################################################
##### CLICK FERRAMENTAS
print("______________________")
print("Atualizando aplicativo")
pyautogui.click(1290, 96)
time.sleep(2)
##### CLICK ATUALIZAR APLICATIVO
pyautogui.click(1364, 126)
time.sleep(int(tempo))
#################################################################










################################################################
#
#           ABRINDO MAQUINA VIRTUAL
#
################################################################
print("Abrindo PC VIRTUAL")
pyautogui.click(375, 280)
time.sleep(2)







###################################################################
#
#       DADOS DE LOGIN
#
####################################################################
print("************* ESCREVENDO DADOS DE LOGIN")
##### ESCREVENDO DADOS DE USUARIO
pyautogui.click(779, 521)
time.sleep(2)
print("Usuario")
pyautogui.write(dadosLogin[0])

##### ESCREVENDO DADOS DE SENHA
time.sleep(2)
print("Senha")
pyautogui.click(739, 606)
pyautogui.write(dadosLogin[1])

##### CLICK LOGIN
time.sleep(2)
print("Acessando PC Virtual")
pyautogui.click(893, 688)
time.sleep(int(tempo))
#########################









#### MENSAGEM QUE FINALIZOU
print("FINALIZPU AUTOMAÇÃO")
time.sleep(20)