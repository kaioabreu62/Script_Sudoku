# 🧩 Script Sudoku

Automação em Python para o jogo **Sudoku**, utilizando **Selenium WebDriver** para acessar o jogo, capturar automaticamente o tabuleiro e resolver o desafio por meio de um algoritmo de **backtracking**.

Após encontrar uma solução válida, o programa preenche automaticamente as células vazias do Sudoku no navegador.

> **Aviso:** Este é um projeto independente, desenvolvido para fins de estudo e aprendizado em Python, algoritmos e automação web. Não possui afiliação oficial com o G1 ou com a Globo.

---

## 🎯 Objetivo

O objetivo do projeto é automatizar a resolução do Sudoku disponível no G1.

O programa realiza as seguintes etapas:

1. Abre o Google Chrome;
2. Acessa o jogo Sudoku;
3. Inicia automaticamente o desafio na dificuldade **Difícil**;
4. Captura o tabuleiro apresentado;
5. Converte o tabuleiro para uma matriz `9x9`;
6. Identifica as células vazias;
7. Resolve o Sudoku utilizando backtracking;
8. Preenche automaticamente as células vazias no navegador;
9. Exibe o tabuleiro original no terminal;
10. Exibe o tabuleiro resolvido;
11. Remove o pop-up final da página;
12. Aguarda a confirmação do usuário antes de fechar o navegador.

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* **Selenium WebDriver**
* **WebDriver Manager**
* **Google Chrome**
* **JavaScript**
* **Algoritmo de Backtracking**
* **Recursividade**
* **Git / GitHub**

---

## 📂 Estrutura do projeto

```text
Script_Sudoku/
│
├── .gitignore
├── config.py
├── inicio.py
├── jogar.py
├── main.py
├── navegador.py
├── tabuleiro.py
└── README.md
```

---

## 🧠 Como o projeto funciona

O projeto é dividido em módulos, cada um responsável por uma parte específica da automação.

```text
                    ┌─────────────────┐
                    │     main.py     │
                    │ Ponto de entrada│
                    └────────┬────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │     navegador.py    │
                  │ Abre o Google Chrome│
                  └──────────┬──────────┘
                             │
                             ▼
                     ┌───────────────┐
                     │   inicio.py   │
                     │ Inicia o jogo │
                     └───────┬───────┘
                             │
                             ▼
                    ┌────────────────┐
                    │   tabuleiro.py │
                    │ Captura Sudoku │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │    jogar.py    │
                    │ Resolve Sudoku │
                    └───────┬────────┘
                            │
                            ▼
                    ┌────────────────┐
                    │ Selenium/Web   │
                    │ Preenche células│
                    └────────────────┘
```

---

## 📄 Descrição dos arquivos

### `main.py`

É o ponto de entrada da aplicação e coordena todo o fluxo.

O programa:

* Inicializa o navegador;
* Inicia o jogo;
* Captura o Sudoku;
* Exibe o tabuleiro original;
* Identifica as células vazias;
* Resolve o tabuleiro;
* Preenche as células no navegador;
* Exibe o resultado;
* Remove o pop-up final;
* Fecha o navegador.

O fluxo principal está concentrado nesse arquivo.

---

### `navegador.py`

Responsável pelo gerenciamento do Google Chrome.

O projeto utiliza:

```python
webdriver
Service
ChromeDriverManager
```

O `webdriver-manager` é utilizado para instalar/gerenciar o ChromeDriver automaticamente.

O navegador também é iniciado maximizado.

```python
options.add_argument("start-maximized")
```

Ao final da execução, o navegador é encerrado utilizando:

```python
driver.quit()
```

---

### `inicio.py`

Responsável por iniciar a partida.

O script procura especificamente pelo botão:

```text
Difícil
```

utilizando XPath:

```python
//button[text()='Difícil']
```

Depois de iniciar o jogo, o programa tenta fechar a tela de ajuda apresentada pelo Sudoku.

Para aguardar os elementos, o projeto utiliza:

```python
WebDriverWait
```

e:

```python
expected_conditions
```

---

### `tabuleiro.py`

É o módulo responsável pela captura e validação do tabuleiro.

#### Captura do tabuleiro

O programa localiza as células utilizando:

```css
.cell-inner
```

Depois cria uma matriz:

```python
9 x 9
```

Inicialmente preenchida com zeros.

Cada célula encontrada é convertida para a posição correspondente da matriz utilizando:

```python
linha = i // 9
coluna = i % 9
```

Quando a célula contém um número, ele é convertido para `int`.

Quando está vazia, recebe:

```python
0
```

---

### Captura das células vazias

A função:

```python
capturar_celulas_vazias()
```

percorre toda a matriz `9x9` e registra as posições que possuem:

```python
0
```

Por exemplo:

```text
(0, 2)
(0, 5)
(1, 1)
(2, 7)
```

Essas coordenadas são utilizadas posteriormente para saber exatamente quais células precisam ser preenchidas no navegador.

---

### Validação de valores

A função:

```python
verificar_valor_valido()
```

verifica as três regras fundamentais do Sudoku:

#### 1. Linha

O número não pode existir anteriormente na mesma linha.

#### 2. Coluna

O número não pode existir anteriormente na mesma coluna.

#### 3. Bloco 3×3

O número não pode existir anteriormente no bloco correspondente.

Para localizar o bloco 3×3, o código utiliza:

```python
bloco_linha = (linha // 3) * 3
bloco_coluna = (coluna // 3) * 3
```

Dessa maneira, o algoritmo consegue determinar corretamente qual região 3×3 deve ser analisada.

---

## 🧮 Algoritmo de Backtracking

A resolução do Sudoku utiliza **backtracking**, uma técnica de busca recursiva bastante utilizada para problemas de restrições.

O algoritmo segue basicamente este fluxo:

```text
Encontrar uma célula vazia
          ↓
Testar números de 1 a 9
          ↓
O número é válido?
      ↙         ↘
    Não          Sim
    ↓             ↓
Próximo       Inserir número
                 ↓
          Resolver próxima célula
                 ↓
             Funcionou?
             ↙       ↘
           Não       Sim
           ↓          ↓
       Remover      Continuar
        número
           ↓
      Tentar outro
```

No código, isso acontece dentro da função:

```python
resolver_tabuleiro_sudoku()
```

A função percorre as posições vazias, tenta valores de `1` a `9` e chama a si mesma novamente para continuar a resolução.

Caso uma escolha leve a um caminho sem solução, o valor é removido e outro número é testado.

Esse processo continua até encontrar uma solução válida ou até que todas as possibilidades sejam descartadas.

---

## 🤖 Preenchimento automático

Depois que o Sudoku é solucionado, o programa utiliza Selenium para preencher as células vazias.

Primeiro, ele localiza:

```css
.cells
```

e depois todas as células:

```css
.cell
```

Para cada posição vazia, o programa calcula a posição correspondente na lista de células:

```python
posicao = (linha * 9) + coluna
```

Depois:

1. Localiza a célula;
2. Realiza um clique;
3. Obtém o elemento ativo;
4. Envia o número correspondente.

O número é enviado utilizando:

```python
driver.switch_to.active_element.send_keys(str(valor))
```

---

## 🌐 Injeção de JavaScript

O projeto também utiliza JavaScript diretamente no navegador.

### Centralização do tabuleiro

Antes de preencher os valores, o programa utiliza:

```javascript
arguments[0].scrollIntoView({block: 'center'});
```

Isso faz com que o tabuleiro seja centralizado na janela do navegador.

### Remoção do pop-up

Depois da resolução, o projeto executa JavaScript para remover elementos que possam representar:

```text
modal
overlay
popup
```

O objetivo é evitar que o pop-up de resultado final atrapalhe a visualização do tabuleiro.

Essa lógica está implementada no `main.py`.

---

## ⚙️ Configuração

A URL utilizada pelo projeto está centralizada em `config.py`:

```python
URL = "https://g1.globo.com/jogos/sudoku/"
```

Essa separação permite alterar o endereço do jogo sem precisar modificar o código principal.

---

## 📥 Requisitos

Para executar o projeto, é necessário possuir:

* Python 3;
* Google Chrome;
* Conexão com a internet;
* Selenium;
* WebDriver Manager.

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/kaioabreu62/Script_Sudoku.git
```

### 2. Entre na pasta

```bash
cd Script_Sudoku
```

### 3. Instale as dependências

```bash
pip install selenium webdriver-manager
```

---

## ▶️ Executando o projeto

Execute o arquivo principal:

```bash
python main.py
```

O fluxo será:

```text
Abrir Chrome
     ↓
Acessar Sudoku
     ↓
Selecionar "Difícil"
     ↓
Capturar tabuleiro
     ↓
Mostrar tabuleiro no terminal
     ↓
Encontrar células vazias
     ↓
Resolver Sudoku
     ↓
Preencher navegador
     ↓
Mostrar solução
     ↓
Remover pop-up
     ↓
Aguardar ENTER
     ↓
Fechar navegador
```

---

## 🖥️ Visualização no terminal

O programa também apresenta o Sudoku no terminal utilizando uma representação visual da matriz `9x9`.

As divisões dos blocos 3×3 são representadas por separadores horizontais e verticais.

Exemplo:

```text
             ---Tabuleiro Sudoku do dia---

              5  3  0 | 0  7  0 | 0  0  0
              6  0  0 | 1  9  5 | 0  0  0
              0  9  8 | 0  0  0 | 0  6  0
              ------------------------------
              8  0  0 | 0  6  0 | 0  0  3
              4  0  0 | 8  0  3 | 0  0  1
              7  0  0 | 0  2  0 | 0  0  6
              ------------------------------
              0  6  0 | 0  0  0 | 2  8  0
              0  0  0 | 4  1  9 | 0  0  5
              0  0  0 | 0  8  0 | 0  7  9
```

Depois da resolução, o mesmo tabuleiro é exibido novamente com os valores preenchidos.

---

## 🧠 Conceitos utilizados

Este projeto aplica diversos conceitos importantes de programação:

* Python;
* Programação modular;
* Funções;
* Listas;
* Matrizes;
* Recursividade;
* Backtracking;
* Algoritmos de busca;
* Validação de restrições;
* Manipulação de matrizes;
* Selenium WebDriver;
* Seletores CSS;
* XPath;
* `WebDriverWait`;
* JavaScript;
* Manipulação do DOM;
* Automação de navegador.

---

## 🚧 Possíveis melhorias

Algumas melhorias podem ser implementadas futuramente:

* [ ] Criar um `requirements.txt`;
* [ ] Adicionar tratamento de exceções mais específico;
* [ ] Substituir `time.sleep()` por esperas explícitas sempre que possível;
* [ ] Criar testes automatizados para o algoritmo de Sudoku;
* [ ] Separar completamente a lógica do Sudoku da automação Selenium;
* [ ] Criar uma classe para representar o tabuleiro;
* [ ] Adicionar suporte para outras dificuldades;
* [ ] Permitir selecionar a dificuldade através de configuração;
* [ ] Melhorar os seletores utilizados pelo Selenium;
* [ ] Criar logs estruturados;
* [ ] Medir o tempo necessário para solucionar o tabuleiro;
* [ ] Adicionar validação para tabuleiros sem solução;
* [ ] Criar uma interface gráfica para acompanhar a resolução;
* [ ] Adicionar screenshots durante a execução.

---

## ⚠️ Observações

O projeto depende da estrutura HTML do jogo.

Como o Selenium utiliza seletores específicos, alterações futuras na página podem fazer com que partes da automação deixem de funcionar.

Por exemplo, a captura do tabuleiro depende atualmente do seletor:

```css
.cell-inner
```

e o preenchimento utiliza:

```css
.cell
```

A inicialização também depende do botão de dificuldade **"Difícil"** e de elementos específicos utilizados para fechar a tela de ajuda.

---

## 🎓 Finalidade do projeto

Este projeto foi desenvolvido como uma aplicação prática de **Python, algoritmos e automação web**.

Através dele, são combinados:

**Python + Selenium + Backtracking + Recursividade + Manipulação de Matrizes + Automação de Navegador.**

O projeto demonstra como um algoritmo clássico de resolução de Sudoku pode ser integrado a uma aplicação de automação web para capturar um problema real, solucioná-lo e enviar a solução de volta para a página.

---

## 👨‍💻 Autor

**Kaio Abreu**

GitHub: [kaioabreu62](https://github.com/kaioabreu62)

---

## 📄 Licença

Este projeto não possui uma licença de software definida no momento.

Caso o projeto seja disponibilizado para reutilização por terceiros, recomenda-se adicionar uma licença de código aberto de acordo com a intenção do autor.
