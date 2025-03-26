num = int(input('Digite um numero: '))
div = 0

for i in range(1,num+1):
    if num % i == 0:
        print("\033[0;31m", end= '')
        div += 1
    else:
        print("\033[0;32m", end= '')
    print('{} '.format(i), end='')
print('\033[0m O numero {} foi divisivel {} vezes'.format(num, div))
if div == 2:
    print("\033[0;32m", 'o numero é primo!', end='')
else:
    print("\033[0;32m", 'Não é primo' , end= '')