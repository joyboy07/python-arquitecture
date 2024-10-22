# main.py
from browser_config import initialize_browser

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from decouple import config
import time

def submit_form(sede:str, titulo:str,  descripcion:str ):
    driver = initialize_browser()
    try:
        driver.get(config('URLWEB'))

        user = driver.find_element(By.ID, "username")
        user.clear()
        user.send_keys(config('USER'))

        password = driver.find_element(By.ID, "clave")
        password.clear()
        password.send_keys(config('PASSWORD'))

        input_element = driver.find_element(By.ID, "a")
        default_value = input_element.get_attribute("value")
        resultado = driver.find_element(By.ID, "b")
        resultado.clear()
        resultado.send_keys(eval(default_value))

        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_ingresar"))
        )
        button.click()

        li_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "n_01"))
        )
        enlace = li_element.find_element(By.TAG_NAME, "a")
        enlace.click()

        input_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.custom-combobox-input'))
        )
        input_element.clear()
        input_element.send_keys(titulo)

        title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'titulo'))
        )
        title.clear()
        title.send_keys(titulo)

        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".select2-selection__arrow"))
        )
        dropdown_button.click()
        option_to_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{sede}')]"))
        )
        option_to_select.click()

        description = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'descripcion_incidencia'))
        )
        description.clear()
        description.send_keys(descripcion)

        # buttonInsidencia = WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.ID, 'btn_guardar_inc'))
        # )
        # buttonInsidencia.click()
        time.sleep(5)
    finally:
        driver.quit()


if __name__ == "__main__":
    submit_form('Sede Central','Otros','Prueba')