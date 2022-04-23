#Importación de las librerías necesarias para el scraper y la manipulación de los datos en excel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from bs4 import BeautifulSoup
import time
import pandas as pd 
import requests

#Inicializar la variable contenedora del controlador de Edge
driver = webdriver.Edge(r"C:\Users\Natyy\OneDrive\Escritorio\reto-talentpitch\msedgedriver.exe")
#abrir la página de emprendedores
paginaElEconomista = "https://www.eleconomista.es/pymes/"
driver.get(paginaElEconomista)

time.sleep(3)

#darle click al anuncio de cookies
try:
    anuncioCookies = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')
    anuncioCookies.click()
except NoSuchElementException as e:
    print('No se pudo dar click al boton', e)
except ElementNotVisibleException:
    print("Elemento no visible")

#Arreglos que serán llenados con los datos que recopilemos
titulos = []
descripciones = []
enlaces = []

paginaEE = BeautifulSoup(driver.page_source,"html.parser")
articulos=paginaEE.find_all('div', attrs={'class':'article rightSide'})
for articulo in articulos:
    title = articulo.find('h2', attrs={'class':'h3'})
    if title:
        titulos.append(title.text)
    else:
        print("no se pudo obtener el titulo")
    
    descripcion = articulo.find('p', attrs={'class':'articleText'})
    if descripcion:
        descripciones.append(descripcion.text)
    else:
        ("No se pudo obtener la descripción")
    
    link = articulo.find('a')['href']
    if link:
        enlaces.append(f"https:{link}")
    else:
        ('No se pudo obtener el enlace')
driver.quit()

paginaEmprendedores_es =  "https://www.emprendedores.es/seccion/guia-juridica-fiscal/"
r = requests.get(paginaEmprendedores_es)
entries = BeautifulSoup(r.text, "html.parser")
contenidos = entries.find_all('article', attrs={'class':'full-item'})
for contenido in contenidos:
    encabezado = contenido.find('h2', attrs={'class': 'full-item-title item-title entry-title'})
    if encabezado:
        titulos.append(encabezado.text)
    else:
        ("No se pudo obtener el encabezado")
    texto = contenido.find('div', attrs={'class': 'full-item-dek item-dek'})
    if texto:
        descripciones.append(texto.text)
    else:
        print("no se pudo obtener la descripcion")
    enlace = contenido.find('a')['href']
    if enlace:
        enlaces.append(enlace)

paginaEmprendedores_es2 = "https://www.emprendedores.es/seccion/guia-juridica-fiscal/page/2/"
r = requests.get(paginaEmprendedores_es)
entries = BeautifulSoup(r.text, "html.parser")
contenidos = entries.find_all('article', attrs={'class':'full-item'})
for contenido in contenidos:
    encabezado = contenido.find('h2', attrs={'class': 'full-item-title item-title entry-title'})
    if encabezado:
        titulos.append(encabezado.text)
    else:
        print("No se pudo obtener el encabezado")
    texto = contenido.find('div', attrs={'class': 'full-item-dek item-dek'})
    if texto:
        descripciones.append(texto.text)
    else:
        print("no se pudo obtener la descripcion")
    enlace = contenido.find('a')['href']
    if enlace:
        enlaces.append(enlace)

paginaEmprendedores_es3 = "https://www.emprendedores.es/seccion/guia-juridica-fiscal/page/3/"
r = requests.get(paginaEmprendedores_es3)
entries = BeautifulSoup(r.text, "html.parser")
contenidos = entries.find_all('article', attrs={'class':'full-item'})
for contenido in contenidos:
    encabezado = contenido.find('h2', attrs={'class': 'full-item-title item-title entry-title'})
    if encabezado:
        titulos.append(encabezado.text)
    else:
        ("No se pudo obtener el encabezado")
    texto = contenido.find('div', attrs={'class': 'full-item-dek item-dek'})
    if texto:
        descripciones.append(texto.text)
    else:
        print("no se pudo obtener la descripcion")
    enlace = contenido.find('a')['href']
    if enlace:
        enlaces.append(enlace)

def archivo():
    df = pd.DataFrame({
        "Comunidad" : "Emprendedores",
        "Tiutlo":titulos,
        "Enlace":enlaces,
        "Descripción" : descripciones
    })
    df.to_excel('emprendedores.xlsx', index=False)


archivo()