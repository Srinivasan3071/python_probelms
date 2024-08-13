import pandas as pd

# Step 1: Generating Sample Data
data = {
    'Employee_ID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing', 'Finance', 'HR', 'Marketing', 'IT', 'Finance'],
    'Salary': [70000, 80000, 75000, 82000, 60000, 78000, 69000, 61000, 83000, 77000],
    'Joining_Date': pd.to_datetime(['2015-12-31', '2016-12-31', '2017-12-31', '2018-12-31', 
                                    '2019-12-31', '2020-12-31', '2021-12-31', '2022-12-31', 
                                    '2023-12-31', '2024-12-31'])
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Step 2: Working with CSV Files

# Saving DataFrame to CSV
csv_file = 'employees.csv'
df.to_csv(csv_file, index=False)
print(f'\nDataFrame saved to {csv_file}')

# Reading DataFrame from CSV
df_csv = pd.read_csv(csv_file)

# Display the DataFrame read from CSV
print("\nDataFrame read from CSV:")
print(df_csv)

# Step 3: Working with JSON Files

# Saving DataFrame to JSON
json_file = 'employees.json'
df.to_json(json_file, orient='records', date_format='iso', indent=4)
print(f'\nDataFrame saved to {json_file}')

# Reading DataFrame from JSON
df_json = pd.read_json(json_file, orient='records')

# Display the DataFrame read from JSON
print("\nDataFrame read from JSON:")
print(df_json)
