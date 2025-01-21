# pliki csv - dane oddzielone znakiem podziału
# Kowalski,Jan,Kłodzko
# Nowak,Zenon,Szczecin
# Brzęczyszczykiewicz,Grzegorz,Chrząszczyżewoszyce

import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ["Radek", "Coe", 2, '9.1']
dictionary = dict(zip(fields, row))

# newline="" ominięcie problemu pustych linii
filename = "records.csv"
with open(filename, "w", newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

filename = 'records_dict.csv'
with open(filename, "w", newline="") as file:
    csvwriter = csv.DictWriter(file, fieldnames=fields)
    csvwriter.writeheader()  # zapis nazw kolumn
    csvwriter.writerow(dictionary)

filename = 'discount.csv'
products = [
    {'sku': 1, "exp_date": "today", "price": 100},
    {'sku': 2, "exp_date": "today", "price": 200},
    {'sku': 3, "exp_date": "tomorrow", "price": 150},
    {'sku': 4, "exp_date": "today", "price": 99.99},
    {'sku': 5, "exp_date": "tomorrow", "price": 500.00},
]

fields_discount = [i for i in products[0]]  # lista kluczy ze słownika
with open(filename, "w", newline="") as file:
    csvwriter = csv.DictWriter(file, fieldnames=fields_discount)
    csvwriter.writeheader()  # zapis nazw kolumn
    csvwriter.writerows(products)  # writerows
