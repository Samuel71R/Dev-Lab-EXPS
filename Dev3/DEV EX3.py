import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Part 1: NumPy Arrays

print("--- Part 1: NumPy Arrays ---")

# 2. Create 1D and 2D arrays.
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr_1d)

arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("2D Array:\n", arr_2d)

# 3. Perform operations like addition, multiplication, slicing, and reshaping.

# Addition
arr_add = arr_1d + 5
print("Addition (arr_1d + 5):", arr_add)

# Multiplication
arr_mult = arr_2d * 2
print("Multiplication (arr_2d * 2):\n", arr_mult)

# Element-wise multiplication of two arrays (requires compatible shapes)
arr_1d_b = np.array([5, 4, 3, 2, 1])
arr_elem_mult = arr_1d * arr_1d_b
print("Element-wise multiplication (arr_1d * arr_1d_b):", arr_elem_mult)


# Slicing
slice_1d = arr_1d[1:4]
print("Slice of 1D Array (arr_1d[1:4]):", slice_1d)

slice_2d = arr_2d[0:2, 1:]
print("Slice of 2D Array (arr_2d[0:2, 1:]):\n", slice_2d)

# Reshaping
reshaped_arr = arr_1d.reshape(5, 1)
print("Reshaped 1D Array (5x1):\n", reshaped_arr)

# Reshape a 2D array (e.g., to a 1D array)
flattened_arr = arr_2d.flatten()
print("Flattened 2D Array:", flattened_arr)

# Part 2: Pandas DataFrame

print("\n--- Part 2: Pandas DataFrame ---")

# 2. Create a DataFrame from a dictionary or CSV.

# From a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df_dict = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df_dict)

# For CSV, assuming you have a 'sample.csv' file in the same directory:
# Create a dummy CSV file for demonstration
with open('sample.csv', 'w') as f:
    f.write('Product,Price,Quantity\n')
    f.write('Apple,1.0,100\n')
    f.write('Banana,0.5,150\n')
    f.write('Orange,0.75,120\n')

try:
    df_csv = pd.read_csv('sample.csv')
    print("\nDataFrame from CSV (sample.csv):\n", df_csv)
except FileNotFoundError:
    print("\n'sample.csv' not found. Please create it or provide a valid path.")

# 3. Display data, info, and statistics.
print("\nFirst 2 rows of DataFrame (df_dict):\n", df_dict.head(2))
print("\nInfo about DataFrame (df_dict):")
df_dict.info()
print("\nStatistics of DataFrame (df_dict):\n", df_dict.describe())

# 4. Perform slicing, indexing, and basic operations.

# Slicing rows
print("\nSlicing rows (df_dict[1:3]):\n", df_dict[1:3])

# Indexing columns
print("\nIndexing 'Name' column (df_dict['Name']):\n", df_dict['Name'])

# Selecting multiple columns
print("\nSelecting 'Name' and 'Age' columns:\n", df_dict[['Name', 'Age']])

# Filtering data
print("\nFiltering: Age > 25 (df_dict[df_dict['Age'] > 25]):\n", df_dict[df_dict['Age'] > 25])

# Basic operations (e.g., adding a new column)
df_dict['Salary'] = [50000, 60000, 45000, 70000]
print("\nDataFrame after adding 'Salary' column:\n", df_dict)

# Part 3: Matplotlib Basic Plots

print("\n--- Part 3: Matplotlib Basic Plots ---")

# 2. Use sample data to draw:

# Sample data
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 1, 5, 3]
categories = ['A', 'B', 'C', 'D', 'E']
values = [15, 30, 25, 10, 20]

# Line plot
plt.figure(figsize=(8, 5))
plt.plot(x_data, y_data, marker='o', linestyle='-', color='blue')
plt.title('Line Plot of Sample Data')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True)
plt.show()

# Bar plot
plt.figure(figsize=(8, 5))
plt.bar(categories, values, color='green')
plt.title('Bar Plot of Categories and Values')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y')
plt.show()

# Pie chart
plt.figure(figsize=(7, 7))
plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired(np.arange(len(categories))))
plt.title('Pie Chart of Category Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
