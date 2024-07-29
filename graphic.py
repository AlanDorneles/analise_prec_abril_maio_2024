import matplotlib.pyplot as plt
from normais import cidades_percentual_chuva_abril_1930,cidades_percentual_chuva_abril_1961,cidades_percentual_chuva_abril_1991,cidades_percentual_chuva_maio_1930,cidades_percentual_chuva_maio_1961,cidades_percentual_chuva_maio_1991,percentual_chuva_abril_1930,percentual_chuva_abril_1961,percentual_chuva_abril_1991,percentual_chuva_maio_1930,percentual_chuva_maio_1961,percentual_chuva_maio_1991

print(percentual_chuva_maio_1991)
print(cidades_percentual_chuva_maio_1991)


#---------------------------------------------  MAIO  -----------------------------------------------------
#GRAFICO DE BARRAS VERTICAIS DO QUANTO CHOVEU EM RELAÇÃO A NORMAL CLIMATOLÓGICA DE MAIO DE 1991-2020

plt.barh(cidades_percentual_chuva_maio_1991, percentual_chuva_maio_1991)
plt.xlabel('Percentuais acima da normal de Maio (%)')
plt.ylabel('Cidades')
plt.title('Percentual acima da normal climatológica (1991-2020)')
for index, value in enumerate(percentual_chuva_maio_1991):
    plt.text(value, index, f'{value}%', va='center')
plt.show()


#GRAFICO DE BARRAS VERTICAIS DO QUANTO CHOVEU EM RELAÇÃO A NORMAL CLIMATOLÓGICA DE MAIO DE 1961-2020
plt.barh(cidades_percentual_chuva_maio_1961, percentual_chuva_maio_1961)
plt.xlabel('Percentuais acima da normal de Maio(%)')
plt.ylabel('Cidades')
plt.title('Percentual acima da normal climatológica (1961-1990)')
for index, value in enumerate(percentual_chuva_maio_1961):
    plt.text(value, index, f'{value}%', va='center')
plt.show()
print(len(percentual_chuva_maio_1961))

#GRAFICO DE BARRAS VERTICAIS DO QUANTO CHOVEU EM RELAÇÃO A NORMAL CLIMATOLÓGICA DE MAIO DE 1931-1960
plt.barh(cidades_percentual_chuva_maio_1930, percentual_chuva_maio_1930)
plt.xlabel('Percentuais acima da normal de Maio (%)')
plt.ylabel('Cidades')
plt.title('Percentual acima da normal climatológica (1930-1961)')
for index, value in enumerate(percentual_chuva_maio_1930):
    plt.text(value, index, f'{value}%', va='center')
plt.show()

#---------------------------------------------  ABRIL  -----------------------------------------------------
#QUANTO CHOVEU EM RELAÇÃO A NORMAL CLIMATOLÓGICA DE ABRIL DE 1991-2020
plt.barh(cidades_percentual_chuva_abril_1991, percentual_chuva_abril_1991,color='gray')
plt.xlabel('Percentuais acima da normal de Abril (%)')
plt.ylabel('Cidades')
plt.title('Percentual acima da normal climatológica (1991-2020)')
for index, value in enumerate(percentual_chuva_abril_1991):
    plt.text(value, index, f'{value}%', va='center')
plt.show()


#QUANTO CHOVEU EM RELAÇÃO A NORMAL CLIMATOLÓGICA DE ABRIL DE 1961-1990
plt.barh(cidades_percentual_chuva_abril_1961, percentual_chuva_abril_1961,color='gray')
plt.xlabel('Percentuais acima da normal de Abril (%)')
plt.ylabel('Cidades')
plt.title('Percentual acima da normal climatológica (1961-1990)')
for index, value in enumerate(percentual_chuva_abril_1961):
    plt.text(value, index, f'{value}%', va='center')
plt.show()

#QUANTO CHOVEU EM RELAÇÃO A NORMAL CLIMATOLÓGICA DE ABRIL DE 1931-1960
plt.barh(cidades_percentual_chuva_abril_1930, percentual_chuva_abril_1930,color='gray')
plt.xlabel('Percentuais acima da normal de Abril (%)')
plt.ylabel('Cidades')
plt.title('Percentual acima da normal climatológica (1930-1961)')
for index, value in enumerate(percentual_chuva_abril_1930):
    plt.text(value, index, f'{value}%', va='center')
plt.show()