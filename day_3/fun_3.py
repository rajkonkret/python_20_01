# zrobić funkcję obliczjącą średnią
def srednia(name=None, *cyfry):  # * dowolna ilośc argumentów pozycyjnych
    print(cyfry)  # (1, 2, 3) -> krotka
    # suma liczb, ilość liczb
    count = len(cyfry)
    suma_p = sum(cyfry)  # sumowanie elementów kolekcji
    suma = 0
    try:
        for c in cyfry:
            suma += c  # suma = suma + c

        avg = suma / count
        avg_p = suma_p / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi: {avg}")
        print(f"Średnia dla ucznia {name} wynosi: {avg_p}")
    finally:
        print("koniec")


srednia()
srednia(1, 2)
srednia(1, 2, 3)
# Średnia dla ucznia  Radek wynosi 5.0
srednia("Radek", 6, 5, 6, 5, 4, 5, 6)
name, *cyfry = ("Radek", 6, 5, 6, 5, 4, 5, 6)

# ()
# Bład division by zero
# koniec
# (1, 2)
# Średnia wynosi: 1.5
# Średnia wynosi: 1.5
# koniec
# (1, 2, 3)
# Średnia wynosi: 2.0
# Średnia wynosi: 2.0
# koniec
