import pandas as pd
# Sample DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)
# Removing rows with index 1 and 2
df = df.drop([1, 2])
print(df)
import pandas as pd

# Sample DataFrame with NaN values
data = {'A': [1, 2, None, 4], 'B': [5, None, 7, 8]}
df = pd.DataFrame(data)

# Remove rows with any NaN values
df = df.dropna()

print(df)
