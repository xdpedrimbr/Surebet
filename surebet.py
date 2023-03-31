import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.esportenetvip.com.br/')

content = driver.page_source
soup = bs4.BeautifulSoup(content, "html.parser")

time.sleep(4)

div = driver.find_element(By.ID, "grdJogos")
linhas = div.find_elements(By.XPATH, ".//tr")

print(linhas)

for linha in linhas:
    colunas = linha.find_elements(By.XPATH, ".//td")
    for coluna in colunas:
        informacao = coluna.text
        print(informacao)


driver.quit()