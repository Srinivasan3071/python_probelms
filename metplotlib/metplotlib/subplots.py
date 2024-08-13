import matplotlib.pyplot as plt
# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 6, 8, 10]
# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(6, 8))
# Plot on the first subplot
axs[0].plot(x, y1, 'tab:blue')
axs[0].set_title('First Plot')
axs[0].set_xlabel('X-axis')
axs[0].set_ylabel('Y-axis')
# Plot on the second subplot
axs[1].scatter(x, y2, color='tab:orange')
axs[1].set_title('Second Plot')
axs[1].set_xlabel('X-axis')
axs[1].set_ylabel('Y-axis')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()
