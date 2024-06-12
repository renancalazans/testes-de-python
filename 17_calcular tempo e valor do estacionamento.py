from datetime import datetime

try:
    # Entrada de dados
    hora_entrada = input("Digite a hora de entrada (HH:MM): ")
    hora_saida = input("Digite a hora de saída (HH:MM): ")
    valor_por_30_minutos = float(input("Digite o valor a ser pago a cada 30 minutos (R$): "))

    # Conversão das horas de entrada e saída para datetime
    formato_hora = "%H:%M"
    entrada = datetime.strptime(hora_entrada, formato_hora)
    saida = datetime.strptime(hora_saida, formato_hora)

    # Cálculo do tempo de permanência em minutos
    tempo_permanencia = (saida - entrada).total_seconds() / 60
    if tempo_permanencia < 0:
        tempo_permanencia += 24 * 60  # Ajuste para permanência que ultrapassa a meia-noite

    # Aplicar a carência de 30 minutos
    tempo_permanencia -= 30

    # Se a permanência for negativa após a carência, considerar como zero
    if tempo_permanencia < 0:
        tempo_permanencia = 0

    # Calcular o valor a pagar
    # Cada 30 minutos é cobrado
    valor_a_pagar = (tempo_permanencia // 30) * valor_por_30_minutos

    # Saída
    print(f"Total a pagar: R$ {valor_a_pagar:.2f}")

except ValueError as ve:
    print(f"ERRO: {ve}")
except Exception as erro:
    print(f"ERRO: {erro}")