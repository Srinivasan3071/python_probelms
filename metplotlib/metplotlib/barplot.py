import matplotlib.pyplot as plt
# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 10]

# Create a bar plot
plt.bar(categories, values, color='blue')

#Add title and labels
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

import matplotlib.pyplot as plt
# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
# Create a histogram
plt.hist(data, bins=4, color='green', edgecolor='black')
# Add title and labels
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
# Show the plot
plt.show()

