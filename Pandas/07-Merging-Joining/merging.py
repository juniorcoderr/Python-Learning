import pandas as pd

# customer dataframe
df_customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
})

# order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1, 2, 4],
    'OrderAmount': [10, 20, 30],
})

# merging
# df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='inner')
# df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='outer')
# df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='left')
# df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='right')
# df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='cross')
print('Join')
# print(df_merged)
