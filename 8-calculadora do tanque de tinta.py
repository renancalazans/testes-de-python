#Calcular e exibir a quantidade de tinta (em latas) 
#custo (em reais) para pintar um tanque cilíndrico
#base circular de Raio (R) e altura (H) em metros, sabendo que:
# 1 lata = 5 litros.
# 1 litro pinta 3 metros quadrados.
# 1 lata custa 50 Reais.

import math
print('Calcular a quantidade de tinta e custo para intar um tanque cilíndrico')
try:
    r=float(input('Insira o raio do tanque cilìndrico(em metros): '))
    h=float(input('Insira a altura do tanque cilìndrico(em metros): '))
    v=2*math.pi*r*(r+h)
    litro= v/3
    lata=int(litro/5)
    valor=lata*50
    print(f'o tanque cilìndrico possui {v:.2f}m³, portanto precisará de {lata} latas de tinta, que custará o total de R${valor:.2F}')
except Exception as erro:
    print(f"ERRO:{erro}")