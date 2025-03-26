#Exercício Python 106: Faça um mini-sistema,
#que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’,
# o programa se encerrará. Importante: use cores.
import time

def intro():
    print('\033[0;36m', end='')
    print('=' * 20)
    print('PyHelp System')
    print('=' * 20)
    print('\033[0m', end='')


def pyHelp():
    intro()
    resp = str(input('Oque deseja buscar na biblioteca do python?: ')).strip().lower()
    print('\033[0;32m')
    print(f'Procurando Por {resp}...')
    print('\033[0m')
    time.sleep(1)
    print('\033[7m')
    print(help(resp))
    print('\033[0m')

pyHelp()
while True:
    keep = str(input('Deseja continuar?[s/n]')).lower()
    if keep == 'n':
        print('\033[0;31mPrograma finalizado com sucesso!')
        break
    else:
        pyHelp()