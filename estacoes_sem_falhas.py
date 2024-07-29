from vizinhos import vizinhos, base_de_dados

estacoes_sem_falhas = {}
for estacao, vizinhas in vizinhos.items():
  estacoes_sem_falhas[estacao] = []
  for i in vizinhas:
    query_estac = f'CD_ESTACAO == "{i}"'
    if not base_de_dados.query(query_estac)['CHUVA'].isnull().any():
      estacoes_sem_falhas[estacao].append(i)
    else:
      continue

for estacao, falhas in estacoes_sem_falhas.items():
    #print(f"{estacao}: {falhas}")
    continue
