# sorting data
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Vinayak", "Anish", "Sugam", "Anuj", "Dinesh", "Himanshu"],
    "Age": [15, 14, 22, 23, 21, 28, 45, 23],
    "Salary": [50000, 60000, 10000, 30000, 90000, 60000, 40000, 50000],
    "Performance Score": [86, 77, 84, 65, 76, 99, 56, 44],
}

df = pd.DataFrame(data)
print(df)

# sorting data of one column
df.sort_values(by=["Name"], ascending=True, inplace=True)
print(df)

# sorting data of multiple columns
df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print(df)
