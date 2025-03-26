keep = 'k'
lnum = []
cdc = 0
tc = 'Não foi digitado'

while True:
    lnum += [int(input('Digite um valor: '))]
    keep = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    #ordenar os numeros da lista em forma decrescente
    lista = lnum.sort(reverse=True)

    # Verificar se o user deseja continuar
    while keep not in ['S', 'N']:
        keep = str(input('Tente novamente. Deseja continuar? [S/N] ')).strip().upper()[0]
    if keep in ['N']:
        break
for i in range(0, len(lnum)):
    if lnum[i] == 5:
        cdc += 1
        tc = 'foi digitado'


print(f'Você digitou {len(lnum)} valores.\n'
      f'A lista ordenada é {sorted(lnum, reverse=True)}\n'
      f'O numero 5 {tc}, {cdc} vezes.')
