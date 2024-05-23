'''
Autor: Flávio Lages Jr
Projeto: EDUCATEC/ARLEQUIM
Inicio: 05/05/2024
Fim: 12/05/2024

Licença: CC BY-NC 4.0 DEED
'''


# MODULO AUTMOAÇÃO PARA NAVEGADOR
from selenium import webdriver ## MÉTODO WEBDRIVER PARA INSTANCIAR O NAVEGADOR
from selenium.webdriver.common.keys import Keys ### CLASSE KEY FORNECE AS TECLAS DO TECLADO
from selenium.webdriver.common.by import By ### CLASSE BY PARA LOCALIZAR ELEMENTOS DA PAGINA

#### FUNÇÃO PARA SUSPENDER O PROGRAMA POR DETERMINADO TEMPO 
import time

# MODULO AUTOMAÇÃO PARA AS TECLAS (foi usado pois o POP-UP é uma janela fora dos elementos da pagina)
import pyautogui



LOGIN = open('AQUI_O_USUARIO_E_SENHA.txt', 'r')
dadosLogin = LOGIN.read().split()
time.sleep(4)

#NAVEGADOR = webdriver.Firefox()
#NAVEGADOR = webdriver.Edge()
NAVEGADOR = webdriver.Chrome()

def automacao():
    ################ ABRE O LINK DO ARLEQUIM
    time.sleep(3)
    NAVEGADOR.get("https://join.arlequim.com/logon/LogonPoint/tmindex.html")



    ################ PREENCHE OS CAMPOS NOME DE USUARIO E SENHA
    time.sleep(2)
    NAVEGADOR.find_element(By.XPATH, '//*[@id="login"]').send_keys(dadosLogin[0])
    time.sleep(2)
    NAVEGADOR.find_element(By.XPATH, '//*[@id="passwd"]').send_keys(dadosLogin[1] + Keys.ENTER)
    time.sleep(2)
    NAVEGADOR.find_element(By.XPATH, '//*[@id="protocolhandler-welcome-installButton"]').send_keys(Keys.ENTER)



    ################ SELECIONA O POP-UP
    time.sleep(5)
    pyautogui.hotkey('tab')
    time.sleep(5)
    pyautogui.hotkey('space')
    time.sleep(5)
    pyautogui.hotkey('tab', 'enter')
    


    ################ SELECIONA A MAQUINA VIRTUAL E CLICA EM ABRIR
    time.sleep(6)
    NAVEGADOR.find_element(By.XPATH, '/html/body/section[3]/div[2]/section[5]/div[5]/div/ul/li/a[3]/div').click()
    time.sleep(5)
    NAVEGADOR.find_element(By.XPATH, '/html/body/section[3]/div[2]/section[5]/div[5]/div/ul/li/div[3]/div[2]/table/tr/td[1]/div/a[1]/div/div[2]').click()
    time.sleep(5)

automacao()