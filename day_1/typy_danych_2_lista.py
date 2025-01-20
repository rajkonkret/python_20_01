# kolekcje

# lista - przechowuje dowolną ilość danych, różnego typu w jednej liście
# zachowuje kolejnosc przy dodawaniu elementów

# pusta lista
lista = []
print(type(lista))  # <class 'list'>
print(lista)  # []

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append()
lista.append("Radek")
lista.append("Zenek")
lista.append("Tomek")
lista.append("Marek")
print(lista)  # ['Radek', 'Zenek', 'Tomek', 'Marek']

# ['Radek', 'Zenek', 'Tomek', 'Marek']
#     0        1        2        3
#     -4       -3       -2       -1
print(len(lista))  # długość listy -> 4
print(lista[0])  # Radek
print(lista[2])  # Tomek

# print(lista[10])  # IndexError: list index out of range

print(lista[len(lista) - 1])  # ostatni element, Marek
print(lista[-1])  # Marek
print(lista[-2])  # Tomek
print(lista[-3])  # Zenek

# wyswietlenie fragmentu listy (slicowanie)
print(lista[0:2])  # ['Radek', 'Zenek'] indeksy 01
print(lista[:2])  # ['Radek', 'Zenek'] indeksy 01
print(lista[1:])  # ['Zenek', 'Tomek', 'Marek']
print(lista[3:10])  # ['Marek']

print(lista[10:29])  # []
print(lista[-4:0])  # []
print(lista[-2:0])  # [] [2:0]
print(lista[0:-2])  # [] [0:2] # ['Radek', 'Zenek']

print(lista[:])  # ['Radek', 'Zenek', 'Tomek', 'Marek']

# nadpisanie elementu na liście
lista[2] = "Zuza"
print(lista)  # ['Radek', 'Zenek', 'Zuza', 'Marek']

# dodanie elementu do listy we wskazanym indeksie
lista.insert(1, "Tomek")
print(lista) # ['Radek', 'Tomek', 'Zenek', 'Zuza', 'Marek']

# odzczytanie indexu
print(lista.index("Tomek")) # indeks 1

# usunięcie elementu
lista.remove("Tomek")
print(lista) # ['Radek', 'Zenek', 'Zuza', 'Marek']

# usunięcie po indeksie
print(lista.pop(2))  # Zuza, usunie element i wypisze jaki usunęliśmy


