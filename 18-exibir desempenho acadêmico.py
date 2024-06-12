#algoritmo que leia as notas entre [0, 10]: AV1, AV2 e PF e faltas: TF de um (1) aluno.
#exiba na tela seus Resultados: Parciais e Final (STATUS: Aprovado, Prova Final, Reprovado por Falta ou Reprovado).

print('exibir resultado semestral de um aluno')
try:
    av1=float(input('insira a nota do primeiro bimestre: '))
    av2=float(input('insira a nota do segundo bimestre: '))
    tf=int(input('insira o total de faltas: '))
    if (10<av1 or av1<0 or 10<av2 or av2<0 or tf<0):
        print('erro na entrada de dados')
    elif (tf>10):
        print('repprovação por falta')
    else:
        mf=(av1+av2)/2
        if(mf<4):
            print(f'A média de {mf:.2f} é insuficiente para a recuperação: reprovação')
        elif(mf>=7):
            print(f'Alcançou a média de {mf:.2f} pontos:aprovação')
        else:
            print(f'média final de {mf:.2f} pontos:recuperação')
            pf=float(input('insira a nota final: '))
            tf=(pf+mf)/2
            if (0<pf>10):
                print('ERRO: nota de prova final inválida')
            elif (tf<5):
                print(f'A média final de {tf:.2f} é insuficiente para a aprovação: reprovação')
            else:
                print(f'A média final de {tf:.2f} é suficiente para a aprovação: aprovação')
except Exception as erro:
    print(f'ERRO: {erro}')