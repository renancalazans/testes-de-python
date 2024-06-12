#Faça um algoritmo que leia um número positivo 
# exiba se seu quadrado é ímpar e múltiplo de 11.

print('verificar se um número positivo possui seu quadrado impar e é multiplo de 11')
try:
    n=float(input('insira um número positivo: '))
    if n <=0:
        print('ERRO:número invalido, insira um número positivo.')
    else:
        if ((n**n)%2!=0) and (n%11==0):
            print(f'{n} possui seu quadrado impar e é multiplo de 11')
        elif ((n**n)%2==0) and (n%11==0):
            print(f'{n} não possui seu quadrado impar mas é multiplo de 11')
        elif ((n**n)%2!=0) and (n%11!=0):
            print(f'{n} possui seu quadrado impar mas não é multiplo de 11')
        else:
            print(f'{n} não possui seu quadrado impar e não é multiplo de 11')
except Exception as erro:
    print(f"ERRO:{erro}")