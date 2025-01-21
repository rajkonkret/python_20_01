from datetime import datetime, date, timedelta

today = date.today()
print(today)  # 2025-01-21
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2025-01-21 14:13:52.917773

# tomorrow = today + 1 # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2025-01-22

formatted_data = datetime.now().strftime("%d/%m/%Y")
print(formatted_data)  # 21/01/2025

# 14:17
formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 14:20

# 21/01/2025
from_str = datetime.now().strptime("21/01/2025", "%d/%m/%Y")
print(from_str)  # 2025-01-21 00:00:00

products = [
    {'sku': 1, "exp_date": today, "price": 100},
    {'sku': 2, "exp_date": today, "price": 200},
    {'sku': 3, "exp_date": tomorrow, "price": 150},
    {'sku': 4, "exp_date": today, "price": 99.99},
    {'sku': 5, "exp_date": tomorrow, "price": 500.00},
]

for p in products:
    # print(p)  # {'sku': 5, 'exp_date': datetime.date(2025, 1, 22), 'price': 500.0}
    # print(p["exp_date"])
    if p["exp_date"] != today:
        continue  # przerywa bezaca iteracje petli, bierze kolejny eleement
    p['price'] *= 0.8  # 20% przeceny
    print(f"""
Price for {p['sku']}
 is now {p['price']}""")
