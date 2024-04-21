##LISTA
lista = ['ala', 'ela', 'ola', 'neska', 'zuzia']

print('pierwszy element listy: ')
print(lista[0])

print('pierwsze dwa elementy listy:')
print(lista[:2])

print('co drugi element:')
print(lista[: : 2])

print('co drugi element od końca:')
print(lista[: : -2])

print('ostatnie dwa elementy:')
print(lista[-2:])

print('idenks konkretnego elementu:')
print(lista.index('neska'))

print('dodaj jeden element na końcu listy:')
lista.append('grazyna')
print(lista)

print('dodaj sekwencje na końcu listy:')
lista.extend(['ania', 'hania'])
print(lista)

print('dodaj jeden element na początku listy:')
lista.insert(0, 'anta')
print(lista)

print('usuń konkretny element z listy:')
lista.remove('grazyna')
print(lista)

print('usuń elementy od 3 do 4 z listy:')
del(lista[3:5])
print(lista)

print('skopiuj do innej listy sortując:')
lista2 = sorted(lista)
print(lista2)

print('posortuj oryginalną:')
lista.sort()
print(lista)

print('posortuj odwrotnie:')
lista.sort(reverse=True)
print(lista)

print('dodaj do siebie dwie listy')
lista1 = ['one', 'two', 'three']
lista2 = ['four', 5]
lista = lista1 + lista2
print(lista)

print('przeiteruj po elementach listy')
for item in lista:
    print(item)

print('usuń konkretny element z listy')
lista.pop(4)
print(lista)

print('długość listy')
print(len(lista))
