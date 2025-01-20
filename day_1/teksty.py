tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Wiatj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()
# zamienic tekst na duże litery
print(tekst.upper())  # WIATAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WIATJ ŚWIECIE

print(tekst)  # Wiataj Świecie
# Witaj Świecie
# 01234567890... -> indeksujemy od 0
print(tekst[3])  # a indeks 3, czwarta literka w tekscie

print(tekst.index("j"))  # indeks 4
print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # występuje 0, indeksy sprawdzane 0123, z prawej strony zbiór otwarty

teskt_zamiana = "Witaj Dobry Świecie"
print(teskt_zamiana.replace("Dobry", ""))  # Witaj  Świecie
print(teskt_zamiana.replace("Dobry ", ""))  # Witaj  Świecie
# ctrl d - powielanie linii
name = " Radek "
print(name.strip())  # "Radek" - usunięcie białych znaków(spacja) z przodu i z tyłu tekstu

encode_s = tekst.encode("utf-8")
print(encode_s)  # b'Witaj \xc5\x9awiecie'
print(type(encode_s))  # <class 'bytes'>
# \xc5\x9a - kod znaku w systemie szesnastkowym \x - system szesnastkowy
print(encode_s.decode('utf-8'))  # Witaj Świecie

# f - string
imie = "Radek"
tekst_format = f"MAm na imię {imie} i lubię pythona"
print(tekst_format)  # MAm na imię Radek i lubię pythona

tekst_format = f"\tMAm na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# \t - tabulator
# \n - nowa linia
# \b - backspace
# 	   "MAm na imię Radek
#  i lubię pythona"

starszy = "Witaj %s!"  # %s - str
print(starszy % imie)  # Witaj Radek!
print("Witaj {}!".format(imie))  # Witaj Radek!
print("Witaj", imie)  # Witaj Radek

# tekst wielolinijkowy
print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

"""Komentarz
    wielolinijkowy"""
