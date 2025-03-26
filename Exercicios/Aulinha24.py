import random
from time import sleep

jgdrs = dict()
lista = list()


for i in range(4):
    jgdrs[f'Jogador'] = int(i)
    jgdrs[f'Valor'] = int(random.randint(0, 6))
    lista.append(jgdrs.copy())
    jgdrs.clear()

print('=' * 20)
for i in lista:
    print(i)
    sleep(1)
print('=' * 20)
nova_lista = sorted(lista, key=lambda d:d['Valor'], reverse=True)
print('=' * 20)
print('Ranqueados')
for i in nova_lista:
    print(i)
print('=' * 20)