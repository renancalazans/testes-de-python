print('Calculadora da área do retângulo')
try:
    b=float(input('insira a base do retângulo: '))
    h=float(input('insira a altura do retângulo: '))
    print(f'A área do retângulo é de {b*h:.2f}')
except Exception as erro:
  print(f'ERRO:{erro}')