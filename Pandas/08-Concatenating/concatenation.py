import pandas as pd

# customer record region one
df_region1 = pd.DataFrame({
    'CustomerID': [1, 2],
    'Name': ['Alice', 'Bob'],
})

# customer record of region two
df_region2 = pd.DataFrame({
    'CustomerID': [3, 4],
    'Name': ['Shyam', 'Ram']
})

# concatenating vertically - row - wise (default)
df_concat_vertical = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)
print(df_concat_vertical)

# concatenating horizontally = column - wise
df_concat_horizontal = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print(df_concat_horizontal)
