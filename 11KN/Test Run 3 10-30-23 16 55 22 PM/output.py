import pandas as pd

# File path
file_path = "SDE/11KN/Test Run 3 10-30-23 16 55 22 PM/Load Test 3 - Data Acquisition 1 - (Timed).txt"

# Read the text file, specifying space as the delimiter
df = pd.read_csv(file_path, delim_whitespace=True)

# Save the DataFrame to a CSV file
csv_file = "output4.csv"
df.to_csv(csv_file, index=False)

print(f"Conversion complete. The data has been saved to {csv_file}.")
