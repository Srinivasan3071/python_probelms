import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create a histogram
plt.hist(data, bins=5, color='green', edgecolor='black')

# Add title and labels
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()
