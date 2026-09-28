from config import URL
from navegador import iniciar_navegador, fechar_navegador
from inicio import iniciar_jogo
from tabuleiro import capturar_tabuleiro_dia, capturar_celulas_vazias
from jogar import resolver_tabuleiro_sudoku, digitar_valor_tabuleiro
import time

def main():

    driver = iniciar_navegador(URL)

    iniciar_jogo(driver)
    print("[INFO] Jogo iniciado com sucesso na dificuldade difícil")

    tabuleiro_sudoku = capturar_tabuleiro_dia(driver)

    # deslocar 12 caracteres de espaços da esquerda do console
    deslocamento_espaco = " " * 12

    titulo_tabuleiro_dia = "---Tabuleiro Sudoku do dia---"
    print(deslocamento_espaco + titulo_tabuleiro_dia.center(32) + "\n")

    # Percorre todas as linhas e colunas do tabuleiro do dia para printar a matriz 9x9 sem resolução no console
    for i, linha in enumerate(tabuleiro_sudoku):
        if i % 3 == 0 and i != 0:
            print(deslocamento_espaco + "-" * 30)
        print(deslocamento_espaco, end="")
        for j, valor in enumerate(linha):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(f"{valor:2}", end=" ")
        print("\n")

    celulas_vazias = capturar_celulas_vazias(tabuleiro_sudoku)
    resolver = resolver_tabuleiro_sudoku(tabuleiro_sudoku)

    # Se o tabuleiro for resolvido, percorre todas as linhas e colunas do tabuleiro do dia e preenche com os valores faltantes válidos
    if resolver:
        digitar_valor_tabuleiro(driver, tabuleiro_sudoku, celulas_vazias)

        titulo_tabuleiro_resolvido = "--Tabuleiro Sudoku Resolvido--"
        print(deslocamento_espaco + titulo_tabuleiro_resolvido.center(32) + "\n")

        # Percorre todas a linhas e colunas do tabuleiro do dia para printar a matriz 9x9 com resolução no console
        for i, linha in enumerate(tabuleiro_sudoku):
            if i % 3 == 0 and i != 0:
                print(deslocamento_espaco + "-" * 30)
            print(deslocamento_espaco, end="")
            for j, valor in enumerate(linha):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(f"{valor:2}", end=" ")
            print("\n")
    else:
        print("[ERRO] Não foi possível encontrar uma solução para este tabuleiro.")


    time.sleep(0.95)
    # Injeção de Javascript para remoção de pop-up de resultado final obtido
    script_remover_popup_final = """
    var popups = document.querySelectorAll('[class*="modal"], [class*="overlay"], [class*="popup"]');
    popups.forEach(function(el) { el.remove(); });
    """
    driver.execute_script(script_remover_popup_final)        

    input("Pressione 'ENTER' para fechar o navegador...")
    fechar_navegador(driver)


if __name__ == "__main__":
    main()