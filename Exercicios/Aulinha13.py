num = []
#Cria uma lista sem numeros repetidos, e sorteados em ordem
while True:
    ui = int(input('Digite um valor: '))
    if ui not in num:
        num.append(ui)
    cnrt = 'K'
    while cnrt != 'S' and cnrt != 'N':
        cnrt = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cnrt == 'N':
        break

print(sorted(num))