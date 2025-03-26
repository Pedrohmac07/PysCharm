
mom = 0
men = 0
ldn = 0
enum = []

#Ordenar uma lista sem usar sort()
for i in range(0,  5):
    ui = int(input('Digite um valor: '))
    if i == 0:
        mom = men = ldn = ui
        enum.append(ui)
    if ui >= mom and ui != men:
        mom = ui
        ldn = ui
        enum.append(ui)
    elif ui <= men and ui != mom:
        men = ui
        ldn = ui
        enum.insert(0,ui)
    elif ui > men and ui > ldn and ui != mom:
        ldn = ui
        enum.insert(i,ui)
    elif ui > men and ui < ldn:
        enum.insert(enum.index(ldn), ui)
        ldn = ui


print(enum)