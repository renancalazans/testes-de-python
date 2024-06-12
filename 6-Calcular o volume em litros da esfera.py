#Calcular e exibir o volume em litros de uma esfera 
# #Raio (R), sabendo que o usuário deve informar
#Sabe-se que: VolumeEsfera = 4/3 * π * R³
# 1 Litro é igual a 10-³ m3.

import math
print('Calculadora do volume da esfera(resultado em litros)')
try:
    r=float(input('insira o raio da esfera:'))
    v= (4/3)*math.pi*r**3
    l= v/(10**-3)
    print(f'O volume da esfera é igual a {l:.2f}l')
except Exception as erro:
    print(f'ERRO: {erro}')
    