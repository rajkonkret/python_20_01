# funkcje zwracające wynik
# kończy się instrukcją return

def dodaj(a, b):
    return a + b  # zwróć wynik działania


def odejmij(a=0, b=0, c=0):
    return a - b - c


print(dodaj(7, 90))  # 97
wynik = dodaj(7, 90)
print('Wynik', wynik)  # Wynik 97

print(odejmij())
print(odejmij(1, 2))
print(odejmij(1, 2, 3))
print(odejmij(c=10, b=8, a=9))
# 0
# -1
# -4
# -9

print(dodaj(5, 78) + odejmij(456, 6, 78))  # 455
