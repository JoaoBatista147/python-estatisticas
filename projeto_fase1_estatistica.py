import pandas as pd 
import math 
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

dados = pd.read_csv('dados/banco_de_dados_alturas.csv', sep=';', decimal=',')

#VERIFICACOES

# Quantidade de registros (linhas) e quantidade de variáveis (colunas)
registros, variaveis = dados.shape
print(f'\n\nQuantidade de registros: {registros}')
print(f'Quantidade de variáveis: {variaveis}\n')

# 5 primeiros registros
print('\n\n5 primeiros registros:')
print(dados.head())

# Verificação de dados ausentes
print('\n\nQuantidade de dados ausentes por variável:')
print(dados.isnull().sum().to_string(), '\n')
print('=' * 30)

#CALCULOS

# n corresponde ao total de dados
n = len(dados)
print(f'\n\nn = {n} --> Total de dados')

# k é a raiz de n --> k corresponde ao número de classes
k = round(math.sqrt(n))
print(f'k = {k} --> Número de classes')

# valor minimo e maximo da coluna alturas
valor_max = dados['Altura_m'].max()
valor_min = dados['Altura_m'].min()

# amplitude total (At) é max-min
amplitude_total = int(round((valor_max - valor_min) * 100))

# h é a amplitude/k --> h corresponde ao intervalo de classes
h = int(round(amplitude_total / k))
print(f'h = {h} --> Intervalo de classes')

#TABELA DE DISTRIBUICAO
print('\n' + '=' * 30)
limites = [round(valor_min + i * (h / 100), 2) for i in range(k + 1)]
rotulos = [f'{limites[i]:.2f} |-- {limites[i+1]:.2f}' for i in range(k)]
classes = pd.cut(dados['Altura_m'], bins=limites, labels=rotulos, right=False)

# Frequência absoluta (fi), acumulada (Fac), relativa (%) e ponto médio (xi)
fi = classes.value_counts().sort_index()
fac = fi.cumsum()
fr_perc = (fi / n) * 100
fac_perc = fr_perc.cumsum()
ponto_medio = [round((limites[i] + limites[i+1]) / 2, 2) for i in range(k)]

tabela_frequencia = pd.DataFrame({
    'Classes': rotulos,
    'xi': ponto_medio,
    'fi': fi.values,
    'Fac': fac.values,
    'fr (%)': fr_perc.values,
    'Fac (%)': fac_perc.values
})

print('\n\nTabela de Distribuição de Frequências:')
print(tabela_frequencia.to_string(index=False))

#MEDIDAS DE POSICAO
print('\n' + '=' * 30)
print('\nMedidas de Posição:')

#MEDIA
media = dados['Altura_m'].mean()
print(f'\nMédia: {media:.4f} m')

#MODA
moda = dados['Altura_m'].mode()[0]
print(f'Moda: {moda:.2f} m')

#MEDIANA
mediana = dados['Altura_m'].median()
print(f'Mediana: {mediana:.2f} m')

#MEDIDAS DE DISPERSAO
print('\n' + '=' * 30)
print('\nMedidas de Dispersão:')

#DESVIO PADRAO
desvio_padrao = dados['Altura_m'].std()
print(f'\nDesvio Padrão: {desvio_padrao:.4f} m')

#COEFICIENTE DE VARIACAO
coeficiente_variacao = (desvio_padrao / media) * 100
print(f'Coeficiente de Variação: {coeficiente_variacao:.2f}%')

#QUARTIS
q1 = dados['Altura_m'].quantile(0.25)
q2 = dados['Altura_m'].quantile(0.50)
q3 = dados['Altura_m'].quantile(0.75)

print('\n' + '=' * 30)
print(f'\nQ1 (25%): {q1:.2f} m')
print(f'Q2 / Mediana (50%): {q2:.2f} m')
print(f'Q3 (75%): {q3:.2f} m')

#GRAFICOS
print('\n' + '=' * 30)
print('\nGerando e salvando gráficos na pasta "graficos/"...')

os.makedirs('graficos', exist_ok=True)

# GRAFICO 1 HISTOGRAMA DE FREQUÊNCIAS
plt.figure(figsize=(9, 5))
contagens, bins, barras = plt.hist(
    dados['Altura_m'],
    bins=limites,
    edgecolor='black',
    color='#4A90D9',
    alpha=0.85
)
plt.axvline(media, color='#D9534F', linestyle='--', linewidth=2, label=f'Média ({media:.4f} m)')
plt.axvline(mediana, color='#2E8B57', linestyle='-.', linewidth=2, label=f'Mediana ({mediana:.2f} m)')
plt.axvline(moda, color='#F0AD4E', linestyle=':', linewidth=2.2, label=f'Moda ({moda:.2f} m)')

for barra in barras:
    altura_barra = barra.get_height()
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        altura_barra + 0.35,
        f'{int(altura_barra)}',
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='none', alpha=0.85)
    )

plt.title('Histograma da Distribuição de Alturas', fontsize=13, fontweight='bold')
plt.xlabel('Altura (m)', fontsize=11)
plt.ylabel('Frequência Absoluta (fi)', fontsize=11)
plt.xticks(limites)
plt.ylim(0, max(contagens) + 2.5)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('graficos/histograma_alturas.png', dpi=300)
plt.show()

# GRAFICO 2 POLÍGONO DE FREQUÊNCIAS
plt.figure(figsize=(9, 5))
plt.plot(
    tabela_frequencia['xi'],
    tabela_frequencia['fi'],
    marker='o',
    color='#1F618D',
    linewidth=2.5,
    markersize=8,
    label='Frequência Absoluta'
)
for x_val, y_val in zip(tabela_frequencia['xi'], tabela_frequencia['fi']):
    plt.text(x_val, y_val + 0.4, f'{y_val}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.title('Polígono de Frequências das Alturas', fontsize=13, fontweight='bold')
plt.xlabel('Ponto Médio das Classes - xi (m)', fontsize=11)
plt.ylabel('Frequência Absoluta (fi)', fontsize=11)
plt.xticks(tabela_frequencia['xi'])
plt.ylim(0, tabela_frequencia['fi'].max() + 2.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig('graficos/poligono_frequencias.png', dpi=300)
plt.show()

# GRAFICO 3 BOXPLOT 
plt.figure(figsize=(8, 4.5))

plt.boxplot(
    dados['Altura_m'],
    orientation='horizontal',
    patch_artist=True,
    boxprops=dict(facecolor='#85C1E9', edgecolor='#1B4F72', linewidth=1.5),
    medianprops=dict(color='#C0392B', linewidth=2.5),
    whiskerprops=dict(color='#1B4F72', linewidth=1.5),
    capprops=dict(color='#1B4F72', linewidth=1.5),
    flierprops=dict(marker='o', markerfacecolor='#E74C3C', markersize=8, markeredgecolor='black')
)

elementos_legenda = [
    Patch(facecolor='#85C1E9', edgecolor='#1B4F72', linewidth=1.5, label=f'Intervalo Interquartil (Q1 = {q1:.2f} m a Q3 = {q3:.2f} m)'),
    Line2D([0], [0], color='#C0392B', linewidth=2.5, label=f'Mediana / Q2 ({mediana:.2f} m)'),
    Line2D([0], [0], color='#1B4F72', linewidth=1.5, label='Limites (mínimo e máximo sem outliers)'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='#E74C3C', markeredgecolor='black', markersize=8, label=f'Outlier / Valor discrepante ({valor_max:.2f} m)')
]

plt.legend(handles=elementos_legenda, loc='upper right', fontsize=9, frameon=True)
plt.title('Boxplot (Diagrama de Caixa) das Alturas', fontsize=13, fontweight='bold')
plt.xlabel('Altura (m)', fontsize=11)
plt.yticks([1], ['Altura_m'])
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('graficos/boxplot_alturas.png', dpi=300)
plt.show()


# GRAFICO 4 OGIVA DE FREQUÊNCIA RELATIVA ACUMULADA
plt.figure(figsize=(9, 5))
fac_perc_ogiva = [0.0] + list(tabela_frequencia['Fac (%)'])
plt.plot(
    limites,
    fac_perc_ogiva,
    marker='s',
    color='#28B463',
    linewidth=2.5,
    markersize=7,
    label='Frequência Relativa Acumulada (%)'
)
for x_val, y_val in zip(limites, fac_perc_ogiva):
    plt.text(x_val, y_val + 2.2, f'{y_val:.0f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.title('Ogiva de Frequência Relativa Acumulada (Fac %)', fontsize=13, fontweight='bold')
plt.xlabel('Limites das Classes de Altura (m)', fontsize=11)
plt.ylabel('Frequência Acumulada (%)', fontsize=11)
plt.xticks(limites)
plt.ylim(0, 110)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('graficos/ogiva_frequencia_acumulada.png', dpi=300)
plt.show()

# GRAFICO 5 DISPERSÃO POR PESSOA
plt.figure(figsize=(8, 4))
plt.scatter(range(1, n + 1), dados['Altura_m'], color='steelblue')
plt.axhline(q1, color='blue', linestyle='--', label=f'Q1 = {q1:.2f} m')
plt.axhline(q2, color='red', linestyle='-', label=f'Q2 (Mediana) = {q2:.2f} m')
plt.axhline(q3, color='green', linestyle='--', label=f'Q3 = {q3:.2f} m')
plt.title('Dispersão das Alturas por Pessoa e Quartis')
plt.xlabel('Pessoa (1 a 50)')
plt.ylabel('Altura (m)')
plt.legend()
plt.tight_layout()
plt.savefig('graficos/3_dispersao_quartis.png')
plt.show()
