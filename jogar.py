from selenium.webdriver.common.by import By
import time
from tabuleiro import verificar_valor_valido, capturar_celulas_vazias

def resolver_tabuleiro_sudoku(tabuleiro_sudoku):
    # Percorre toda a matriz 9x9 onde o valor é 0, que será preenchida com um novo valor válido (1 a 9) sem repetição dos valores horizontalmente e verticalmente nas células
    for linha in range(9):
        for coluna in range(9):
            if tabuleiro_sudoku[linha][coluna] == 0:
                for valor in range(1, 10):
                    if verificar_valor_valido(tabuleiro_sudoku, linha, coluna, valor):
                        tabuleiro_sudoku[linha][coluna] = valor
                    
                        if resolver_tabuleiro_sudoku(tabuleiro_sudoku):
                            return True
                        tabuleiro_sudoku[linha][coluna] = 0
                return False
    return True

def digitar_valor_tabuleiro(driver, tabuleiro_sudoku, celulas_vazias):
    tabuleiro = driver.find_element(By.CSS_SELECTOR, ".cells")
    celulas = driver.find_elements(By.CSS_SELECTOR, ".cell")

    # Injeção de Javascript para centralizar o tabuleiro corretamente para melhor visualização
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tabuleiro)

    # Chama a função de resolver toda a matriz 9x9 para que fique totalmente preenchida com os valores válidos
    tabuleiro_sudoku_resolvido = resolver_tabuleiro_sudoku(tabuleiro_sudoku)
    celula_atual = []
    
    # Se o tabuleiro for resolvido, percorre todas as linhas e colunas para digitar os valores que foram validados
    if tabuleiro_sudoku_resolvido:
        print("[INFO] O tabuleiro do Sudoku foi solucionado. Iniciando o preenchimento...")
        for (linha, coluna) in celulas_vazias:
            valor = tabuleiro_sudoku[linha][coluna]
            posicao = (linha * 9) + coluna
            celula_atual = celulas[posicao]
            celula_atual.click()
            time.sleep(0.30)
            driver.switch_to.active_element.send_keys(str(valor))
    else:
        print("[ERRO] Não foi possível realizar o preenchimento do tabuleiro.")
