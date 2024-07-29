import pandas as pd
import csv

# LENDO O CSV COM AS NORMAIS CLIMATOLÓGICAS
def read_csv(csv_file_path):
    normais_climatologicas = []
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')  # Use ';' como delimitador
        for row in csv_reader:
            normais_climatologicas.append(row)
    #print(normais_climatologicas)
    return normais_climatologicas


csv_file_path = 'NORM-CLIM-ESTACOES.csv'  # CAMINHO DO CSV
normais_climatologicas = read_csv(csv_file_path)

# Convertendo a lista para DataFrame
df_normais_climatologicas = pd.DataFrame(normais_climatologicas)

# Nome dos meses com a primeira letra maiúscula
months = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

months_lc = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

# Filtrando os dados por mês e criando DataFrames dinâmicos
for month in months_lc:
    exec(f'df_norm_clim_{month} = df_normais_climatologicas[df_normais_climatologicas.iloc[:, 0] == "{month.capitalize()}"]')


print(df_norm_clim_abril)
print(df_norm_clim_maio)