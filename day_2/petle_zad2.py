# while - sterowana warunki
#
# while True:
#     print("Pętla nieskończona")

licznik = 0
while True:
    licznik += 1
    print("Komunikat")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 2")

# password = input("Podaj hasło")
# while password != "secret":  # != rózne
#     password = input("Błędne hasło, podaj ponownie")
# print("Hasło prawidłowe")

# Podaj hasłoass
# Błędne hasło, podaj ponownieasasa
# Błędne hasło, podaj ponowniedsadas
# Błędne hasło, podaj ponownieadasdas
# Błędne hasło, podaj ponowniesecret
# Hasło prawidłowe

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
elemnt_to_remove = 5
while elemnt_to_remove in my_list:
    my_list.remove(elemnt_to_remove)

print(my_list)  # [1, 2, 3, 4, 6], nie zmmieniło kolejności

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")
    #  A string is numeric if all characters in the string are numeric
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))
print(lista)  # ['2', '3', '4', '5', '6'] string
print(lista_int)  # [1, 2, 3, 4] int
