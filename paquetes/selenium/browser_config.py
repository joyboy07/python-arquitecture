from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from decouple import config

def initialize_browser():
    service = Service(executable_path=config('URL'))
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver
