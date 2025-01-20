# krotka - tuple - kolekcja niemutowalna, tylko do odczytu
# pozwala efektywniej zarządzać pamięcią

tupla = ("Radek", "Tomek", "Zenek", "Marek", "Anna")
print(type(tupla))  # <class 'tuple'>
print(tupla)  # ('Radek', 'Tomek', 'Zenek', 'Marek', 'Anna')

tupla1 = "Radek", "Tomek", "Zenek", "Marek", "Anna"
print(type(tupla1))  # <class 'tuple'>
print(tupla1)  # ('Radek', 'Tomek', 'Zenek', 'Marek', 'Anna')

tupla2 = ("Radek")
print(type(tupla2))  # <class 'str'>

tupla3 = "Radek",
print(type(tupla3))  # <class 'tuple'>
print(tupla3)  # ('Radek',)

# PEP8 zaleca by tupla jednoelementowa miała nawiasy
tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>
print(tupla3)  # ('Radek',)

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))

# tupla jest niemutowalna
# tupla_liczby[3] = 123 # TypeError: 'tuple' object does not support item assignment

print(tupla1.index("Anna"))  # indeks 4
print(tupla1.count("Anna"))  # występuje 1 raz

tup = 1, 2
a, b = 1, 2
a, b = tup
print(a, b)  # 1 2
tup_2 = 1, 2, 3
a, *b = tup_2  # * worek na pozostałe
print(a, b)  # 1 [2, 3]

# name1, name2, name3 rozpakowac tuple do trzech zmiennych
# "Radek", "Tomek", "Zenek", "Marek", "Anna"
name1, name2, *name3 = tupla
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Marek', 'Anna']

# "Radek", "Tomek", "Zenek", "Marek", "Anna"
name1, *name2, name3 = tupla
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek', 'Marek'] Anna

*name1, name2, name3 = tupla
print(name1, name2, name3)  # ['Radek', 'Tomek', 'Zenek'] Marek Anna

# sortowanie krotki, zwróci nową listę
print(sorted(tupla))  # ['Anna', 'Marek', 'Radek', 'Tomek', 'Zenek']
print(tupla)  # ('Radek', 'Tomek', 'Zenek', 'Marek', 'Anna'), nie zmieniło kolejności krotki
