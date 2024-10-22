import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys

def get_chromedriver_path():
    # Solo se obtiene la ruta del directorio actual
    base_path = os.path.dirname(os.path.abspath(__file__))

    chromedriver_path = os.path.join(base_path, 'chromedriver-win32', 'chromedriver.exe')
    print(f"Chromedriver path: {chromedriver_path}")  # Imprime la ruta que se está buscando
    return chromedriver_path

def initialize_browser():
    service = Service(executable_path=get_chromedriver_path())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

if __name__ == "__main__":
    driver = initialize_browser()
    driver.quit()
