lista = [1,2,3,4,5,6,7,8,9,10]
nowa_lista = lista[5:]
lista=lista[:5]
print(lista, ' ' , nowa_lista)

lista=[0]+lista+nowa_lista
kopia = lista
print(kopia)
kopia.sort(reverse=True)
print(kopia)

imie = 'krzysztof'
nazwisko = 'kubiak'

print(imie, nazwisko)

imie_list = list(imie)
nazwisko_list = list(nazwisko)

print(imie_list, nazwisko_list)

imie_list[0] = imie_list[0].upper()
nazwisko_list[0] = nazwisko_list[0].upper()

# print(imie_nazwisko_list)

# imie_i_nazwisko=imie_list+nazwisko_list


print('*'.join(imie)[::-1])

zdanie="Dzisiaj jest wyjątkowo brzydka pogoda."
print(zdanie.split(' '))