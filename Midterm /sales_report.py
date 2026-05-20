# A store manager needs a daily sales report. Write a program that:

# 1. Ask the user how many sales to enter (a number)
num_sales = input("How many sales to enter? ")
while not num_sales.isdigit():
    num_sales = input("Please enter a number: ")
num_sales = int(num_sales)

sales_dict = []

for i in range(num_sales):
    item_name = input("What is the item name? ")
    sale_amount = int(input("What is the sale amount in dollars? "))
    return_= input("Was it a return? yes or no ")
    if return_ == "yes": 
        return_ = True 
    else: 
        return_ = False 
    sales_dict.append({
        "item": item_name, "amount": sale_amount, "is_return": return_
    })
# 2. For each sale, ask for:
#    - Item name (a string)
#    - Sale amount in dollars (a number)
#    - Whether it was a return: yes or no (a string)

# 3. Store each sale as a dictionary in a list. Each dictionary should have keys: `"item"`, `"amount"`, and `"is_return"` (True or False)
total_revenue = 0 
for items in sales_dict: 
    total_revenue += sale_amount - return_

largest_sale = 0 
largest_sale_item = " "
for i in range(len(sales_dict)): 
    largest_sale += sales_dict['amount']
retrun_yes = []
# 4. After all sales are entered, calculate and display:
#    - Total revenue (sum of all non-return amounts, minus return amounts). Returns should be subtracted, not added. Use the accumulator pattern.
#    - Largest sale (the item name and amount of the highest non-return sale). Use the min/max pattern. If there are no non-return sales, print "No sales recorded."
#    - Returns list (the names of all items that were returns). Use the filter pattern. If there are no returns, print "No returns today."

# 5. Print a formatted summary:
#    --- Daily Sales Report ---
#    Total revenue: $247.50
#    Largest sale: Winter Jacket ($89.99)
#    Returns: Broken Lamp, Wrong Size Shirt

# Constraints:
# - You must use a `for` loop to process the list
# - You must store data in a list of dictionaries
# - You must use at least two named loop patterns (accumulator, min/max, or filter)
