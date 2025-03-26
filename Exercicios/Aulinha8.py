abc = str(input("Digite uma palavra: ")).strip().lower()
plvrs = abc.split()
junto = ''.join(plvrs)
invr = junto[::-1]

print(invr, junto)
if invr == junto:
    print('é um palindromo')
else:
    print('Não é um palindromo')
