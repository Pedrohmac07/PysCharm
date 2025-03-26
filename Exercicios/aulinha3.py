cidade = str(input('Digite uma frase: ').strip())
cidadeor = ''.join(cidade.split())
ver = cidadeor.lower()
conta = ver.count('a')
first = ver.find('a')
last = ver.rfind('a')

print(conta)
print(first)
print(last)

