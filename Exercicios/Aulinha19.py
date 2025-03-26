matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valp = 0
vdtc = 0
vmen = 0

for i in range(0, 3):
    for a in range(0, 3):
        matriz[i][a] = int(input(f'Digite um valor para [{i}, {a}]: '))
        if a == 1 and matriz[i][a] > vmen:
            vmen = matriz[i][a]
        if i == 2:
            vdtc += matriz[i][a]

print('Sua matriz é')
for i in matriz:
    print(i)
    for a in range(0, 3):
        if i[a] % 2 == 0:
            valp += i[a]

print(f'A soma de todos valores pares é {valp}')
print(f'A soma de todos valores da terceira coluna é {vdtc}')
print(f'O maior valor da segunda linha é {vmen}')