cores = {'limpa':'\033[m',
        'azul':'\033[0;34m',
        'preto': '\033[7;30m',}

print('{} Olá, mundo! {} Seja bem vindo {}Pedro{}'.format(cores['azul'], cores['limpa'], cores['preto'], cores['limpa']))