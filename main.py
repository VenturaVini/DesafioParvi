from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
import numpy as np

options = webdriver.ChromeOptions()
options.add_argument("--headless")

navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

link = 'https://gizmodo.uol.com.br/'

navegador.get(link)

dicionario = {}
lista = []
lista1 = []
lista2 = []
for i in np.arange(1,11):
    titulo = navegador.find_element(By.XPATH,f'//*[@id="mdContent"]/div[{i}]/article/header/h3/a').text;
    lista.append(titulo)
    data = navegador.find_element(By.XPATH,f'//*[@id="mdContent"]/div[{i}]/article/div[3]/div[1]/div/div/span/abbr').get_attribute('title')
    lista1.append(data)
    resumo = navegador.find_element(By.XPATH,f'//*[@id="mdContent"]/div[{i}]/article/div[3]/div[2]/div/p').text;
    lista2.append(resumo)

dicionario['Titulo'] = lista
dicionario['Data'] = lista1
dicionario['Resumo'] = lista2

base = pd.DataFrame(dicionario)

print(base)
print(base)

base.to_excel('Teste.xlsx',index=False)
base.to_csv('Teste.csv',index=False)

time.sleep(10)
