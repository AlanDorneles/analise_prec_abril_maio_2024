from vizinhos import base_de_dados
from preenchimento import base_de_dados_filtered
import matplotlib.pyplot as plt

quantidade_de_nulos = {}
quantidade_de_nulos_filtered = {}
estacoes = base_de_dados['CD_ESTACAO'].unique()
estacoes_preenchidas = base_de_dados_filtered['CD_ESTACAO'].unique()
#print(estacoes)

for estacao in estacoes:
    tabela_estacao = base_de_dados.query(f"CD_ESTACAO == '{estacao}'")
    nulos_por_estacao = tabela_estacao['CHUVA'].isnull().sum()
    quantidade_de_nulos[estacao] = nulos_por_estacao

for estacao, nulos in quantidade_de_nulos.items():
    print(f'{estacao}:{nulos}') 

for estacao in estacoes_preenchidas:
    tabela_estacao_filtered = base_de_dados_filtered.query(f"CD_ESTACAO == '{estacao}'")
    nulos_por_estacao_filtered = tabela_estacao_filtered['CHUVA'].isnull().sum()
    quantidade_de_nulos_filtered[estacao] = nulos_por_estacao_filtered

for estacao_filtered, nulos_filtered in quantidade_de_nulos_filtered.items():
    print(f'{estacao_filtered}:{nulos_filtered}') 


quantidade_de_nulos.values()
plt.boxplot(quantidade_de_nulos.values())
plt.xlabel('Base de dados inmet')
plt.ylabel('Quantidade de falhas')
plt.show()

plt.boxplot(quantidade_de_nulos_filtered.values())
plt.xlabel('Base de dados inmet com preenchimento')
plt.ylabel('Quantidade de falhas')
plt.show()


