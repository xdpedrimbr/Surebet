import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.esportenetvip.com.br/')

html = driver.page_source
soup = bs4.BeautifulSoup(html, "html.parser")
items = soup.find("div", {"id": "grdJogos"})


if items:
    print(items.text)
else:
    print('Div não encontrada')

time.sleep(4)

div = driver.find_element(By.ID, "grdJogos")
linhas = div.find_elements(By.XPATH, ".//tr")

# for linha in linhas:
#     colunas = linha.find_elements(By.XPATH, ".//td")
#     for coluna in colunas:
#         informacao = coluna.text
#         print(informacao)


driver.quit()