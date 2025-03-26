def factorial(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    return f

fctr = int(input('Digite um numero para fatorar:'))
resultado = factorial(fctr)
print(resultado)