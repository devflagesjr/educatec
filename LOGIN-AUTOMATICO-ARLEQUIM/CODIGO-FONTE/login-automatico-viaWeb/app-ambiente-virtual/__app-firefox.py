'''
Autor: Flávio Lages Jr
Data de criação: 04/05/2024
Data da publicação: 15/05/2024
Repositório: https://github.com/devflagesjr/arlequim
Licença: CC BY-NC 4.0 DEED Attribution-NonCommercial 4.0 International.
'''


###########################
#
#  IMPORTS
#
###########################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time





###########################
#
#  ARQUIVO DADOS DE LOGIN
#
###########################
arquivoUsuario = open('usuario.txt', 'r')
dadosLogin = arquivoUsuario.read().split()



#cxfreeze app.py --target-dir APP_EXE




###########################
#
#  APLICAÇÃO 
#
###########################
with webdriver.Firefox() as driver:
    # Abre no navegador a url
    driver.get("https://join.arlequim.com/logon/LogonPoint/tmindex.html")

    
    
    # Escreve nos campos de login os dados de usuario e senha
    wait = WebDriverWait(driver, 10)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(dadosLogin[0])
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys(dadosLogin[1] + Keys.RETURN)
    

    # Click o botão Detectar Aplicativo Citrix
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="protocolhandler-welcome-installButton"]').click()
    


    # Click na maquina virtual
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/section[3]/div[2]/section[5]/div[5]/div/ul/li/a[3]').click()
    # Click na abra abrir maquina virtual
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/section[3]/div[2]/section[5]/div[5]/div/ul/li/div[3]/div[2]/table/tr/td[1]/div/a[1]/div/div[2]').click()
    


    ####
    time.sleep(40)
    driver.quit()
    print("Fim")
    time.sleep(20)