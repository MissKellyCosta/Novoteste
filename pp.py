import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def slp():
    time.sleep(5)

def slp():
    time.sleep(5)

def slp():
    time.sleep(5)

# Inicializando o navegador
navegadorpa = webdriver.Chrome()
navegadorpa.get('https://www.paodeacucar.com/')
slp()
navegadorpa.maximize_window()

# Realizando a pesquisa por 'pão'
pesquisa = navegadorpa.find_element(By.ID, "input-search")
pesquisa.click()
pesquisa.send_keys('pão')
slp()

# Clicando no botão de busca
busca = navegadorpa.find_element(By.CLASS_NAME, "Icon-sc-1mux0mx-1")
busca.click()
slp()

# Lista para armazenar todos os dicionários de produtos
produtos = []
produto = []

# Pegando todos os links dos produtos na página de resultados
produtos = navegadorpa.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[2]")
produto = produtos.find_elements(By.PARTIAL_LINK_TEXT, "Pão ")

# Iterando sobre cada produto da lista
for info in produto:
    info.click()
    slp()
    
    # Criando o dicionário para armazenar informações do produto
    produto_info = {}
    lista_produtos = []
    try:
        # Pegando o nome do produto
        nome = navegadorpa.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div[2]/div/div[1]/div[2]")
        produto_info['Nome'] = nome.text
    except Exception as e:
        produto_info['Nome'] = "Nome não encontrado"
        print(f"Erro ao encontrar nome do produto: {e}")

    try:
        # Pegando o preço do produto
        valor = navegadorpa.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/main/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]")
        produto_info['Valor'] = valor.text
    except Exception as e:
        produto_info['Valor'] = "Preço não encontrado"
        print(f"Erro ao encontrar valor do produto: {e}")

    # Adicionando as informações do produto à lista
    lista_produtos.append(produto_info)

    # Voltando para a página de resultados
    navegadorpa.back()
    slp()

# Exibindo a lista com todos os produtos
for produto in lista_produtos:
    print(produto)

# Fechando o navegador
navegadorpa.quit()
