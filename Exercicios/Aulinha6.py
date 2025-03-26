import random

print('Vamos jogar jokenpo ?')
jkpu = int(input('1: Pedra, 2:Papel, 3: Tesoura'))
jkpc = random.randint(1,3)

print(jkpc)

if jkpu == 1 and jkpc ==1 or jkpu == 2 and jkpc == 2 or jkpu == 3 and jkpc ==3:
    print('Você empatou com o cpu')
elif jkpu == 1 and jkpc ==3 or jkpu == 2 and jkpc == 1 or jkpu == 3 and jkpc ==2:
    print('Voce ganhou!')
elif jkpu == 1 and jkpc ==2 or jkpu == 2 and jkpc ==3 or jkpu == 3 and jkpc ==1:
    print('Voce perdeu!')
else:
    print('Não tente roubar!')
