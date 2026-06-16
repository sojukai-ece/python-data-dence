#Task #1
#A customer just placed an order, and you need to log the details of their transaction.
"""
The task: Create four variables to store the following data:

1. A variable named beverage that stores the text: Espresso
2. A variable named quantity that stores the whole number: 3
3. A variable named price_per_cup that stores the decimal: 3.50
4. A variable named is_takeaway that stores a true/false value indicating the order is to-go (True).
"""

#Solution for the given problem:

beverage = "Espresso"
quantity = 3
price_per_cup = 3.50
is_takeaway = True

print(beverage)
print(quantity)
print(price_per_cup)
print(is_takeaway)

#Task #2
#You want to organize the shop's menu and track the number of customers who visited this week.
"""
The Task: 
1.  Lists: Create a list named daily_customers that contains the following numbers representing Monday through Friday: 45, 52, 38, 61, 59.
2.  Dictionaries: Create a dictionary named menu_item that stores the details of a single product. Use the keys "name", "price", and "in_stock". Assign them the values "Latte", 4.25, and True, respectively.
"""

# List of daily customers
daily_customers = [45, 52, 38, 61, 59]

# Dictionary for a menu item
menu_item = {
    "name": "Latte",
    "price": 4.25,
    "in_stock": True
}

print(daily_customers)
print(menu_item)

#Task #3
#You need an automated accouting system to tell you if the shop had a busy day or a slow day based on the customer data.
"""
The Task:
Using the daily_customers list you created in Exercise 2, write a for loop that iterates through each number in the list. Inside the loop, write an if/else statement with the following rules:
1. If the number of customers is 50 or greater, print: "Busy day!"
2. Else (if it's under 50), print: "Slow day."
"""

# Reusing the list from Exercise 2
daily_customers = [45, 52, 38, 61, 59]

# The loop and decision-making logic
for customers in daily_customers:
    if customers >= 50:
        print("Busy day!")
    else:
        print("Slow day.")
