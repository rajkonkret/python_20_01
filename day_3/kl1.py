# klasa - element programowania obiektowego
# klasa - szablon, przepis
# obiekt (instancja) - zbudowany wg przepisu
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# klasa musibyc zadeklarowana
# tworzenie obiektu uruchmia funkcję inicjalizujaąca w klasie


# PEP8 zaleca z dużej litery PascalCase
class Human:
    """
    Klasa Human
    """
    imie = ""
    wiek = None
    plec = "k"


print(Human.__doc__)  # Klasa Human
# tworzenie obiektu klasy Human
cz1 = Human()
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# "
# None
# k"
cz1.imie = "Radek"
cz1.wiek = 56
cz1.plec = "m"
print(cz1.imie)  # Radek
print(cz1.wiek)  # 56
print(cz1.plec)  # m
cz2 = Human()
cz2.imie = "Zuzia"
cz2.wiek = 34
print(cz2.imie)  # Zuzia
print(cz2.wiek)  # 34
print(cz2.plec)  # k

print(cz1)  # <__main__.Human object at 0x00000276471AA1E0>
print(cz2)  # <__main__.Human object at 0x00000276471AA240>
