# instrukcje warunkowe
# wyrazenie musi zwracac bool
# instrukcje sterowania przepływem programu
# w zależności od warunku wykona jeden lub drugi blok programu
# if
# odp = True
odp = False
print(bool(odp))  # True
if odp:
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print('Dalsza częśc programu')
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Dalsza częśc programu

# Dla False
# False
# Dalsza częśc programu

odp = "Radek"
print(bool("Radek"))  # True
if odp:
    print("Dane zostały odebrane")

print(bool([]))  # False

if odp == "Radek":  # == porównanie
    print("Radek")  # Radek

odp = 0
if odp:
    print("Działa")
else:  # w przeciwnym razie
    print("Błędna dane, zero")  # Błędna dane, zero

a = "Radek"
n = len(a)  # długośc tekstu
if n > 3:
    print(f"Długość tekstu większa niż 3, {n}")  # Długość tekstu większa niż 3, 5

# operator morsa (walrus)
if (n := len(a)) > 3:
    print(f"Długość tekstu większa niż 3, {n}")

# # kolejnośc warunków ma znaczenie
# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10_000:
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100_000:  # kolejny warunek
#     podatek = 0.4
# else:
#     podatek = 0.9
# print(f"Podatek wynosi {podatek * zarobki}")
# # dodac 0.2 dla zarobków od 10_000 do 29_999

sum_zam = 150
if sum_zam > 100:
    rabat = 25
else:
    rabat = 0

print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

rabacik = 25 if sum_zam > 100 else 0
print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25

# zasymulejemy system zbierania logów
# system jaki wysłął logi - musimy zmienną
# email, console, inny
# gdy sytem cosole wyswietlamy napis "Stało się coś strasznego"
# email -> "System email"
# jesli system jest email to do listy błedów wpisac opis błedu
# error, medium, inny
errror = "medium"
alert_system = "email"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("Sytem email")
    if errror == "error":
        lista_b.append("Bład Krytyczny")
    elif errror == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        print("Inny bład")
else:
    print("Inny system")

print(lista_b)
# Sytem email
# ['Bład Krytyczny']

# napisać aplikacje test z...
# zadac pytanie
# pobrac odpowiedz
# wypisac wynik spraawdzenia
# dodac punktację
punkty = 0
odp = input("Podaj datę Chrztu Polski")
if odp == "966":
    print("Brawo")
    punkty += 1  # punkty = punkty + 1
else:
    print("Masz w ksiązce na stronie 21")
print("Punkty", punkty)

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
