# dropping the missing values - dropna()
import pandas as pd

data = {
    "Name": ["Ram", None, "Vinayak", "Anish", "Sugam", "Anuj", "Dinesh", "Himanshu"],
    "Age": [15, None, 22, 23, 21, 28, 45, 23],
    "Salary": [50000, None, 10000, 30000, 90000, 60000, 40000, 50000],
    "Performance Score": [86, None, 84, 65, 76, 99, 56, 44],
}

df = pd.DataFrame(data)
print(df)

df.dropna(inplace=True)

# drop missing values in rows
# df.dropna(axis=0, inplace=True)

# drop missing values in columns
# df.dropna(axis=1, inplace=True)

print(df)
