import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pya

grupos = "grupos.xlsx"
try:
    df = pd.read_excel(grupos)
except FileNotFoundError:
    print("Arquivo não encontrado: ", grupos)
    df = pd.DataFrame()
    
PATH = (r"C:\Users\mayco\Documents\Jupyter Testes\zapzap\zapzap\chromedriver.exe")
try:
    navegador = webdriver.Chrome(executable_path='chromedriver.exe')
except Exception as e:
    print("Não foi possível iniciar o navegador. Erro: ", e)
    navegador = None
    
if navegador:
    navegador.get ("https://web.whatsapp.com/")
    time.sleep(60)

    for index,row in df.iterrows():
        navegador.get (row['link'])
        time.sleep(10)

    for index,row in df.iterrows():
    ###clicando em cadastrar
        ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        try:
            select1 = WebDriverWait(navegador,10,ignored_exceptions=ignored_exceptions)\
                            .until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='action-button]'}")))
            select1.click()
            time.sleep(5)
        except Exception as e:
            print("Não foi possível clicar no elemento. Erro: ", e)
            continue

        try:
            select2 = navegador.find_element("xpath","//*[@id='fallback_block']/div/h4/a/span");
            select2.click();
            time.sleep(10);
        except Exception as e:
            print("Não foi possível clicar no elemento. Erro: ", e)
            continue

        try:
            select3 = navegador.find_element("xpath","//*[@id='app']/div/span[2]/div/div/div/div/div/div/div[2]/div/div[2]")
            select3.click()
            time.sleep(10)
        except Exception as e:
            print("Não foi possível clicar no elemento. Erro: ", e)
            continue

