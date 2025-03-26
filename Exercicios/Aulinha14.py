num = []
mai = 0
men = 0

#Programa que le 5 numeros e mostra o menor e o maior em suas respectivas posições
for c in range(0,5):
    num.append(int(input('Digite um valor: ')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        elif num[c] < men:
            men = num[c]

print(num)

print(mai)
for i, v in enumerate(num):
    if v == mai:
        print(i, end='...')

print()
print(men)
for i, v in enumerate(num):
    if v == men:
        print(i, end='...')