from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

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

######################3 Lista para armazenar todos os dicionários de produtos
lista_produtos = []

list_produto = navegadorpa.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[2]")
for info in list_produto:
    info.click()
    slp()

#############################3
produto_info = {}

try:
    nome = navegadorpa.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div[2]/div/div[2]/div[2]/h1")
    nomes = nome.find_element(By.CLASS_NAME, "H1Styled-sc-18mg5yw-0") 
    produto_info['Nome'] = nomes.text

except Exception as e:
    produto_info['Nome'] = "Nome não encontrado"
    print(f"Erro ao encontrar nome do produto: {e}")

################################

try:
    valor = navegadorpa.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]")
    valores = valor.find_element(By.CLASS_NAME, "TextComponent-sc-w4b5ef-0")
    produto_info['Valor'] = valores.text
except Exception as e:
    produto_info['Valor'] = "Preço não encontrado"
    print(f"Erro ao encontrar valor do produto: {e}")

    lista_estoquepao = []

    lista_produtos.append(produto_info.copy)
    lista_estoquepao.append(lista_produtos[:])
    lista_produtos.clear()

    navegadorpa.back()
    slp()

for produto in lista_produtos:
    print(produto)

navegadorpa.quit()

wait = WebDriverWait(navegadorpa, 5)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/a")))

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

######################3 Lista para armazenar todos os dicionários de produtos
lista_produtos = []

list_produto = navegadorpa.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[2]")
for info in list_produto:
    info.click()
    slp()

#############################3
produto_info = {}

try:
    nome = navegadorpa.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div[2]/div/div[2]/div[2]/h1")
    nomes = nome.find_element(By.CLASS_NAME, "H1Styled-sc-18mg5yw-0") 
    produto_info['Nome'] = nomes.text

except Exception as e:
    produto_info['Nome'] = "Nome não encontrado"
    print(f"Erro ao encontrar nome do produto: {e}")

################################

try:
    valor = navegadorpa.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]")
    valores = valor.find_element(By.CLASS_NAME, "TextComponent-sc-w4b5ef-0")
    produto_info['Valor'] = valores.text
except Exception as e:
    produto_info['Valor'] = "Preço não encontrado"
    print(f"Erro ao encontrar valor do produto: {e}")

    lista_estoquepao = []

    lista_produtos.append(produto_info.copy)
    lista_estoquepao.append(lista_produtos[:])
    lista_produtos.clear()

    navegadorpa.back()
    slp()

for produto in lista_produtos:
    print(produto)

navegadorpa.quit()

wait = WebDriverWait(navegadorpa, 5)
wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[2]/div[2]/div[1]/div/div[3]/div[1]/a")))