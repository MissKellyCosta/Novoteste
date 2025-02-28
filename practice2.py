from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def slp():
    time.sleep(5)

navegadorpa = webdriver.Chrome()
navegadorpa.get('https://www.paodeacucar.com/')
slp()
navegadorpa.maximize_window()

pesquisa = navegadorpa.find_element(By.ID, "input-search")
pesquisa.click()
pesquisa.send_keys('pão')
slp()

busca = navegadorpa.find_element(By.CLASS_NAME, "Icon-sc-1mux0mx-1")
busca.click()
slp()


list_produto = navegadorpa.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[2]/div[2]/div[1]/div/div[1]/a")
for info in list_produto:
    info.click()
    slp()
estoquepao = dict()
nome = navegadorpa.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div[2]/div/div[1]/div[2]")
all_nomes = nome.find_elements(By.CLASS_NAME, "H1Styled-sc-18mg5yw-0")
for n in all_nomes: 
    print(n.text)
valor = navegadorpa.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]")
all_valores = valor.find_elements(By.CLASS_NAME, "TextComponent-sc-w4b5ef-0")
for v in all_valores:
    print(v.text)        
    estoquepao['Nome: '] = n.text
    estoquepao['Valor: '] = v.text
    print(estoquepao)
navegadorpa.back()
'''try:
        wait = WebDriverWait(navegadorpa, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/a")))
except:'''