# adding columns
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Vinayak", "Anish", "Sugam", "Anuj", "Dinesh", "Himanshu"],
    "Age": [15, 14, 22, 23, 21, 28, 45, 23],
    "Salary": [50000, 60000, 10000, 30000, 90000, 60000, 40000, 50000],
    "Performance Score": [86, 77, 84, 65, 76, 99, 56, 44],
}

df = pd.DataFrame(data)
print(df)

# adding column via assignment
df["Bonus"] = df['Salary'] * 0.1  # 10% of the salary
print(df)

# adding column using insert() method
df.insert(0, "Employee ID", [10, 20, 30, 40, 50, 60, 70, 80])
print(df)
