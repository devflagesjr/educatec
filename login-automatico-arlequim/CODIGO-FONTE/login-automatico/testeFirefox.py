from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time

#cxfreeze debut_console.py --target-dir exeDir




with webdriver.Firefox() as driver:
    driver.get("https://join.arlequim.com/logon/LogonPoint/tmindex.html")
    # https://join.arlequim.com/Citrix/FloripaWeb/
    
    
    ####
    wait = WebDriverWait(driver, 10)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="login"]').send_keys("paulofontes20")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys("salainformatizada" + Keys.RETURN)
    
    
    #### 
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="protocolhandler-welcome-installButton"]').click()
    
    #### CLICA NA MAQUINA VIRTUAL
    time.sleep(10)
    driver.find_element(By.XPATH, '/html/body/section[3]/div[2]/section[5]/div[5]/div/ul/li/a[3]').click()
    #### CLICA EM ABRIR A MAQUINA VIRTUAL
    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/section[3]/div[2]/section[5]/div[5]/div/ul/li/div[3]/div[2]/table/tr/td[1]/div/a[1]/div/div[2]').click()
    

    ####
    time.sleep(40)
    driver.quit()
    print("Fim")
    time.sleep(20)