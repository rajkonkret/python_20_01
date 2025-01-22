# funkcje - wydzielony fragment kodu, mozna go wywołąć w dowolnym momencie
# funkcja musibyc najpierw zadeklarowana
# w miejscu deklaracji funkcja nic nie robi
# żeby wykonac funkcję naklezy ja wywołać

# funkcje niezwracajce wyniku
# globalne
a = 6
b = 8


# PEP8 zaleca dwie linijki odstepu
# deklaracja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)  # wypisz wynik dodawania


def dodaj2(a, b):  # funkcja przyjmuje dwa argumenty, obowiązkowe do przekazania
    print(a + b)  # lokalne argumenty


# symulowanie przeciązania funkcji liczbą argumnentów
def odejmij(a, b, c=0):  # argument c o wartości domyslnej
    print(a - b - c)


# argumenty pozycyjne (wg kolejności)
# wywołąnie funkcji
dodaj()  # 14
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(5, 90)  # 95

odejmij(5, 5)  # 0
odejmij(5, 5, 5)  # -5

# argumnty po nazwie
odejmij(b=9, a=10)  # 1
odejmij(c=99, b=9, a=10)  # -98

# argumenty mieszane
# pozycyjne muszą być przed nazwanymi
odejmij(1, c=10, b=8)
# odejmij(c=1, b=10, 8) # SyntaxError: positional argument follows keyword argument

print(dodaj())  # 14, None
# print(dodaj() + dodaj()) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
