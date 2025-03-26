import math

def calc_factorial(num, show=False):
    ''''
    Calcula o fatorial de um numero.
    :param num: Number to be calculated.
    :param show:(optional) True = Show the calculation. False = only show result.
    :return: Calculated factorial
    '''

    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f

#main Program
