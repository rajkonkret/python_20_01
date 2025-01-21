# słownik
# {"klucz": "wartość"}
# słownik jest odpowiednikiem jsona w pythonie
# klucze nie mogą się powtarzać

# pusty słownik
dictionary = dict()
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dict_1 = {}
print(dict_1)  # {}
print(type(dict_1))  # <class 'dict'>

# dodanie elementu do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 39
print(dictionary)  # {'imie': 'Radek', 'wiek': 39}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 39])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 39)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39}

# wypisanie wartości dla klucza
print(dictionary['imie'])  # Tomek

# print(dictionary['Imie'])  # KeyError: 'Imie'
print(dictionary.get("Imie"))  # None, nie znalazł klucza
print(dictionary.get("Imie", "default"))  # default, nie znalazł klucza, podstawił wartość domyślną

dictionary.update({'data': '12-12-2025'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 39, 'data': '12-12-2025'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 5)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 5}

# input() - pobiera dane np.: od użytkownika
# tekst = input("Podaj imię")
# print(tekst)

# napisac aplikacje kalkulator
# pobrac dwie liczby -> 2 x input
# wyswietlic wynik działania (+) -> print
# a = int(input("Podaj pierwszą liczbę"))  # zwraca str
# b = input("Podaj drugą liczbę")
# print(f"Wynik działania {a} + {b} = {a + float(b)}")
# Podaj pierwszą liczbę5
# Podaj drugą liczbę6.7
# Wynik działania 5 + 6.7 = 11.7

# napisac aplikacje słownik pol -> ang
pol_ang = {'pies': 'dog', 'kot': "cat", "dach": "roof"}
print("Dostępne słówka", pol_ang.keys())
odp = input("Podaj słowo do przetłumaczenia")
# print(pol_ang[odp.strip().lower()])
print(pol_ang.get(odp.strip().casefold()))
#  """ Return a version of the string suitable for caseless comparisons. """
# ẞ -> ss
print("GROSS".casefold() == "Groẞ".casefold())  # True
print("GROSS".lower() == "Groẞ".lower())  # False
