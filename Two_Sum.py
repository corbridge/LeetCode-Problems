lista = [1,2,3,4,5]
lista_r = []
target = 3
i = 0
j = 0

found = False

while i < len(lista) and not found:
    j = i + 1
    while j < len(lista) and not found:
        if lista[i] + lista[j] == target:
            found = True
            lista_r.append(i)
            lista_r.append(j)
print(lista_r)