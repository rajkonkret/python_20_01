dictionary = {'imie': "Radek", 'nazwisko': "kowalski"}

# wyswietla klucze
for i in dictionary:
    print(i)

# imie
# nazwisko
for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wyswietlenie wartości
for i in dictionary.values():
    print(i)
# Radek
# kowalski

# wyswietli pary
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'kowalski')
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => kowalski
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>kowalski
for k, v in dictionary.items():
    print(k, v, sep="=>", end="")
# imie=>Radeknazwisko=>kowalski
print("Dopisane")  # imie=>Radeknazwisko=>kowalskiDopisane, end="\n"
print("Następna linia")
# imie=>Radeknazwisko=>kowalskiDopisane
# Następna linia
