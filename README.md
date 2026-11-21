# 📊 Análise Estatística Descritiva com Python

Projeto desenvolvido para a disciplina de **Estatística**, utilizando **Python** e as bibliotecas **Pandas** e **Matplotlib** para realizar a análise exploratória, tabulação de frequências, cálculo de medidas estatísticas e visualização gráfica de um conjunto de dados de alturas ($n = 50$).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas** — Leitura, tratamento e cálculos estatísticos sobre o DataFrame `dados`
* **Matplotlib** — Geração, estilização e exportação dos gráficos estatísticos
* **Math & OS** — Cálculos matemáticos auxiliares e gerenciamento de diretórios

---

## 📁 Estrutura do Projeto

```text
├── dados/
│   ├── banco_de_dados_alturas.csv       # Base original (50 registros, 2 variáveis)
│   └── banco_de_dados_alturas_2.csv     # Base expandida com variáveis adicionais
├── graficos/
│   ├── histograma_alturas.png           # Histograma com média, mediana e moda
│   ├── poligono_frequencias.png         # Polígono de frequências absolutas
│   ├── boxplot_alturas.png              # Diagrama de caixa com quartis e outlier
│   └── ogiva_frequencia_acumulada.png   # Ogiva de frequência relativa acumulada (%)
├── analise_estatistica.py               # Script principal da análise
└── README.md                            # Documentação do projeto
```

---

## 🔍 Etapas da Análise

### 1. Exploração e Validação dos Dados
* Carregamento do arquivo `dados/banco_de_dados_alturas.csv` (`sep=';'`, `decimal=','`).
* Inspeção dos **5 primeiros registros** (`dados.head()`).
* Verificação da dimensão da base: **50 registros** e **2 variáveis** (`Pessoa` e `Altura_m`).
* Checagem de integridade: **0 dados ausentes** em todas as colunas.

### 2. Parâmetros para Agrupamento em Classes
* **Tamanho da amostra ($n$):** `50`
* **Número de classes ($K = \text{round}(\sqrt{n})$):** `7`
* **Valor mínimo / máximo:** `1,54 m` e `1,93 m`
* **Amplitude total ($A_t$):** `39 cm` (`0,39 m`)
* **Amplitude do intervalo de classe ($h = \text{round}(A_t / K)$):** `6 cm` (`0,06 m`)

### 3. Tabela de Distribuição de Frequências

| Classes (m) | Ponto Médio ($x_i$) | Freq. Absoluta ($f_i$) | Freq. Acumulada ($F_{ac}$) | Freq. Relativa ($f_r\%$) | Freq. Rel. Acumulada ($F_{ac}\%$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **1.54 \|-- 1.60** | 1,57 | 5 | 5 | 10,0% | 10,0% |
| **1.60 \|-- 1.66** | 1,63 | 12 | 17 | 24,0% | 34,0% |
| **1.66 \|-- 1.72** | 1,69 | 16 | 33 | 32,0% | 66,0% |
| **1.72 \|-- 1.78** | 1,75 | 10 | 43 | 20,0% | 86,0% |
| **1.78 \|-- 1.84** | 1,81 | 5 | 48 | 10,0% | 96,0% |
| **1.84 \|-- 1.90** | 1,87 | 1 | 49 | 2,0% | 98,0% |
| **1.90 \|-- 1.96** | 1,93 | 1 | 50 | 2,0% | 100,0% |

### 4. Medidas de Posição, Separatrizes e Dispersão

| Categoria | Medida Estatística | Resultado |
| :--- | :--- | :---: |
| **Posição** | Média | `1,6920 m` |
| **Posição** | Moda | `1,69 m` |
| **Posição / Separatriz** | Mediana ($Q_2$) | `1,69 m` |
| **Separatriz** | 1º Quartil ($Q_1$ — 25%) | `1,63 m` (`1,6325 m`) |
| **Separatriz** | 3º Quartil ($Q_3$ — 75%) | `1,73 m` |
| **Dispersão** | Desvio Padrão Amostral ($s$) | `0,0778 m` |
| **Dispersão** | Coeficiente de Variação ($CV$) | `4,60%` |

### 5. Visualizações Gráficas (`Matplotlib`)
Os gráficos são exibidos em tela após a execução dos cálculos no terminal e salvos automaticamente em alta resolução (`300 dpi`) na pasta `graficos/`:
* **Histograma:** apresenta a distribuição de frequências por classe com as marcações de média, mediana e moda.
* **Polígono de Frequências:** destaca o comportamento da curva de frequências através dos pontos médios ($x_i$).
* **Boxplot (Diagrama de Caixa):** evidencia a concentração interquartil ($Q_1$ a $Q_3$), a mediana ($Q_2$) e o valor discrepante (*outlier*) em `1,93 m`, acompanhado de legenda descritiva.
* **Ogiva de Frequência Acumulada / Dispersão por Quartis:** permite acompanhar o crescimento percentual acumulado da amostra e a posição individual de cada registro frente aos quartis.

---

## 📈 Principais Conclusões

* **Tendência Central Simétrica:** A proximidade entre média (`1,6920 m`), mediana (`1,69 m`) e moda (`1,69 m`) indica uma distribuição bastante equilibrada em torno do centro, com maior concentração na classe `1,66 |-- 1,72 m` (**32%** da amostra).
* **Baixa Dispersão:** O coeficiente de variação de **4,60%** (abaixo do limiar clássico de 15%) demonstra que o grupo analisado é homogêneo em relação à estatura.
* **Presença de Outlier:** O boxplot identifica apenas um valor discrepante superior (`1,93 m`, referente ao registro `P18`), enquanto 50% das observações centrais situam-se entre `1,63 m` ($Q_1$) e `1,73 m` ($Q_3$).

---
