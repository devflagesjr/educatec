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








#################################################################
##### INTRODUÇÃO
print("INICIANDO AUTOMATIZAÇÃO PC VIRTUAL, aguarde...")
time.sleep(15)
##### CLICK ICONE LADO DO RELOGIO
pyautogui.click(int(posicao[0]), int(posicao[1]))
time.sleep(1)
##### CLICK TELA PROGRAMA
pyautogui.click(1250, 770)
print("Abriu o progrma")
time.sleep(35)
###################################################################







#################################################################
##### CLICK FERRAMENTAS
pyautogui.click(1290, 96)
time.sleep(2)
##### CLICK ATUALIZAR APLICATIVO
pyautogui.click(1383, 131)
print("Atualizando aplicativo")
##### CLICK MAQUINA VIRTUAL
time.sleep(2)
pyautogui.click(374, 289)
print("Abrindo PC VIRTUAL")
time.sleep(int(tempo))
#################################################################









#################################################################
##### CLICK FERRAMENTAS
pyautogui.click(1290, 96)
time.sleep(2)
##### CLICK ATUALIZAR APLICATIVO
pyautogui.click(396, 125)
print("Atualizando aplicativo")
##### CLICK MAQUINA VIRTUAL
time.sleep(2)
pyautogui.click(374, 289)
print("Abrindo PC VIRTUAL")
time.sleep(int(tempo))
#################################################################






#################################################################
##### ESCREVENDO DADOS DE USUARIO
time.sleep(1)
pyautogui.click(779, 521)
pyautogui.write(dadosLogin[0])

##### ESCREVENDO DADOS DE SENHA
time.sleep(1)
pyautogui.click(739, 606)
pyautogui.write(dadosLogin[1])

##### CLICK LOGIN
time.sleep(1)
pyautogui.click(893, 688)
time.sleep(int(tempo))
##################################################################






#### MENSAGEM QUE FINALIZOU
print("FINALIZPU AUTOMAÇÃO")
time.sleep(20)