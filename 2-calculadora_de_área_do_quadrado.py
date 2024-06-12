print("calculadora de área do quadrado")
try:
    l=float(input('insira o lado do quadrado: '))
    print(f'o valor da área do qaudrado de lado {l} é de {l*l:.2f}')
except:
    print('erro na entrada de dados')