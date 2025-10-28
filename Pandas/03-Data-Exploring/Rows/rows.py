import pandas as pd

df = pd.read_json("sample_Data.json")

# head
print('Displaying first 5 rows by default, if there is no value of n')
print(df.head())
print('Displaying first 10 rows')
print(df.head(10))

# tail
print('Displaying last 5 rows by default, if there is no value of n')
print(df.tail())
print('Displaying last 10 rows')
print(df.tail(10))
