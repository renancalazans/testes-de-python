#Calcular e exibir o IMC (Índice de Massa Corpórea) 
#sabendo que IMC = M / H²
print('calculadora de IMC')
try:
    m=float(input('insira sua massa: '))
    h=float(input('insira sua altura: '))
    print(f'O IMC calculado é de {m/(h*h):.2f}')
except Exception as erro:
    print(f'ERRO: {erro}')