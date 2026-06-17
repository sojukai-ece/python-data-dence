import pandas as pd
# Setup: Creating a simple DataFrame to test our functions and their usage

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Age": [25, 30, 35, 28, None],  # 'None' simulates missing data
    "Department": ["Sales", "IT", "IT", "HR", "Sales"],
    "Salary": [50000, 75000, 80000, 60000, 55000]
}

# 'pd.DataFrame()' is a function belonging to the Pandas library (pd).
# It takes standard Python data and upgrades it into a Pandas object.
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n" + "-"*50 + "\n")


# CATEGORY 1: INSPECTION FUNCTIONS (Methods)
# These are used using 'df.' because they belong to the DataFrame object.

# 1. df.head()
# Returns the first 'n' rows of the DataFrame (default is 5). 
# Good for: Getting a quick look at the top of a massive dataset.
print("1. Using df.head(2):")
print(df.head(2)) 
print("-" * 30)

# 2. df.info()
# Prints a concise summary of the DataFrame, including column names, 
# data types, and how many non-null (non-empty) values exist.
# Good for: Finding out if you have missing data or incorrect data types.
print("2. Using df.info():")
df.info() 
print("-" * 30)

# 3. df.describe()
# Generates descriptive statistics (mean, min, max, etc.) for numerical columns.
# Good for: Getting instant mathematical summaries of your data.
print("3. Using df.describe():")
print(df.describe())
print("-" * 30)


# CATEGORY 2: ANALYSIS & AGGREGATION FUNCTIONS
# These functions do math on specific columns.

# 4. df['Column_Name'].mean() / .max() / .min() / .sum()
# Calculates the specific math operation for a single column.
# Good for: Finding total revenue, average age, highest salary, etc.
print("4. Math Functions:")
average_salary = df["Salary"].mean()
max_age = df["Age"].max()
print(f"The average salary is: {average_salary}")
print(f"The oldest person is: {max_age} years old")
print("-" * 30)

# 5. df['Column_Name'].value_counts()
# Counts how many times each unique value appears in a column.
# Good for: Finding out how many employees are in each department, or tallying votes.
print("5. Using .value_counts() on the Department column:")
print(df["Department"].value_counts())
print("-" * 30)


# CATEGORY 3: CLEANING FUNCTIONS

# 6. df.dropna()
# Creates a copy of the DataFrame with any rows containing missing data removed.
# Good for: Quickly getting rid of incomplete data (Notice Eve is removed!).
print("6. Using df.dropna():")
print(df.dropna())
print("-" * 30)

# 7. df.fillna()
# Replaces missing (NaN/None) values with a specified value.
# Good for: Replacing missing ages with a default number, like 0.
print("7. Using df.fillna(0):")
print(df.fillna(0))
print("-" * 50)

# Notice that we use 'df.' for all of these. Since df stands for DataFrame which is inside the pandas library.
# If you typed 'head(df)', Python would crash because 'head()' is a method 
# attached strictly to the 'df' object, not a standalone Python tool.
