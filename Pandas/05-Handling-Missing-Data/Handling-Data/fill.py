# filling the missing values - fillna()
import pandas as pd

data = {
    "Name": ["Ram", None, "Vinayak", "Anish", "Sugam", "Anuj", "Dinesh", "Himanshu"],
    "Age": [15, None, 22, 23, 21, 28, 45, 23],
    "Salary": [50000, None, 10000, 30000, 90000, 60000, 40000, 50000],
    "Performance Score": [86, None, 84, 65, 76, 99, 56, 44],
}

df = pd.DataFrame(data)
print(df)

# filling default value
# df.fillna(value=0, inplace=True)
# print(df)

# filling calculated values
df["Age"].fillna(df['Age'].mean(), inplace=True)  # in the null age column it will fill the mean of the Age column
print(df)
