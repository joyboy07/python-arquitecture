from browser_config import initialize_browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from decouple import config
from datetime import datetime
from dateutil.relativedelta import relativedelta

def process_sunat_request(montante=None):
    driver = initialize_browser()
    driver.get("https://api-seguridad.sunat.gob.pe/v1/clientessol/4f3b88b3-d9d6-402a-b85d-6a0bc857746a/oauth2/loginMenuSol?originalUrl=https://e-menu.sunat.gob.pe/cl-ti-itmenu/AutenticaMenuInternet.htm&state=rO0ABXNyABFqYXZhLnV0aWwuSGFzaE1hcAUH2sHDFmDRAwACRgAKbG9hZEZhY3RvckkACXRocmVzaG9sZHhwP0AAAAAAAAx3CAAAABAAAAADdAAEZXhlY3B0AAZwYXJhbXN0AEsqJiomL2NsLXRpLWl0bWVudS9NZW51SW50ZXJuZXQuaHRtJmI2NGQyNmE4YjVhZjA5MTkyM2IyM2I2NDA3YTFjMWRiNDFlNzMzYTZ0AANleGVweA")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnPorDni"))).click()

    user = driver.find_element(By.ID,"txtDni")
    user.clear()
    user.send_keys(config('USERUC'))
    password = driver.find_element(By.ID,"txtContrasena")
    password.clear()
    password.send_keys(config('PASSWORD'))

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btnAceptar"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nivel1_11"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nivel2_11_5"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nivel2Cuerpo_11_5"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nivel4_11_5_1_1_2"))).click()

    try:
        iframe = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "iframeApplication"))
        )
        driver.switch_to.frame(iframe)
        boton_continuar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "wacepta"))
        )
        boton_continuar.click()
        print("Cambiado al iframe correctamente.")
    except Exception as e:
        print(f"No se pudo encontrar el iframe: {str(e)}")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "formaPago2"))).click()

    rucDocument = driver.find_element(By.ID,"numdoc")
    rucDocument.clear()
    rucDocument.send_keys("20131369981")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "wvalidar"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "wacepta"))).click()

    ## formularios 2
    descripcion = driver.find_element(By.NAME,"motivo")
    descripcion.clear()
    descripcion.send_keys(config('DESCRIPTION'))

    observacion = driver.find_element(By.NAME,"observacion")
    observacion.clear()
    observacion.send_keys("-")

    radioButonNo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="indretencion"][value="00"]')))
    radioButonNo.click()

    try:
        x = driver.find_element(By.ID, "totalHonorarios")
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except Exception as e:
            print("No se encontró ninguna alerta.")
        x.click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.HOME).perform()
        actions.send_keys(montante if montante is not None else config('MONT')).perform()  # Usar el montante proporcionado o el predeterminado
        actions.send_keys(Keys.ENTER).perform()

    except Exception as e:
        print(f"Error: {e}")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "addCuota"))).click()
    fecha_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "fecCuotaId"))
    )

    # Habilitar el campo de entrada de fecha
    driver.execute_script("arguments[0].removeAttribute('disabled');", fecha_input)

    # Establecer el valor de la fecha
    fecha_input.clear()

    fecha_actual = datetime.now()
    fecha_nueva = fecha_actual + relativedelta(months=1)

    fecha_formateada = fecha_nueva.strftime("%d/%m/%Y")

    fecha_input.send_keys(fecha_formateada)

    try:
        cantidad = driver.find_element(By.ID, "valorCuota")
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except Exception as e:
            print("No se encontró ninguna alerta.")
        cantidad.click()
        actions = ActionChains(driver)
        actions.send_keys(Keys.HOME).perform()
        actions.send_keys(montante if montante is not None else config('MONT')).perform()  # Usar el montante proporcionado o el predeterminado
        actions.send_keys(Keys.ENTER).perform()

    except Exception as e:
        print(f"Error: {e}")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "addModifCuota"))).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "wacepta"))).click()

    # Emitir = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "wacepta"))).click()

    # try:
    #     descargar = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Presione este link para descargar el archivo pdf del Recibo por Honorarios Electrónico. "]'))
    #     )
    #     descargar.click()
    # except TimeoutException:
    #     print("El enlace de descarga no está disponible.")

    time.sleep(10)


if __name__ == "__main__":
    process_sunat_request()
