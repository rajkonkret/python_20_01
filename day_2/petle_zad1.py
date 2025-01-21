# petlę - możliwosc wykonania kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(5):  # int od 0 do 4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):  # niema zmienna
    print("Test podłoga")
    # print(_)

for i in range(5):
    print(i * 2)
    print(i + 2)

# lotto
lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)
lista_wyl = []
for i in range(6):  # 0 do 5 -> 012345
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wyl.append(wyn)

print(lista_wyl)  # [41, 24, 49, 6, 4, 21]
print(random.choices(lista_kule, k=6))  # [18, 4, 15, 42, 4, 35] z powtórzeniami
print(random.sample(lista_kule, 6))  # [35, 42, 7, 4, 48, 32], bez powtórzeń

for i in range(10):
    if i % 2 == 0:  # modulo
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

lista3 = []
for j in range(10):
    if j % 2 == 0:
        lista3.append(j)
print(lista3)  # [0, 2, 4, 6, 8]

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

for c in lista_wyl:
    if c > 10:
        print("Większy niż 10", c)
    else:
        print("Mniejsze, równa 10", c)
# Większy niż 10 33
# Większy niż 10 23
# Mniejsze, równa 10 3
# Większy niż 10 49
# Większy niż 10 37
# Większy niż 10 22

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print(c)
    print("Przy każdym przejsciu pętli")
# Przy każdym przejsciu pętli
# 3
# Przy każdym przejsciu pętli
# Przy każdym przejsciu pętli
# Przy każdym przejsciu pętli
# Przy każdym przejsciu pętli

imiona = ["Radek", "Tomek", "Zenek", "Zuza"]
for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Zuza
# 0 Radek

for i in imiona:
    print(imiona.index(i), i)

for i in range(len(imiona)):
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zuza

# enumerate() - zwraca numer i element kolekcji
for p in enumerate(imiona):
    print(p)
# (0, 'Radek') -> 0 Radek
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Zuza')
a, b = (1, 'Tomek')
print(a, b)  # 1 Tomek, rozpakowanie krotki
for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zuza
for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Zuza
imiona = ["Radek", "Tomek", "Zenek", "Zuza", 'Gosia']
wiek = [45, 54, 23, 34]
# Radek 45
# zip() łączy kolekcje
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 45)
# ('Tomek', 54)
# ('Zenek', 23)
# ('Zuza', 34)
for i, w in zip(imiona, wiek):
    print(i, w)
# Radek 45
# Tomek 54
# Zenek 23
# Zuza 34
for i in enumerate(zip(imiona, wiek), start=1):
    print(i)
# (1, ('Radek', 45))
# (2, ('Tomek', 54))
# (3, ('Zenek', 23))
# (4, ('Zuza', 34))
# ile jest elementów(wartości)
a, b = (1, ('Radek', 45))  # mamy dwie wartości 1 i wenętrną krotkę ('Radek', 45)
print(f"{a=} {b=}")  # a=1 b=('Radek', 45)
c, d = ('Radek', 45)
print(f"{c=} {d=}")  # c='Radek' d=45
print(a, c, d)  # 1 Radek 45
x, (y, z) = (1, ('Radek', 45))
print(x, y, z)
for i, (o, w) in enumerate(zip(imiona, wiek), start=1):
    print(i, o, w)
# 1 Radek 45
# 2 Tomek 54
# 3 Zenek 23
# 4 Zuza 34
