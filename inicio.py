from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def iniciar_jogo(driver):
    try:
        try:
            botao_iniciar_jogo_dificil = driver.find_element(By.XPATH, "//button[text()='Difícil']")
            botao_iniciar_jogo_dificil.click()
            time.sleep(0.60)

            botao_fechar_ajuda = WebDriverWait(driver, 0.60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button--game-white.svelte-1ybwuxd")))
            botao_fechar_ajuda.click()
            time.sleep(0.60)
        except:
            pass

            botao_iniciar_jogo_dificil = driver.find_element(By.XPATH, "//button[text()='Difícil']")
            botao_iniciar_jogo_dificil.click()
            time.sleep(0.60)

            botao_fechar_ajuda = WebDriverWait(driver, 0.60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button--game-white.svelte-1ybwuxd")))
            botao_fechar_ajuda.click()
            time.sleep(0.60)
    except Exception as e:
        print("[ERRO] Não foi possível clicar no botão iniciar jogo na dificuldade difícil", e)
            