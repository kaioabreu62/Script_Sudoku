from selenium.webdriver.common.by import By


def capturar_tabuleiro_dia(driver):
    try:
        celulas = driver.find_elements(By.CSS_SELECTOR, ".cell-inner")
        tabuleiro_sudoku = [[0]*9 for num in range(9)] # inicia uma matriz 9x9 com todas as linhas e colunas preenchidas com 0
        
        # Percorre todas as linhas e colunas de uma matriz 9x9
        for i, celula in enumerate(celulas):
            linha = i // 9  # divisão inteira por 9 para definir o índice da linha (0 a 8)
            coluna = i % 9  # resto da divisão por 9 para definir o índice da coluna (0 a 8)
            valor = celula.text.strip() 
            if valor.isdigit(): # se o texto da célula atual for um número inteiro, converte para int; caso contrário manter o valor como 0
                tabuleiro_sudoku[linha][coluna] = int(valor)
            else:
                tabuleiro_sudoku[linha][coluna] = 0

        return tabuleiro_sudoku
    except Exception as e:
        print("[ERRO] Não foi possível capturar os elementos do tabuleiro Sudoku.")

def capturar_celulas_vazias(tabuleiro_sudoku):
    vazias = []

    for i in range(9):
        for j in range(9):
            if tabuleiro_sudoku[i][j] == 0:
                vazias.append((i, j))
    return vazias

def verificar_valor_valido(tabuleiro_sudoku, linha, coluna, valor):

    # Verifica se o valor já foi preenchido na linha; caso contrário poderá ser preenchido com um valor válido
    for i in range(9):
        if tabuleiro_sudoku[linha][i] == valor: 
            return False
    # Verifica se o valor já foi preenchido na coluna; caso contrário poderá ser preenchido com um valor válido
    for j in range(9):
        if tabuleiro_sudoku[j][coluna] == valor:
            return False
    # Identifica a região do quadrante 3x3 para verificar onde deve ser preenchido com um valor válido
    bloco_linha = (linha // 3 ) * 3 
    bloco_coluna = (coluna // 3) * 3
    # Percorre a região do quadrante 3x3 se estiver preenchida, nenhum valor novo será preenchido 
    for i in range(3):
        for j in range(3):
            if tabuleiro_sudoku[i + bloco_linha][j + bloco_coluna] == valor: # verifica-se os blocos 3x3 das linhas e colunas já possuem valores, se for retorna Falso
                return False
    return True # Se todas as regras forem cumpridas, a célula acessada poderá ser preenchida com um valor (1, 9) retornando Verdadeiro para a operação
   
              
