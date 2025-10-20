"""
Create sample sales data for the project
This creates a simple CSV file to work with
"""

import pandas as pd
import numpy as np

print("Creating sample sales data...")

# Set random seed for consistent results
np.random.seed(42)

# Create sample data
n_rows = 1000

data = {
    'InvoiceNo': [f'INV{1000+i}' for i in range(n_rows)],
    'StockCode': [f'SC{np.random.randint(100, 999)}' for _ in range(n_rows)],
    'Description': [f'Product {chr(65 + i%26)}' for i in range(n_rows)],
    'Quantity': np.random.randint(1, 20, n_rows),
    'UnitPrice': np.round(np.random.uniform(1, 100, n_rows), 2),
    'CustomerID': [f'C{np.random.randint(1000, 9999)}' for _ in range(n_rows)],
    'Country': np.random.choice(['UK', 'France', 'Germany', 'Spain', 'Italy'], n_rows)
}

# Create DataFrame
df = pd.DataFrame(data)

# Add some missing values to practice cleaning
missing_indices = np.random.choice(df.index, 50, replace=False)
df.loc[missing_indices[:25], 'CustomerID'] = None
df.loc[missing_indices[25:], 'UnitPrice'] = 0

# Save to CSV
df.to_csv('sales_data.csv', index=False)

print("✅ Sample data created!")
print(f"📊 Created {len(df)} rows of sample sales data")
print("File saved as: sales_data.csv")
print("\n📋 Data preview:")
print(df.head())
print(f"\n🔍 Data info: {df.shape[0]} rows, {df.shape[1]} columns")
print("Ready to use in the analysis notebook!")