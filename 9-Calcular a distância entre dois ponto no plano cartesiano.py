#Calcular e exibir a distância entre dois pontos quaisquer do plano,
#P(x1, y1) e Q(x2, y2), 
#sabendo que a fórmula da distância é d = √((x2 – x1)² + (y2 – y1)²),
#sendo os pontos P(x1, y1) e Q(x2, y2) como dados de entrada.

print('calculadora da distânci de dois pontos no plano cartesiano')
try:
    x1=float(input('insira o x do ponto 1: '))
    y1=float(input('insira o y do ponto 1: '))
    x2=float(input('insira o x do ponto 2: '))
    y2=float(input('insira o y do ponto 2: '))
    d=(((x2-x1)**2)+((y2-y1)**2))**0.5
    print(f'A ditância do ponto 1({x1},{y1}) ao ponto 2({x2},{y2}) é de {d:.2f}')
except Exception as erro:
    print(f'ERRO{erro}')