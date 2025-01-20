user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # <class 'float'>, liczby zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 456789098123  # int

print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# TypeError: %d format: a real number is required, not str
# print("Witaj %d, masz teraz %s lat." % (user, wiek))

print(f"Wiatj {user}. Masz teraz {wiek} lat.")  # Wiatj Tomek. Masz teraz 39 lat.

print("Używamy wersji pythona %i" % 3)  # Używamy wersji pythona 3
print("Używamy wersji pythona %f" % 3)  # Używamy wersji pythona 3.000000
print("Używamy wersji pythona %.1f" % 3)  # Używamy wersji pythona 3.0

print(f"Uzywamy wersji python {wersja}")  # Uzywamy wersji python 3.900001
print(f"Uzywamy wersji python {wersja:.1f}")  # Uzywamy wersji python 3.9
print(f"Uzywamy wersji python {wersja:.2f}")  # Uzywamy wersji python 3.90
print(f"Uzywamy wersji python {wersja:.0f}")  # Uzywamy wersji python 4, zaokrągla wyświetlanie
print(f"Uzywamy wersji python {3.6789:.2f}")  # Uzywamy wersji python 3.68, zaokrągla wyświetlanie

print(f"{user:<10}")  # "Tomek     "
print(f"{user:>20}")  # "               Tomek"
print(f"{user:^25}")  # "          Tomek          "
print(f"{user:.^25}")  # "..........Tomek.........."

print(liczba)  # 456789098123
print(f"Nasza duza liczba {liczba:,}")  # Nasza duza liczba 456,789,098,123
print(f"Nasza duza liczba {liczba:_}")  # Nasza duza liczba 456_789_098_123
print(f"Nasza duza liczba {liczba:_}".replace("_", " "))  # Nasza duza liczba 456 789 098 123
print(f"Nasza duza liczba {liczba:_}".replace("_", "."))  # Nasza duza liczba 456.789.098.123

# liczba2 = 150000000000
liczba2 = 150_000_000_000
print(type(liczba2))  # <class 'int'>
print(liczba2)  # 150000000000
