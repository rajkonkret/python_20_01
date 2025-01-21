import sys

wiek = 47
rok = 2024
temp = 36.6

print(temp)
print(type(temp))  # <class 'float'>

print(wiek + rok)
print(wiek - rok)
print(wiek * rok)
print(wiek / rok)  # float, 0.023221343873517788
print(rok // wiek)  # 43, częśc całkowita z dzielenia
print(2024 / 47)  # 43.06382978723404
print(43 * 47)  # 2024 - 2021 = 3
print(rok % wiek)  # reszta z dzielenia, modulo -> 3 reszty
print(5 % 2)  # reszta 1

print(wiek ** rok)  # potęgowanie

# len() długośc kolekcji(tekstu)
print(len(str(wiek ** rok)))  # długość 3385 znaków
# print(len(str(wiek ** rok ** 2)))  # długość 3385 znaków
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# float ma bład zaokrąglenia
# wynika z zapisu wykladniczego
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.2 + 0.1)  # 0.30000000000000004
# For example,
# in a floating-point arithmetic with five base-ten digits,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal  - pozwala ominąć bład zaokrąglenia
print(f"{0.2 + 0.7:.2f}")  # 0.90
a = 0.8999999999999999
a = round(a, 2)  # 0.90
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308,
# min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"""
{temp}
    {wiek}""")

# "36.6
#     47"

# typ logiczny
# prawda, fałsz
# 1, 0
# True, False - obowiązkowo dużymi literami
czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, typ logiczny, boolean

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False

print(bool(100))  # True
print(bool(-100))  # True
print(bool("Radek"))  # True

print(bool(""))  # False
print(bool(None))  # odpowiednik null, nic, stan nieokreslony, False

a = 8
b = 6

print(f"Porównaie {a} < {b} = {a < b}")  # Porównaie 8 < 6 = False
print(f"Porównaie {a} > {b} = {a > b}")  # Porównaie 8 > 6 = True
print(f"Porównaie {a} >= {b} = {a >= b}")  # Porównaie 8 >= 6 = True
print(f"Porównaie {a} <= {b} = {a <= b}")  # Porównaie 8 <= 6 = False
print(f"Porównaie {a <= b = }")  # Porównaie a <= b = False

print(f"Porównanie {a} == {b} = {a == b}")  # == porównanie
print(f"Porównanie {a} != {b} = {a != b}")  # !=  czy różne
# Porównanie 8 == 6 = False
# Porównanie 8 != 6 = True

# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False
# The or Operator’s Truth Table:
#
# Expression    Evaluates to
# True or True    True
# True or False    True
# False or True    True
# False or False    False
# The not Operator’s Truth Table:
#
# Expression    Evaluates to
# not True    False
# not False