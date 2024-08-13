import pandas as pd

# Sample data
data = {
    'Height': [150, 200, 170, 180, 190],
    'Weight': [65, 70, 75, 80, 85],
    'Age': [25, 30, 35, 40, 45]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Calculating the correlation matrix
correlation_matrix = df.corr()

print(correlation_matrix)
