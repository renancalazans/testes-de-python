# pergunte quanto você ganha por hora e o número de horas trabalhadas no mês
# Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato. 
# Com isso, exiba na tela:✓ salário bruto.✓ quanto pagou ao INSS.
# #✓ quanto pagou ao sindicato.✓ o salário líquido = Brutos - Descontos.

try:
    hora=float(input('insira quanto você recebe por hora: '))
    mes=float(input('insira quantas horas trabalhadas no mês '))
    bruto=hora*mes
    inss=bruto*0.08
    sindicato=bruto*0.05
    imposto =bruto*0.11
    print(f'Salário bruto: R${bruto:.2f}')
    print(f'INSS: R${inss:.2f}')
    print(f'Pagou ao sindicato: R${sindicato:.2f}')
    print(f'Pagou ao imposto de renda: R${imposto:.2f}')
    print(f'Salário líquido: R${bruto-(inss+sindicato+imposto):.2f}')
except Exception as erro:
    print(f'ERRO:{erro}')