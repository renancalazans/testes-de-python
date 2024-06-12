#Tendo como dado de entrada a altura (h) e o sexo de uma pessoa,
# algoritmo que calcule
#seu peso (Massa: Quilogramas) ideal, utilizando as seguintes fórmulas:
#✓ Para homens: (72.7 ∗ h) − 58
#✓ Para mulheres: (62.1 ∗ h) − 44.7

print('exibir peso(em kg) médio para a sua altura e genero')
try:
    h=float(input('insira a sua altura(em metros): '))
    if (h<=0):
        print('ERRO:insira uma altura válida')
    else:
        genero=(input('insira o seu sexo M para masculino e F para feminino: '))
        if (genero ==( 'M' or 'm')):
            print(f'O peso médio para pessoas da sua altura é de {(72.7*h)-58:.2f}kg')
        elif (genero ==( 'F' or 'f')):
            print(f'O peso médio para pessoas da sua altura é de {(62.1*h)-44.7:.2f}kg')
        else:
            print("ERRO: Sexo inválido. Por favor, digite 'M' para masculino ou 'F' para feminino.")
except Exception as erro:
    print(f"ERRO:{erro}")