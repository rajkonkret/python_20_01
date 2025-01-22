import csv

fields = []
rows = []

filename = '../day_2/records.csv'
# filename = '../day_2/discount.csv'

with open(filename, "r") as file:
    dialect = csv.Sniffer().sniff(file.read(1024))
    print(dialect.delimiter)
    file.seek(0)
    # csvreader = csv.reader(file, delimiter=";")
    csvreader = csv.reader(file, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x000002E62E4CE6E0> iterator
    fields = next(csvreader)  # odczyta pierwszy wiersz, ustawi odczyt na następny
    for i in csvreader:  # zacznie czzytac od drugiego wiersza
        # print(i)
        rows.append(i)

print(f"Fields: {fields}")
print(f"Rows: {rows}")

# Fields: ['name', 'branch', 'year', 'cgpa']
# Rows: [['Radek', 'Coe', '2', '9.1']]

# Fields: ['sku', 'exp_date', 'price']
# Rows: [['1', 'today', '100'],
#        ['2', 'today', '200'],
#        ['3', 'tomorrow', '150'],
#        ['4', 'today', '99.99'],
#        ['5', 'tomorrow', '500.0']]
# StopIteration - wyczerpane dane w iteratorze