from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca -> konstruktor
        :param gatunek:
        :param szybkosc:
        self - obiekt np.: cz1, cz2
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # dekorator - oznacza metode jako abstrakcyjna
    def wydaj_odglos(self):
        pass  # nic nie rób


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # super klasa nadrzędna

    # nadpisanie metody
    def lataj(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("ko ko ko ko")


class Orzel(Ptak):

    def wydaj_odglos(self):
        print("kier kir kier")


# pozrobieniu klasy abstrakcyjnej nie mozna tworzyc obiektów klasy Ptak
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak() # TypeError: Ptak.__init__() missing 2 required positional arguments: 'gatunek' and 'szybkosc'
# or1 = Ptak("Orzeł", 45)
# or1.lataj()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.lataj()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.lataj()  # Tu Kura domowa Ja nie latam
kur2.wydaj_odglos()  # ko ko ko ko

# or1.wydaj_odglos()

or2 = Orzel("Orzeł Bielik", 50)
or2.lataj()  # Tu Orzeł Bielik Lecę z szybkością 50
or2.wydaj_odglos()  # kier kir kier

# polimorfizm - obiekty róznych klas mają wspólną metode
lista = [or2, kur2]  # obiekty różnych klas, dziedziczących po Ptak
for i in lista:
    i.wydaj_odglos()
# kier kir kier
# ko ko ko ko
