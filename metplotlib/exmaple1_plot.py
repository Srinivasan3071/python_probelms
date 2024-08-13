import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = [0, 1, 2, 3, 4, 5]

# Create a histogram with KDE
sns.histplot(data, kde=True)

# Show the plot
plt.show()
