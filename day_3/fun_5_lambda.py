# funkcja lambda
# skrócony zapis funkcji
# lambda zawsze zwraca wynik

def odejmij(a, b):
    return a - b


odejmij2 = lambda a, b: a - b
print(odejmij(3, 4))
print(odejmij2(3, 4))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(18))  # dorosły

# mapowanie danych - zmiana danych
lista = [1, 2, 3, 5, 10, 20, 50, 200, 300, 500]
lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)  # [2, 4, 6, 10, 20, 40, 100, 400, 600, 1000]
print([i * 2 for i in lista])  # [2, 4, 6, 10, 20, 40, 100, 400, 600, 1000]
lista_wyn_f = []


def zmien(x):
    return x * 2


for i in lista:
    lista_wyn_f.append(zmien(i))
print(lista_wyn_f)  # [2, 4, 6, 10, 20, 40, 100, 400, 600, 1000]

# funkcje wyższego rzędu
# map() - bierze element, wykonuje na nim zadanie zadane funkcją
print(f"Użycie map() {list(map(zmien, lista))}") # zmien zawiera adres funkcji a nie wynik działania funkcji!!!
# Użycie map() [2, 4, 6, 10, 20, 40, 100, 400, 600, 1000]
# moze byc wykonana w mmiejscu deklaracji
# uzyta jako funkcja anonimowa - bez nazwy
print(f"Użycie map() {list(map(lambda x: x * 2, lista))}")
print(f"Użycie map() {list(map(lambda x: x * 4, lista))}")
print(f"Użycie map() {list(map(lambda x: x * 8, lista))}")
# Użycie map() [2, 4, 6, 10, 20, 40, 100, 400, 600, 1000]
# Użycie map() [4, 8, 12, 20, 40, 80, 200, 800, 1200, 2000]
# Użycie map() [8, 16, 24, 40, 80, 160, 400, 1600, 2400, 4000]