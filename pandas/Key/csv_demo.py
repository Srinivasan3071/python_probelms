import pandas as pd
# Define data to be written to a CSV file
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
# Create a DataFrame from the data
df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv('data.csv', index=False)

# Read the CSV file into a new DataFrame
df_read = pd.read_csv('data.csv')

# Display the DataFrame read from the CSV file
print(df_read)


