lda = list()
aluno = list()

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    aluno.append(nome)
    aluno.append(n1)
    aluno.append(n2)
    lda.append(aluno[:])
    print(aluno)
    aluno.clear()

    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        break

for i in range(0, len(lda)):
    print(f'Aluno{i}:')
    for a in range(0, 3):
        if a == 0:
            print(f'Nome:{lda[i][a]}', end= ' ')
            N1 = 0
            N2 = 0
        elif a == 1:
            N1 = lda[i][a]
        elif a == 2:
            N2 = lda[i][a]
    print(f'Media: {(N1 + N2) / 2}')

while True:
    ali = int(input('Ver a nota de um aluno ou sair(999): '))
    if ali == 999:
        break
    else:
        if ali < len(lda):
            print(f'Nota de {lda[ali][0]}: é {lda[ali][1]},{lda[ali][2]}')
        else:
            print('Erro tente novamente: ')


