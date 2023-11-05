import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps

# Load data from the Excel file
excel_file = '15kN.xlsx'
sheet_name = 'Sheet1'
data = pd.read_excel(excel_file, sheet_name=sheet_name)

# Extract Stress and Strain data
stress = data['Stress(MPa)']
strain = data['Strain']

# Create the curve plot connecting points in the same order with curves
plt.figure(figsize=(10, 10))
plt.plot(strain, stress, linestyle='-', marker='None')
plt.title('Hysteresis Curve of Stress vs. Strain (15kN)')
plt.xlabel('Strain')
plt.ylabel('Stress')
plt.grid(False)

# Set the axis limits to include both positive and negative values
max_y = max(max(stress), abs(min(stress))) + 10
max_x = max(max(strain), abs(min(strain))) + 0.001
plt.xlim(-max_x, max_x)
plt.ylim(-max_y, max_y)
plt.axhline(y=0, color='black', linestyle='--')
plt.axvline(x=0, color='black', linestyle='--')

# Calculate the area of the hysteresis loop using numerical integration (Simpson's rule)
area = simps(stress, strain)

# Show the plot
print("Area of Hysteresis Loop:", area)
plt.show()

# Print the area of the hysteresis loop
