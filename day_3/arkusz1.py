# pliki excel
# jako alias
import pandas as pd
import numpy as np
import openpyxl

# pip install sciezka do pliku whl
technologies = ['Spark', "Pandas", 'Python', "PHP"]
fee = [25000, 15000, 12000, 23000]
duration = ['50 Days', '30 Days', np.nan, '15 Days']
# np.nan to odpowiednik None
discount = [2000, 1500, 800, 500, 500]
columns = ['Courses', 'Fee', "Duration", 'Discount']

df = pd.DataFrame(list(zip(technologies, fee, duration, discount)),
                  columns=columns)

print(df)
#   Courses    Fee Duration  Discount
# 0   Spark  25000  50 Days      2000
# 1  Pandas  15000  30 Days      1500
# 2  Python  12000      NaN       800
# 3     PHP  23000  15 Days       500

df.to_excel('courses.xlsx')
df.to_excel('courses_no_index.xlsx', index=False)
