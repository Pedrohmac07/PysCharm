ldn = []
ldnp = []
ldni = []

while True:
    #sistema de lista

    ui = int(input('Digite um valor: '))
    print(ldn)
    if ui %2 == 0:
        ldnp.append(ui)
        ldn.append(ui)
    else:
        ldni.append(ui)
        ldn.append(ui)

    keep = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while keep not in ['S', 'N']:
        keep = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if keep in ['N']:
        break


print(f'Lista normal organizada {sorted(ldn)}')
print(f'Lista de numeros pares organizada {sorted(ldnp)}')
print(f'Lista de numeros impares organizada {sorted(ldni)}')