import pandas as pd

# File path
file_path = ""

# Read the text file, specifying space as the delimiter
df = pd.read_csv(file_path, delim_whitespace=True)

# Save the DataFrame to a CSV file
csv_file = "output3.csv"
df.to_csv(csv_file, index=False)

print(f"Conversion complete. The data has been saved to {csv_file}.")
