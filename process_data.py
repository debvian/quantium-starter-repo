import pandas as pd
import glob

# Step 1: Get all CSV files from the 'data' folder
csv_files = glob.glob("data/*.csv")  # This finds all CSV files in the data folder

# Step 2: Read, filter, and process each file
dataframes = []  # List to store processed DataFrames

for file in csv_files:
    df = pd.read_csv(file)

    # Step 3: Filter only 'Pink Morsels'
    df = df[df['product'] == 'Pink Morsel']

    # Step 4: Create 'sales' column (quantity * price)
    df['sales'] = df['quantity'] * df['price']

    # Step 5: Keep only necessary columns: sales, date, and region
    df = df[['sales', 'date', 'region']]

    # Add to the list
    dataframes.append(df)

# Step 6: Combine all processed DataFrames into one
final_df = pd.concat(dataframes, ignore_index=True)

# Step 7: Save to a new CSV file
final_df.to_csv("data/final_sales.csv", index=False)

print("Processing complete! The formatted output file is saved as 'data/final_sales.csv'.")
