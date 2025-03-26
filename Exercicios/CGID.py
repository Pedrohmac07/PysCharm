#Exercício Python 094: Crie um programa que leia nome,
# sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pr = 0
registro = dict()
ldpg = list()
ldsm = list()
ldmi = list()

while True:
    registro['nome'] = str(input('Nome: '))
    registro['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    registro['idade'] = int(input('Idade: '))
    pr += 1

    ldpg.append(registro.copy())
    if registro['sexo'] == 'F':
        ldsm.append(registro.copy())
    registro.clear()
    resp = input('Deseja continuar? [S/N] ')
    while resp not in 'SsNn':
        resp = input('Erro. Deseja continuar? [S/N] ')

    if resp in 'Nn':
        break

soma_idade = 0
for c, v in enumerate(ldpg):
    soma_idade += v['idade']
media_idade = soma_idade / len(ldpg)

for c, v in enumerate(ldpg):
    if v['idade'] > media_idade:
        ldmi.append(v['nome'])



print('=' * 20)
print(ldpg)
print('=' * 20)
print(f'Foram cadastradas {pr} pessoas')
print(f'A media das idades foi {media_idade}')
print(f'Mulheres: {ldsm}')
print(f'Maiores de idade: {ldmi}')
