from preenchimento import base_de_dados
import pandas as pd
import csv

base_de_dados['CHUVA'] = base_de_dados['CHUVA'].astype(float) # Convertendo a coluna "CHUVA" para float
base_de_dados['DT_MEDICAO'] = pd.to_datetime(base_de_dados['DT_MEDICAO']) #Convertendo a coluna "DT_MEDICAO" para datetime

#DIVIDINDO POR MÊS (ABRIL E MAIO)
base_de_dados_maio = base_de_dados[(base_de_dados['DT_MEDICAO'] >= '2024-05-01') & (base_de_dados['DT_MEDICAO'] <= '2024-05-31')]
base_de_dados_abril = base_de_dados[(base_de_dados['DT_MEDICAO'] >= '2024-04-01') & (base_de_dados['DT_MEDICAO'] <= '2024-04-30')]


chuva_maio_por_cidade = base_de_dados_maio.groupby('DC_NOME')['CHUVA'].sum()
chuva_abril_por_cidade = base_de_dados_abril.groupby('DC_NOME')['CHUVA'].sum()
nomes_das_cidades_maio = chuva_maio_por_cidade.index.tolist()
nomes_das_cidades_abril = chuva_abril_por_cidade.index.tolist()

print(nomes_das_cidades_abril)




#LENDO O CSV COM AS NORMAIS CLIMATOLÓGICAS
def read_csv(csv_file_path):
    normais_climatologicas = []
    with open(csv_file_path, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')  # Use ';' como delimitador
        for row in csv_reader:
            #print(row)
            cidade = row[4]  # A quarta coluna (índice 3) é a coluna "CIDADE"
            normais_climatologicas.append(row)

    return normais_climatologicas

csv_file_path = 'NORM-CLIM-ESTACOES.csv' #CAMINHO DO CSV
normais_climatologicas = read_csv(csv_file_path)
df_normais_climatologicas = pd.DataFrame(normais_climatologicas)

# Agora você pode usar o DataFrame "df" para análise e manipulação dos dados
df_norm_clim_maio = df_normais_climatologicas[df_normais_climatologicas.iloc[:, 0] == 'Maio'] #NORMAIS DE MAIO
df_norm_clim_abril = df_normais_climatologicas[df_normais_climatologicas.iloc[:, 0] == 'Abril'] #NORMAIS DE ABRIL
print(df_norm_clim_maio)