# wyjątki - błedy podczas wykonywania programu
# print(5 / 0)  # ZeroDivisionError: division by zero

try:
    # print(5 / 0)
    # print("a" + 9)
    # print(int("A"))
    # raise KeyError("Brak klucza")
    wartosc = 90 / 33
except ZeroDivisionError:
    print("Nie dzielimy przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Bład wartość")
except Exception as e:
    print("Błąd", e)
else:  # gdy nie ma błędu
    print("Wynik", wartosc)
finally:
    print("Wykonuje się zawsze")

print("Program nadal działa")
# Nie dzielimy przez zero
# Program nadal działa
# Błąd 'Brak klucza'
# Program nadal działa
# Wynik 2.727272727272727
# Wykonuje się zawsze
# Program nadal działa

# try - except [else - finally]
