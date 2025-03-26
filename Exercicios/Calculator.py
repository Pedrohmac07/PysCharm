
while True:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    print('=' * 20)
    print('Escolha uma das opções:\n'
          'Somar os valores(1)\n'
          'Subtrair os valores(2)\n'
          'Multiplicar os valores(3)\n'
          'Dividir os valores(4)')
    print('=' * 20)
    ui = int(input('Sua escolha: '))
    if ui == 1:
        print('Resultado:',n1 + n2)
    elif ui == 2:
        print('Resultado:',n1 - n2)
    elif ui == 3:
        print('Resultado:', n1 * n2)
    elif ui == 4:
        if n2 == 0:
            print('Erro. Não é possivel dividir por zero.')
        else:
            print('Resultado:', n1 / n2)
    else:
        print('Erro seu imbecil de merda')

    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break