import pandas as pd
from vizinhos import base_de_dados
from estacoes_sem_falhas import estacoes_sem_falhas
from haversine import haversine

base_de_dados['HR_MEDICAO'] = base_de_dados['HR_MEDICAO'].astype(str)
base_de_dados['CD_ESTACAO'] = base_de_dados['CD_ESTACAO'].astype(str)
base_de_dados['DT_MEDICAO'] = base_de_dados['DT_MEDICAO'].astype(str)


base_de_dados_filtered =  base_de_dados[base_de_dados['CHUVA'].isna()]
estacoes_com_proximas = {k: v for k, v in estacoes_sem_falhas.items() if v}
keys = estacoes_com_proximas.keys()
base_de_dados_filtered =  base_de_dados_filtered[base_de_dados_filtered['CD_ESTACAO'].isin(keys)]

print(base_de_dados_filtered['CHUVA'].isnull().sum())

for index, row in base_de_dados_filtered.iterrows(): #ITERANDO SOBRE A BASE DE DADOS
         if pd.isnull(row['CHUVA']): #GARANTINDO QUE O VALOR É NULL
            variaveis = [[], []] #SOMATÓRIO 1 E 2
            estacoes_proximas = estacoes_sem_falhas.get(row['CD_ESTACAO'], []) #VERIFICANDO SE HÁ VIZINHOS
            
            for estacao_proxima in estacoes_proximas: #ITERANDO SOBRE OS VIZINHOS
                    filtro_query = f"CD_ESTACAO == '{estacao_proxima}' & DT_MEDICAO == '{row['DT_MEDICAO']}' & HR_MEDICAO == '{row['HR_MEDICAO']}'" #FILTRO DA DATA E HORA DAS ESTAÇÕES VIZINHAS

                    item = base_de_dados.query(filtro_query) #OBTENDO A LINHA DA OCORRENCIA NA ESTAÇÃO VIZINHA
                    for idx, row_item in item.iterrows(): 
                                                
                        distancia_entre_estacao = haversine(float(row['VL_LATITUDE']), float(row['VL_LONGITUDE']), float(row_item['VL_LATITUDE']), float(row_item['VL_LONGITUDE'])) 
                        prec_vizinha = float(row_item['CHUVA']) # Garantir que o valor é float
                        sum1 = prec_vizinha / distancia_entre_estacao 
                        sum2 = 1 / distancia_entre_estacao
                        variaveis[0].append(sum1) 
                        variaveis[1].append(sum2)

                        print(f'Estação alvo:\n {row["DC_NOME"]}\n CHUVA: {row["CHUVA"]}\n DIA E HORA: {row["DT_MEDICAO"]} {row["HR_MEDICAO"]}\n ESTAÇÃO VIZINHA:\n CHUVA: {row_item["CHUVA"]}\n NOME: {row_item["DC_NOME"]}\n DATA E HORA: {row_item["DT_MEDICAO"]} {row_item["HR_MEDICAO"]}')


            #APLICANDO A INTERPOLAÇÃO DO INVERSO DA DISTANCIA
            if variaveis[0] and variaveis[1]:  # Certificar-se de que as listas não estão vazias
                result = sum(variaveis[0]) / sum(variaveis[1]) # (Di/d) / (1/d) 
                base_de_dados.at[index, 'CHUVA'] = result
                print(result)