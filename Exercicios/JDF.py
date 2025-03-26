#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.
while True:
    nome = str(input('Digite seu nome: '))
    prt = int(input('Digite quantas partidas jogou: '))
    gep = dict()
    lgep = list()
    soma = 0

    for c in range(prt):
        gep['partida'] = c + 1
        gep['gols'] = int(input(f'Digite quantos gols fez na {c + 1} partida: '))
        lgep.append(gep.copy())

    for c, v in enumerate(lgep):
        soma += v['gols']

    print(lgep)
    print(f'No total você fez {soma} gols')
    media = soma / prt
    print(media)

    print(f'No campeonato inteiro, Você marcaria {media * 38:.1f} gols')

    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
