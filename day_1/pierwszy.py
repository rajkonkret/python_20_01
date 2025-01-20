import sys

print()  # wypisz/wydrukuj
# Process finished with exit code 0 - program zakończony poprawnie

print("Nazywam się Radek")
print('Nazywam się Radek')
# Nazywam się Radek
# Nazywam się Radek

# print("Nazywam się Radek')
#   File "C:\Users\Administrator\PycharmProjects\python_20_01\day_1\pierwszy.py", line 9
#     print("Nazywam się Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 9)
# Process finished with exit code 1bład wykonania programu
print("Dalej")  # Dalej

# type() - sprawdzenie typu danych
print(type("Radek"))  # tekst, <class 'str'>, string
print("39")
print(type("39"))  # <class 'str'>

print(39)
print(type(39))  # <class 'int'> liczba calkowita

print("39" + "39")  # łaczenie tekstów 3939, konkatenacja
print(39 + 39)  # 78
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
# nie zmaienia typów samodzielnie - silne typowanie

# rzutowanie
print(int("39") + 39)  # int() - rzutowanie tekstu na liczbę, 78
print(str(39) + "39")  # str()  - rzutowanie na string, 3939

print("160" * 5)  # 160160160160160
print(int("160") * 5)  # 800

# print(int("A")) # ValueError: invalid literal for int() with base 10: 'A'
print(sys.int_info)
# sys.int_info(
# bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# zmienna - pudełko na dane, przechowuje jeden element
# snake_case
# nazwa powinna sugerowac co zawiera

# wnioskuje typ na podstawie danych - typowanie dynamiczne
# w każdej chwili do zmiennej wrzucić dowolny typ danych
liczba = 39
print(liczba)
print(type(liczba))  # <class 'int'>

liczba = "39"
print(type(liczba))
print(liczba)

name = "Radek"
print(name)
print(type(name))  # <class 'str'>

name = 90
# print(name + "Radek")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# to jest tylko podpowiedź typu!!! nie jest to sprawdzanie typu!!!
name: str = "Radek"
print(name)
print(type(name))  # <class 'str'>

name = 190
print(name)

age: int = 56
print(age)
print(type(age))
# 56
# <class 'int'>
