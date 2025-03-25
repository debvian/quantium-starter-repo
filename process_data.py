import pandas as pd
import glob

# Get all CSV files from the 'data' folder
csv_files = glob.glob("data/daily_sales_data_*.csv")  # Match only relevant files

# List to store processed DataFrames
dataframes = []

for file in csv_files:
    df = pd.read_csv(file)

    # Filter only 'Pink Morsel'
    df = df[df['product'] == 'Pink Morsel']

    # Create 'sales' column (quantity * price)
    df['sales'] = df['quantity'] * df['price']

    # Keep only necessary columns: sales, date, and region
    df = df[['sales', 'date', 'region']]

    # Add to the list
    dataframes.append(df)

# Combine all processed DataFrames into one
final_df = pd.concat(dataframes, ignore_index=True)

# Save to a new CSV file
final_df.to_csv("data/final_sales.csv", index=False)

print("✅ Processing complete! The formatted output file is saved as 'data/final_sales.csv'.")
