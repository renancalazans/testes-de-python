print('calculadora da hipotenusa')
try:
    cateto1= float(input('insira o valor do cateto 1: '))
    cateto2= float(input('insira o valor do cateto 2: '))
    h= (cateto1**2 + cateto2**2)**0.5
    print(f'o valor da hipotenusa é de {h:.2f}')
except:
    print('ERRO NA ENTRADA DE DADOS')