import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Generating Sample Data
data = {
    'Employee_ID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'Marketing', 'Finance', 'HR', 'Marketing', 'IT', 'Finance'],
    'Salary': [70000, 80000, 75000, 82000, 60000, 78000, 69000, 61000, 83000, 77000],
    'Years_Experience': [5, 8, 6, 9, 3, 7, 4, 2, 10, 7],
    'Joining_Date': pd.to_datetime(['2015-12-31', '2016-12-31', '2017-12-31', '2018-12-31',
                                    '2019-12-31', '2020-12-31', '2021-12-31', '2022-12-31',
                                    '2023-12-31', '2024-12-31'])
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Sample DataFrame:")
print(df)

# Step 2: Basic Plots with Matplotlib

# Line Plot: Salary over Experience
plt.figure(figsize=(10, 6))
plt.plot(df['Years_Experience'], df['Salary'], marker='o', linestyle='-', color='b')
plt.title('Salary vs. Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.grid(True)
plt.show()

# Bar Plot: Salary by Department
plt.figure(figsize=(10, 6))
plt.bar(df['Department'], df['Salary'], color='skyblue')
plt.title('Salary by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.show()

# Scatter Plot: Salary vs. Years of Experience
plt.figure(figsize=(10, 6))
plt.scatter(df['Years_Experience'], df['Salary'], color='red')
plt.title('Salary vs. Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Step 3: Advanced Visualizations with Seaborn

# Histogram and KDE: Salary Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['Salary'], kde=True, color='purple')
plt.title('Salary Distribution with KDE')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Box Plot: Salary by Department
plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='Salary', data=df, palette='Set2')
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.show()

# Heatmap: Correlation Matrix
plt.figure(figsize=(8, 6))
corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()
