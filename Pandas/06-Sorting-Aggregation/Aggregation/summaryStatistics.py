# summary statistics in aggregation
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Vinayak", "Anish", "Sugam", "Anuj", "Dinesh", "Himanshu"],
    "Age": [15, 14, 22, 23, 21, 28, 45, 23],
    "Salary": [50000, 60000, 10000, 30000, 90000, 60000, 40000, 50000],
    "Performance Score": [86, 77, 84, 65, 76, 99, 56, 44],
}

df = pd.DataFrame(data)
print(df)

avg_salary = df["Salary"].mean()  # mean max min sum
print(avg_salary)
