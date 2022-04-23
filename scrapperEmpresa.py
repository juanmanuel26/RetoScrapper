from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
driver = webdriver.Edge(r"C:\Users\Natyy\OneDrive\Escritorio\reto-talentpitch\msedgedriver.exe")
url = "https://blogs.iadb.org/ideas-que-cuentan/es/"
driver.get(url)

pgBlogs=BeautifulSoup(driver.page_source,"html.parser")
#contenidos = pgBlogs.find_all('article', attrs={'class' : 'content'})
titulo = [driver.find_element(By.XPATH, '//*[@id="genesis-content"]/article[1]/header/h2/a')]
titulos = []
descripciones = []
enlaces = []
if titulo:
    print(titulo.text)


# url = "http://www.businessanddisability.org/videos/"
# peticion = requests.get(url)
# objeto = BeautifulSoup(peticion.text, "html.parser")
# contenidos = objeto.find_all('article', attrs={'class' : 'wef-1vx1dtt'})
# for valor in contenidos:
#     titulo = valor.find('a', attrs={'class': 'chakra-link wef-1c7l3mo'})
#     if titulo:
#         print("titulos: ", titulo.text)
#         #titulos.append(titulo.text)
#     else:
#         print("there is no title")
#     # parrafo = valor.find('p')
#     # if parrafo:
#     #     descripciones.append(parrafo.text)
#     # else:
#     #     print("No hay parrafo")
#     # enlace = valor.find('a')["href"]