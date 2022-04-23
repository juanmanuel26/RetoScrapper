from calendar import c
from operator import index
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
import pandas as pd
import time
#Inicializar la variable contenedora del controlador de Edge
driver = webdriver.Edge(r"C:\Users\Natyy\OneDrive\Escritorio\reto-talentpitch\msedgedriver.exe")
#abrir la página de emprendedores
whatsApp = "https://web.whatsapp.com/"
driver.get(whatsApp)

articulos = []

def envio():
    df = pd.read_excel('emprendedores.xlsx',  usecols=['Comunidad', 'Titulo', 'Descripción'])
    comunidad = df['Comunidad'].unique()
    mensaje = []
    if len(mensaje) != 5:
        for i in range(5):
            articulo = df[df['Comunidad'] == comunidad[0].sample(1).to_string(header=False, index=False)]
            if not comunidad in articulos:
                articulos.append(articulo)
                mensaje.append(articulo)
                cadenaM = '\n'.join([str])

#time.sleep(20)
    
group = 'Prueba'

title_search = 'Cuadro de texto para ingresar la búsqueda'
text_search ='Escribe un mensaje aquí'
search_box = driver.find_element(By.XPATH, "//div[@title='{}']".format(title_search))
search_box.send_keys(group)
item = driver.find_element(By.XPATH,'//span[@title="{}"]'.format(group))
item.click()
message_box = driver.find_element(By.XPATH,"//div[@title='{}']".format(text_search))
#message = get_article()
article = 'Holiii'
message_box.send_keys(article)
message_box.send_keys(Keys.ENTER)