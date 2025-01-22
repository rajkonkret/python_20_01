import pandas
# pip install pandas

data = pandas.read_csv('../day_2/discount.csv', delimiter=";")

print(data)
#    sku  exp_date   price
# 0    1     today  100.00
# 1    2     today  200.00
# 2    3  tomorrow  150.00
# 3    4     today   99.99
# 4    5  tomorrow  500.00
print(data.columns)  # Index(['sku', 'exp_date', 'price'], dtype='object')