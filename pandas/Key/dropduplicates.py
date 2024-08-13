import pandas as pd

# Sample DataFrame with duplicate rows
data = {'A': [1, 2, 2, 4], 'B': [5, 6, 6, 8]}
df = pd.DataFrame(data)

# Remove duplicate rows
df = df.drop_duplicates()

print(df)
