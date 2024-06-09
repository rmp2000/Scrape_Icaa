import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time
from scrap_page import iteraciones_pelis 

def iteraciones_pelis_año(url_padre,year):
    data = {
        'Dirigido por': [],
        'Título Original': [],
        'Título en Inglés': [],
        'Calificación': [],
        'Año de Producción': [],
        'Fecha de Estreno': [],
        'Duración': [],
        'Tipo': [],
        'Género': [],
        'Nacionalidad': [],
        'Breve sinopsis': [],
        'Intérpretes': [],
        'Productor': [],
        'Productor ejecutivo': [],
        'Dirección de producción': [],
        'Guión': [],
        'Dirección de fotografía': [],
        'Productoras': [],
    }
    df = pd.DataFrame(data)
    driver = webdriver.Chrome()
    driver.get(url_padre)
    wait = WebDriverWait(driver, 10)
    time.sleep(1)
    element = driver.find_element(By.XPATH, "//*[@id='filter_p_prod']")
    element.click()
    time.sleep(1)
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'filter_p_prod')))
    select = Select(select_element)
    select.select_by_visible_text(str(year))
    time.sleep(1)
    element_search = driver.find_element(By.XPATH, "//*[@id='buttonSearchMovies']")
    element_search.click()
    time.sleep(2)
    
    element_siguiente_presente = True

    while element_siguiente_presente:
        try:
            page_source = driver.page_source
            element_siguiente = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "PagedList-skipToNext")))
            list_url(page_source,data,df)
            time.sleep(1)
            element_siguiente.click()
            time.sleep(2)  
            
        except:
            element_siguiente_presente = False
    
    page_source = driver.page_source
    list_url(page_source,data,df)
    return df

def list_url(page_source,data,df):
    soup = BeautifulSoup(page_source, 'html.parser')
    lista_url = soup.find_all("div", class_="sin-list-pro fix")
    for films in lista_url:
        aux=films.find_all("a","list-pro-title")
        df=iteraciones_pelis(aux[0]['href'],df,data)