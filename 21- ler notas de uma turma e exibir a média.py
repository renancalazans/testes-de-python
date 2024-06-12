#Ler a nota[0, 10] de 50 alunos (CONDIÇÃO: VALOR FINAL) de uma turma
#e exibir sua a média geral.
#Média = Soma as Notas de todos / Alunos

print('Calcular média de notas de uma turma')
soma=0
alunos=int(input('insira o número de alunos da turma.'))
nota=0
while nota<alunos:
    try:
        ponto=float(input('insira a nota do aluno:'))
        if 10>=ponto>=0:
           nota+=1
           soma+=ponto
        else:
           print('insira uma nota válida, de 0 a 10')
    except Exception as erro:
        print(f'ERRO:{erro}')
print(f' a turma de {alunos} alunos possui uma média de {soma/alunos:.2f} pontos')