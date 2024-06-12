#programa que peça o tamanho de um arquivo para download (em Megabytes) 
# e a velocidade de um link de Internet (em Megabytes / Segundo),
# calcule e informe o tempo: Minutos + Segundos aproximado de download do arquivo usando este link.

print('calcular o tempo de download de um arquivo')
try:
    tamanho=float(input('insira o tamanho do arquivo (em megabytes): '))
    velocidade=float(input('insira a velocidade da internet(em Megabytes / Segundo): '))
    t=tamanho/velocidade
    m=int(t//60)
    s=int(t%60)
    print(f'o tempo para efetuar o download do arquivo é de aproximadamente {m} minutos e {s} segundos.')
except Exception as erro:
    print(f'ERRO{erro}')