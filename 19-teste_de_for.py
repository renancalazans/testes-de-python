#Escrever um algoritmo para exibir os múltiplos de 11,
#  a soma e a média dos múltiplos de 11, em ordem
#decrescente (inversa), compreendidos entre o intervalo: [200 100].
quantidade=0
soma=0
for n in range(200,100,-1):
    if ((n%11)==0):
        quantidade += 1
        soma = soma+n
        print(f'{quantidade}° número:{n}')
print(f'Entre o intervalo de [200,100] possui {quantidade} multiplos 11, de soma {soma} e média de {soma/quantidade}.')