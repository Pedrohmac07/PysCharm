#Jogo da mega sena!
import random
from time import sleep

ldnm = []
qdj = int(input('Quantos jogos você quer sortear: '))

for i in range(qdj):
    print(f'Jogo {i + 1}:', end=' ')
    for a in range(6):
        ldnm.append(random.randint(0, 60))
    print(ldnm)
    ldnm.clear()
    sleep(1)

print('*' * 10,'Boa sorte!','*' * 10)
