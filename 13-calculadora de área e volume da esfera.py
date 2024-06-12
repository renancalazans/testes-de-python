#Escrever um algoritmo em Python que determine o volume e a área
#uma esfera de raio r (PERTENCE AOS REAIS POSITIVOS SEM O ZERO).
#Sendo que π = 3.14.
#Area = 4 ∗ π ∗ r²
#Volume =4/3∗ π ∗ r³

print('calculadora da área e volume de uma esfera.')
try:
    r=float(input('insira o raio da esfera'))
    if(r<=0):
        print('ERRO:insira um valor positivo')
    else:
        a=4*3.14*r*r
        v=(4/3)*3.14*(r**3)
        print(f'A esfera possui {a:.2f} de área e {v:.2f} de volume.')
except Exception as erro:
    print(f"ERRO:{erro}")