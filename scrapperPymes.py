from bs4 import BeautifulSoup
import pandas as pd 
import requests
#from scrapperEmprendedores import *
titulos = []
descripciones = []
enlaces = []

def pymes(url, url2):
    r = requests.get(url)
    entries = BeautifulSoup(r.text, "html.parser")
    contenidos = entries.find_all('div', attrs={'class':'mod_noticia_box'})
    for contenido in contenidos:
        encabezado = contenido.find('h2', attrs={'class': 'notTituloDest notEfectDest'})
        if encabezado:
            titulos.append(encabezado.text)
        else:
            print("No se pudo obtener el encabezado")
        texto = contenido.find('div', attrs={'class': 'noticia_InfoTexto'})
        if texto:
            descripciones.append(texto.text)
        else:
            print("no se pudo obtener la descripcion")
        enlace = contenido.find('a', attrs={'class': 'datalayer_podcast'})['href']
        if enlace:
            enlaces.append(enlace)
        else:
            print("No se pudo obtener link")

    r = requests.get(url2)
    entries = BeautifulSoup(r.text, "html.parser")
    contenidos = entries.find_all('div', attrs={'class':'mod_noticia_box'})
    for contenido in contenidos:
        encabezado = contenido.find('h2', attrs={'class': 'notTituloDest notEfectDest'})
        if encabezado:
            titulos.append(encabezado.text)
        else:
            print("No se pudo obtener el encabezado")
        texto = contenido.find('div', attrs={'class': 'noticia_InfoTexto'})
        if texto:
            descripciones.append(texto.text)
        else:
            print("no se pudo obtener la descripcion")
        enlace = contenido.find('a')['href']
        if enlace != "#":
            enlaces.append(enlace)
        else:
            print("No se pudo obtener link")

def archivoPymes():
    df = pd.DataFrame({
        "Comunidad" : "Pymes",
        "Tiutlo":titulos,
        "Enlace":enlaces,
        "Descripción" : descripciones
    })
    df.to_excel('pymes.xlsx', index=False)
pymes("https://www.bbva.com/es/especiales/bbva-compartiendo-conocimiento/", "https://www.bbva.com/es/autores-invitados/communications/")
archivoPymes()
