item = {'nome': 'Bandagem', 'quantidade':10}
inventario = []
inventario.append(item.copy())
item.clear()
item = {'nome': 'Munição', 'quantidade':32}
inventario.append(item.copy())
item.clear()

for v, i in enumerate(inventario):
    print(f'item{v}:{i['nome']} {i['quantidade']}x.')
