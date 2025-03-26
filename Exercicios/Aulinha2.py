#num = int(input('Digite um numero de 4 digitos: '))
#n = str(num)

#print('unidade: {}\ndezena: {}\ncentena: {}\nmillhar {}'.format(n[3], n[2], n[1], n[0]))

num = int(input('Digite um numero de 4 digitos: '))
u = num % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('unidade: {}\n dezena{}\n centena{}\n milhar{}'.format(u,d,c,m))