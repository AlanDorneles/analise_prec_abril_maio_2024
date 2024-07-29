from vizinhos import base_de_dados
import matplotlib.pyplot as plt
import pandas as pd

dias = base_de_dados['DT_MEDICAO'].unique()
stations = base_de_dados['CD_ESTACAO'].unique()

grouped_data = base_de_dados.groupby(['DT_MEDICAO', 'CD_ESTACAO'])['CHUVA'].sum().reset_index()
grouped_data = grouped_data.query( f'DT_MEDICAO >= "2024-04-26" & DT_MEDICAO <= "2024-05-14"')


plt.figure(figsize=(10, 6))
for estacao in stations:
    data_estacao = grouped_data[grouped_data['CD_ESTACAO'] == estacao]
    plt.plot(data_estacao['DT_MEDICAO'], data_estacao['CHUVA'], label=f'Estação {estacao}')

plt.xlabel('Dia/Mês')
plt.ylabel('Precipitação diária')
plt.title('Precipitação em Abril e Maio de 2024')
plt.grid(True)


plt.show()



    


