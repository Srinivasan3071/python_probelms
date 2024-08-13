import pandas as pd

# Define data as a dictionary
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Kathy'],
    'age': [30, 25, 35, 40, 29, 31, 27, 33, 26, 38, 28],
    'city': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Boston', 'Seattle', 'Denver', 'Miami', 'Atlanta', 'Philadelphia', 'San Diego']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Print the first 10 rows of the DataFrame
# print(df.head(4))
print(df.tail())
