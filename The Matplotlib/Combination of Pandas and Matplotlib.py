import pandas as pd
import matplotlib.pyplot as plt

# THE SETUP: Creating a DataFrame
# (In the real world, this would be: df = pd.read_csv("data.csv"))

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [2500, 3200, 2800, 4100, 3900],
    "Expenses": [2000, 2100, 1900, 2500, 2400]
}
df = pd.DataFrame(data)

print("--- DataFrame Ready ---")
print(df)
print("\nGenerating charts...")

# METHOD 1: The "Manual" Way (Standard Matplotlib)
# We take specific Pandas columns (df["Column_Name"]) and drop them 
# right into the X and Y spots of the plt.plot() function.

plt.plot(df["Month"], df["Sales"], marker='o', color='green', label='Sales')
plt.plot(df["Month"], df["Expenses"], marker='x', color='red', label='Expenses')

# Adding standard labels
plt.title("Monthly Financials (Manual Method)")
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True) # Adds a background grid for easier reading

# Display the first chart
plt.show()

# METHOD 2: The "Pandas Shortcut" Way
# Because Pandas and Matplotlib are best friends, Pandas DataFrames 
# have a built-in .plot() method.


# With one line, we tell Pandas: "Plot yourself as a bar chart, 
# and use the 'Month' column as the X-axis." 
# It automatically turns all other numerical columns into bars!
df.plot(x="Month", kind="bar", title="Monthly Financials (Pandas Shortcut)")

# Even though we used the Pandas shortcut, we STILL use Matplotlib (plt)
# to tweak the chart and show it!
plt.ylabel("Amount ($)")
plt.xticks(rotation=0) # Keeps the month labels horizontal instead of sideways
plt.show()
