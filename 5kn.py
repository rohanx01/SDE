import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load data from the Excel file
excel_file = 'output3.xlsx'
sheet_name = 'Sheet1'
data = pd.read_excel(excel_file, sheet_name=sheet_name)

# Extract Stress and Strain data
stress = data['Stress(MPa)']
strain = data['Strain']

# Create an empty figure
fig, ax = plt.subplots(figsize=(10, 10))
plt.title('Animated Hysteresis Curve of Stress vs. Strain')
plt.xlabel('Strain')
plt.ylabel('Stress')
plt.grid(False)

# Set the axis limits to include both positive and negative values
max_y = max(max(stress), abs(min(stress))) + 10
max_x = max(max(strain), abs(min(strain))) + 0.001
ax.set_xlim(-max_x, max_x)
ax.set_ylim(-max_y, max_y)
ax.axhline(y=0, color='black', linestyle='--')
ax.axvline(x=0, color='black', linestyle='--')

# Initialize an empty line for the animation
line, = ax.plot([], [], linestyle='-', marker='o')

# Function to update the plot for the animation
def update(frame):
    # Plot data up to the current frame
    ax.plot(strain[:frame], stress[:frame], linestyle='-', marker='o', color='b')
    line.set_data(strain[:frame], stress[:frame])
    return line,

# Create an animation with frames equal to the number of data points and a slower interval
ani = FuncAnimation(fig, update, frames=len(strain), blit=True, interval=300)

# Show the animated plot
plt.show()
