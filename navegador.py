from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_navegador(url):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    return driver

def fechar_navegador(driver):
    driver.quit()