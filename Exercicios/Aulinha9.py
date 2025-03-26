nums = 0
soma = 0
maior = 0
menor = 999
continuar = 'S'

while continuar == 'S':
    ui = int(input('Digite um numero: '))
    if maior < ui:
        maior = ui
    if menor > ui:
        menor = ui
    soma += ui
    nums += 1
    continuar = input('Deseja continuar? [S/N] ').upper()
print('Você digitou {} numeros, a media deles é {}.\nO maior numero foi {} e o menor foi {}'.format(nums, soma // nums, maior, menor))
