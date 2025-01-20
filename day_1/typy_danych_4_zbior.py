# zbiór (set) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # zmiana (rzutowanie na zbiór)
print(type(zbior))  # <class 'set'>
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

# pusty zbior
zb2 = set()  # tworzymy pusty zbiór
print(zb2)  # set() - pusty zbior
print(type(zbior))  # <class 'set'>

# dodanie elementu do zbioru
zbior.add(33)
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(24)
zbior.add(18)

print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunięcie pierwszego! elementu
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}
zmienna = zbior.pop()
print("Usunięty:", zmienna)  # Usunięty: 66

zbior_copy = zbior.copy()  # kopia elementów listy
print(zbior)
print(zbior_copy)
print(id(zbior))
print(id(zbior_copy))
# {777, 11, 44, 18, 22, 24}
# {18, 22, 24, 777, 11, 44}
# 2721605165216
# 2721605160736

zbior_2 = {667, 11, 44, 18, 52, 62, 999, 999, 12.34}
print(type(zbior_2))  # <class 'set'>
print(zbior_2)  # {999, 11, 44, 12.34, 18, 52, 667, 62}

# suma zbiorów
print(zbior | zbior_2)  # {999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}
print(zbior.union(zbior_2))  # {999, 777, 11, 44, 12.34, 18, 52, 22, 24, 667, 62}

# częśc wspólna
print(zbior & zbior_2)  # {18, 11, 44}
print(zbior.intersection(zbior_2))  # {18, 11, 44}

# róznica
print(zbior - zbior_2)  # {24, 777, 22}
print(zbior.difference(zbior_2))  # {24, 777, 22}
print(zbior_2.difference(zbior))  # {999, 12.34, 52, 667, 62}

krotka = tuple(zbior)
print(krotka)  # (777, 11, 44, 18, 22, 24)

lista = list(zbior)
print(lista)  # [777, 11, 44, 18, 22, 24]

# sprawdzic czy element jest w...
print(777 in lista)  # True
print(999 in zbior)  # False
print(999 in krotka)  # False
