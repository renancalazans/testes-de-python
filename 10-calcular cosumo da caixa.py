#Calcular e exibir o tempo (em horas) de autonomia de uma caixa d’água 
# que consome 1350 litros por hora em média. 
#O tanque do restaurante é cilíndrico 
# base circular de Raio(R) e de altura (H) em metros. 
# Sabendo que 1 m³ = 1000 Litros.

import math
print('calcular o tempo de autonomia de uma caixa d´água(consome 1350 litros por hora)')
try:
    r=float(input('insira o raio da caixa d´água(em metros): '))
    h=float(input('insira a altura da caixa d´água(em metros): '))
    v=math.pi*(r**2)*h
    l= v*1000
    t= l/1350
    print(f'o tempo de autonomia fa caixa com volume de {v:.2f}m³ é de {t:.2f}litos/hora.')
except Exception as erro:
    print(f"ERRO:{erro}")