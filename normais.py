from handle_normais import df_norm_clim_maio, df_norm_clim_abril
from read_csv import nomes_das_cidades_abril, nomes_das_cidades_maio, chuva_abril_por_cidade, chuva_maio_por_cidade

#---------------------------------------------  MAIO  -----------------------------------------------------

percentual_chuva_maio_1930 = []
percentual_chuva_maio_1961 = []
percentual_chuva_maio_1991 = []

cidades_percentual_chuva_maio_1930 = []
cidades_percentual_chuva_maio_1961 = []
cidades_percentual_chuva_maio_1991 = []

for row in df_norm_clim_maio.itertuples():
    if(row[5] in nomes_das_cidades_maio ): #SE EXISTIR PELO MENOS UMA NORMAL CLIMATOLOGICA DE PARA CIDADE

      #--------------------- NORMAL CLIMATOLÓGICA DE 1930-1961 ------------------------------------------
      if(row[2] == ''): #SEM NORMAL CLIMATOLOGICA PARA ESTA ÉPOCA
        print(f'({row[5]}) SEM NORMAL CLIMATOLOGICA PARA 1930-1960 ')
        
      else:
        percentual_1930 = chuva_maio_por_cidade[row[5]] / float(row[2]) #RAZÃO DE CHUVA DE MAIO COM A NORMAL DE 1930
        percentual_formatado_1930 = round(percentual_1930, 2)*100 #RAZÃO EM FORMA PERCENTUAL
        cidades_percentual_chuva_maio_1930.append(row[5]) #ADICIONANDO O ARRAY DE CIDADES
        percentual_chuva_maio_1930.append(percentual_formatado_1930) #ADICIONANDO O ARRAY DE PERCENTUAIS
        print(f'({row[5]}) PERCENTUAL ACIMA DA NORMAL (1930-1960): {percentual_formatado_1930:.2f}%')



      #--------------------- NORMAL CLIMATOLÓGICA DE 1961-1990 ------------------------------------------
      if(row[3] == ''): #SEM NORMAL CLIMATOLOGICA CLIMATOLÓGICA PARA ESTA ÉPOCA
         print(f'({row[5]}) SEM NORMAL CLIMATOLOGICA PARA 1961-1990')
      else:
        percentual_1961 = chuva_maio_por_cidade[row[5]] / float(row[3]) #RAZÃO DE CHUVA DE MAIO COM A NORMAL DE 1961
        percentual_formatado_1961= round(percentual_1961, 2)*100 #RAZÃO EM FORMA PERCENTUAL
        cidades_percentual_chuva_maio_1961.append(row[5]) #ADICIONANDO O ARRAY DE CIDADES
        percentual_chuva_maio_1961.append(percentual_formatado_1961) #ADICIONANDO O ARRAY DE PERCENTUAIS
        #print(f'({row[5]}) PERCENTUAL ACIMA DA NORMAL (1961-1990): {percentual_formatado_1961:.2f}%')



      #---------------------NORMAL CLIMATOLÓGICA DE 1991-2020 ------------------------------------------
      if(row[4] == ''): #SEM NORMAL CLIMATOLOGICA PARA ESTA ÉPOCA
         print(f'({row[5]}) SEM NORMAL CLIMATOLOGICA PARA 1991-2020')
      else:
        percentual_1991 = chuva_maio_por_cidade[row[5]] / float(row[4]) #RAZAO DE CHUVA DE MAIO COM A NORMAL DE 1991
        percentual_formatado_1991 = round(percentual_1991, 2)*100 #RAZÃO EM FORMA PERCENTUAL
        cidades_percentual_chuva_maio_1991.append(row[5]) #ADICIONANDO O ARRAY DE CIDADES
        percentual_chuva_maio_1991.append(percentual_formatado_1991) #ADICIONANDO O ARRAY DE PERCENTUAIS
        #print(f'({row[5]}) PERCENTUAL ACIMA DA NORMAL (1991-2020): {percentual_formatado_1991:.2f}%')
      print(  ) #QUEBRA DE LINHA

#print(percentual_chuva_maio_1930)
#print(percentual_chuva_maio_1961)
#print(percentual_chuva_maio_1991)

#---------------------------------------------  ABRIL  -----------------------------------------------------

percentual_chuva_abril_1930 = []
percentual_chuva_abril_1961 = []
percentual_chuva_abril_1991 = []

cidades_percentual_chuva_abril_1930 = []
cidades_percentual_chuva_abril_1961 = []
cidades_percentual_chuva_abril_1991 = []

for row in df_norm_clim_abril.itertuples():
    if(row[5] in nomes_das_cidades_abril ):  #SE EXISTIR PELO MENOS UMA NORMAL CLIMATOLOGICA DE PARA CIDADE

      #--------------------- NORMAL CLIMATOLÓGICA DE 1930-1961 ------------------------------------------
      if(row[2] == ''): #SEM NORMAL CLIMATOLOGICA CLIMATOLÓGICA PARA ESTA ÉPOCA
        print(f'({row[5]}) SEM NORMAL CLIMATOLOGICA PARA 1930-1960')
      else:
        percentual_1930_abril = chuva_abril_por_cidade[row[5]] / float(row[2]) #RAZÃO DE CHUVA DE MAIO COM A NORMAL DE 1930
        percentual_formatado_1930_abril = round(percentual_1930_abril, 2)*100 #RAZÃO EM FORMA PERCENTUAL
        cidades_percentual_chuva_abril_1930.append(row[5]) #ADICIONANDO O ARRAY DE CIDADES
        percentual_chuva_abril_1930.append(percentual_formatado_1930_abril) #ADICIONANDO O ARRAY DE PERCENTUAIS
        #print(f'({row[5]}) PERCENTUAL ACIMA DA NORMAL (1930-1960): {percentual_formatado_1930:.2f}%')



      #--------------------- NORMAL CLIMATOLÓGICA DE 1961-1990 ------------------------------------------
      if(row[3] == ''): #SEM NORMAL CLIMATOLOGICA PARA ESTA ÉPOCA
         print(f'({row[5]}) SEM NORMAL CLIMATOLOGICA PARA 1961-1990')
      else:
        percentual_1961_abril = chuva_abril_por_cidade[row[5]] / float(row[3]) #RAZÃO DE CHUVA DE MAIO COM A NORMAL DE 1961
        percentual_formatado_1961_abril = round(percentual_1961_abril, 2)*100 #RAZÃO EM FORMA PERCENTUAL
        cidades_percentual_chuva_abril_1961.append(row[5]) #ADICIONANDO O ARRAY DE CIDADES
        percentual_chuva_abril_1961.append(percentual_formatado_1961_abril) #ADICIONANDO O ARRAY DE PERCENTUAIS
        #print(f'({row[5]}) PERCENTUAL ACIMA DA NORMAL (1961-1990): {percentual_formatado_1961:.2f}%')



      #---------------------NORMAL CLIMATOLÓGICA DE 1991-2020 ------------------------------------------
      if(row[4] == ''):#SEM NORMAL CLIMATOLOGICA PARA ESTA ÉPOCA
         print(f'({row[5]}) SEM NORMAL CLIMATOLOGICA PARA 1991-2020')
      else:
        percentual_1991_abril = chuva_abril_por_cidade[row[5]] / float(row[4]) #RAZAO DE CHUVA DE MAIO COM A NORMAL DE 1991
        percentual_formatado_1991_abril = round(percentual_1991_abril, 2)*100 #RAZÃO EM FORMA PERCENTUAL
        cidades_percentual_chuva_abril_1991.append(row[5]) #ADICIONANDO O ARRAY DE CIDADES
        percentual_chuva_abril_1991.append(percentual_formatado_1991_abril) #ADICIONANDO O ARRAY DE PERCENTUAIS
        #print(f'({row[5]}) PERCENTUAL ACIMA DA NORMAL (1991-2020): {percentual_formatado_1991:.2f}%')
      print(  ) #QUEBRA DE LINHA


print(nomes_das_cidades_abril)
print(nomes_das_cidades_maio)