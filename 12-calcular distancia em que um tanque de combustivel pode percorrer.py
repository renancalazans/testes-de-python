#Calcular e exibir a distância máxima (em Quilômetros) de autonomia de um carro que possui
#tanque de combustível cúbico de lado (L) em metros e Altura (h) de preenchimento do tanque.
#Sabendo que seu consumo é em média 10 km/litro. Sabendo que 1 m3 = 1000 Litros.

print('calcular a distancia (em km) de autonomia de um carro(seu consumo é em média 10 km/litro)')
try:
    l=float(input('considerando um tanque cubico, insira o lado(em metros): '))
    h=float(input('insira a altura do tanque(em metros): '))
    v= (l**2)*h
    litro=v*1000
    d=litro*10
    print(f'O tanque de {v:.3f}m³, com a capacidade de {litro:.2f} litros percorre até {d:.2f}km.')
except Exception as erro:
    print(f"ERRO:{erro}")