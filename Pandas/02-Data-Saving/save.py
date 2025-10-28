# saving data using pandas

import pandas as pd

# creating a dataframe
data = {
    "Name": ["Ram", "Shyam", "Vinayak", "Anish", "Sugam", "Anuj", "Dinesh", "Himanshu"],
    "Age": [15, 14, 22, 23, 21, 28, 45, 23],
    "City": ["Nagpur", "Mumbai", "Bulandshahr", "Sirsa", "Noida", "Lucknow", "Rampur", "Agra"],
    "State": ["Maharashtra", "Maharashtra", "Uttar Pradesh", "Haryana", "Uttar Pradesh", "Uttar Pradesh", "Uttarakhand",
              "Uttar Pradesh"],
}

df = pd.DataFrame(data)
print(df)

# saving data into csv, json, excel
df.to_csv("sample_Data.csv", index=False)  # index=False to avoid the indexing
df.to_json("sample_data_json.json", index=False)
df.to_excel("sample_Data.xlsx", index=False)
