#Escreva um algoritmo que leia de 10.000 habitantes de uma pequena cidade 
# se está empregado ou não, e exiba em porcentagem a quantidade de empregados e desempregados 


quantidade=0

empregados=0
desempregados = 0
habitantes=int(input('insira a quantidade de habitantes da cidade: '))
print('selecione e(empregado) e d(desempregado)')
while quantidade < habitantes: a=int(input('digite 1 se está empregado e 0 se está desempregado: '))
if a == 1:
            quantidade +=1
            empregados +=1
elif a == 0:
            quantidade +=1
            desempregados +=1
else:
          print('ERRO: dado inserido inválido, insira 0 ou 1')

print(f'na cidade que possui {habitantes} habitantes possui um total de {empregados*100/habitantes:.2f}% empregados e {desempregados*100/habitantes:.2f}% desempregados')