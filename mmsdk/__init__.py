import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the dataset
# Replace 'sales_data.csv' with the path to your dataset
data = pd.read_csv('sales_data.csv')

# Step 2: Basic analysis
# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Summary statistics
print("\nSummary statistics:")
print(data.describe())

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Step 3: Data visualization
# Total sales per product
total_sales_per_product = data.groupby('Product')['Sales'].sum()
total_sales_per_product.plot(kind='bar', title='Total Sales per Product')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.show()

# Total sales per region
total_sales_per_region = data.groupby('Region')['Sales'].sum()
total_sales_per_region.plot(kind='bar', title='Total Sales per Region', color='orange')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()

# Sales trend over time
data['Date'] = pd.to_datetime(data['Date'])
sales_trend = data.groupby('Date')['Sales'].sum()
sales_trend.plot(title='Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()