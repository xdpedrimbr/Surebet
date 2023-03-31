import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

driver = webdriver.Chrome()
driver.get('https://www.esportenetvip.com.br/')

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
# divExterna1 = soup.find("div", {"class": "body2"})
# divExterna2 = divExterna1.find("div", {"id": "content"})
# divExterna3 = divExterna2.find("div", {"class": "LeftColumn"})
# items = divExterna3.find("div", {"class": "grdJogos"})

# print(soup.prettify())

# if items:
#     print(items.text)
# else:
#     print('Div não encontrada')

time.sleep(4)

div = driver.find_element(By.ID, "grdJogos")
qtdLinhas = len(div.find_elements(By.XPATH, "/html/body/div[1]/div[1]/table/tbody/tr/td[2]/div[2]/div/table/tbody/tr"))


listElements = []
for i in range(qtdLinhas):
    linhas = div.find_elements(By.XPATH,f'//*[@id="grdJogos"]/table/tbody/tr[{i}]')
    for idx, coluna in enumerate(linhas):
        # nao efetua a leitura do header
        if coluna.get_attribute("id") == "header":
            continue
        # nao efetua a leitura do subheader
        if coluna.get_attribute("class") == "subtitulotabela":
            continue
        
        informacao = coluna.text
        confronto = informacao.split("\n")[0]
        valores = informacao.split("\n")[1].split(" ")
        odd = 0

        if valores[5].find("+") != -1:
            odd = int(valores[5].replace("+", ""))
        else:
            odd = int(valores[5])

        tempDict = {"Confronto": confronto, 
                    "Data": datetime.strptime(valores[0].replace(",", ""), "%d/%m/%y"), 
                    "Horario": valores[1], 
                    "Casa": float(valores[2].replace(",", ".")), 
                    "Empate": float(valores[3].replace(",", ".")), 
                    "Fora": float(valores[4].replace(",", ".")), 
                    "ODD": odd}
        
        listElements.append(tempDict)
    
for value in listElements:
    print(value)
    
list = []

driver.quit()