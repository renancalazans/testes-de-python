#Calcular e exibir a área e o comprimento de um círculo.
#sabendo que, Área = π * R²
#Comprimento = 2 * π * R.

import math
print('calculadora de área e comprimento de um circulo:')
try:
    r=float(input('insira o raio do circulo: '))
    print(f'a área do circulo é de {math.pi*(r**2):.2f}')
    print(f'o comprimento do circulo é de:{math.pi*2*r}')
except Exception as erro:
    print(f'ERRO:{erro}')