#Escrever um algoritmo em Python que leia a Massa (Quilos) e a Altura (Metros) do indivíduo
#calculando o IMC = Massa / Altura2
#. Após isso, classifique-o conforme a tabela:

#IMC        CLASSIFICAÇÃO
#<18.5      Magreza
#[18.5, 25[ Saudável
#[25, 30[   Sobrepeso
#[30, 35[   Obesidade Grau I
#[35, 40[   Obesidade Grau II (Severa)
#>=         40 Obesidade Grau III (Mórbida)

print('calculadora de IMC')
try:
    m=float(input('insira a massa(em kg): '))
    h=float(input('insira a altura(em metros): '))
    if(m<=0 or h<=0):
        print('ERRO:Dado inválido inserido')
    else:
        imc=m/(h**2)
        if(imc<18.5):
            x='magreza'
        elif(18.5>=imc<25):
            x='saudável'
        elif(25>=imc<30):
            x='sobrepeso'
        elif(30>=imc<35):
            x='obesidade garu I'
        elif(35>=imc<40):
            x='obesidade grau II(severa)'
        else:
            x='Obesidade Grau III(mórbida)'
    print(f'O IMC calculado é de {imc:.2f} classificado em {x}')
except Exception as erro:
    print(f"ERRO: {erro}")