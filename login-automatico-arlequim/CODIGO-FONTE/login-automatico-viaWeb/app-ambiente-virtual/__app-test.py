

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import time

dadosLogin = ["flavio.junior", "18041991"]

driver = Firefox()
driver.get('https://join.arlequim.com/logon/LogonPoint/tmindex.html')
wait = WebDriverWait(driver, 10)
def _waitForAlert(driver):
    return WebDriverWait(driver, 5).until(EC.alert_is_present())

time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(dadosLogin[0])
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys(dadosLogin[1] + Keys.RETURN)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="protocolhandler-welcome-installButton"]').click()
time.sleep(5)
# Espera o pop-up carregar.
alert = _waitForAlert(driver)
# Pega o texto do pop-up.
value = alert.text
print(value)
# Dar o Ok no pop-up.
alert.accept()
# Compara o texto com o esperado.
assert "Press a button!" == value