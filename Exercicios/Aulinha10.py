cdur = cddr = cdvr = cdcr = 0

while True:
    das = int(input('Digite o valor que deseja ser sacado'))
    certo = str(input(f'O valor a ser sacado é {das:.2f}? [S/N] ')).upper().strip()
    print(certo)
    if certo == 'S':
        while das > 0:
            if das >= 50:
                das -= 50
                cdcr += 1
            elif das >= 20:
                das -= 20
                cdvr += 1
            elif das >= 10:
                das -= 10
                cddr += 1
            elif das >= 1:
                das -= 1
                cdur += 1

    print(f'Você recebe {cdcr} cedulas de 50 reais\n'
            f'Você recebe {cdvr} cedulas de 20 reais\n'
            f'Você recebe {cddr} cedulas de 10 reais\n'
            f'Você recebe {cdur} cedulas de 1 reais\n')

    continuar = input('Deseja continuar? [S/N]').upper().strip()
    if continuar == 'N':
        break
