"""
The task.
You have a temperature sensor outside your shop. Most of the time it works, but occasionally it glitches and records a temperature of -999. You need to clean this data before you can analyze it.

Objectives:
1. Create a list called raw_temps with these numbers: 72, 74, -999, 75, 71, -999, 73.
2. Create a new, empty list called clean_temps. (Hint: just use empty brackets []).
Write a for loop to iterate through raw_temps.
3. Inside the loop, write an if statement: If the temperature is not equal to -999, append (add) that temperature to your clean_temps list.
4. Print the clean_temps list. It should no longer contain any errors!

"""


# 1. The list with errors
raw_temps = [72, 74, -999, 75, 71, -999, 73]

# 2. An empty list to hold the good data
clean_temps = []

# 3 & 4. Filtering the data
for temp in raw_temps:
    if temp != -999: # The != symbol means "not equal to"
        clean_temps.append(temp) # .append() adds an item to a list

# 5. Output should be [72, 74, 75, 71, 73]
print(clean_temps)

