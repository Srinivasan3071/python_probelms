import matplotlib.pyplot as plt

# Sample data
sizes = [20, 30, 25, 25]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Create a pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Add title
plt.title('Pie Chart')

# Show the plot
plt.show()
