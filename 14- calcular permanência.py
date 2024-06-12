#algoritmo que leia o tempo (segundos) de permanência de um aluno no
#Laboratório de Programação: UVV e 
#exiba na tela seu tempo de permanência: Horas + Minutos + Segundos. 
# Exemplo: Tempo: 10000 Segundos = 2 Hora(s) + 46 Minuto(s) + 40 Segundo(s).

print('calcular tempo de permanencia')
try:
    s=int(input('insira o tempo de permanencia em segundos: '))
    if (s<=0):
        print('ERRO:tempo inválido.')
    else:
        h=(s//3600)
        m = (s % 3600) // 60
        s2 = s % 60
        print(f'o tempo de permanência é de {h} horas + {m} minutos + {s2} segundos.')
except Exception as erro:
    print(f"ERRO:{erro}")