import pandas as pd
from haversine import haversine

# Ler o arquivo CSV
base_de_dados= pd.read_csv('./database.csv')
base_de_dados = base_de_dados[base_de_dados['CD_ESTACAO'].str.startswith('A')] #RETIRANDO AS ESTAÇÕES DO SIMAGRO
limiar = 100 # km
vizinhos = {}
estacoes = base_de_dados.drop_duplicates(subset='CD_ESTACAO', keep='first')

# Iterar sobre todas as combinações de estações
for i, row1 in estacoes.iterrows():
    cd_estacao1 = row1['CD_ESTACAO']
    nome1 = row1['DC_NOME']
    lat1 = row1['VL_LATITUDE']
    lon1 = row1['VL_LONGITUDE']
    vizinhos[cd_estacao1] = []



    for j, row2 in estacoes.iterrows():
        if i != j:
            cd_estacao2 = row2['CD_ESTACAO']
            nome2 = row2['DC_NOME']
            lat2 = row2['VL_LATITUDE']
            lon2 = row2['VL_LONGITUDE']
            distancia = haversine(float(lat1), float(lon1), float(lat2), float(lon2))
            

            if distancia < limiar:
                vizinhos[cd_estacao1].append(cd_estacao2)

# Exibir o dicionário de vizinhos
"""for estacao, vizinhas in vizinhos.items():
    print(f"{estacao}: {vizinhas}")"""



