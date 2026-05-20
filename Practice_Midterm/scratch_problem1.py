# Write a program that helps plan a party by calculating costs. The program should:
# 1.	Ask the user for:
# •	Number of guests (a whole number)
# •	Cost per person for food (a number)
# •	Cost per person for drinks (a number)
# •	Whether they need to rent a venue: yes or no (a string)
num_guests = int(input("Number of guests: "))
food_cost = float(input("Cost per person for food: "))
drink_cost = float(input("Cost per person for drink: "))
rent_venue = input("Do you need to rent a venue? yes or no ").lower()
# 2.	Calculate:
# •	Food total (guests × food cost per person)
# •	Drink total (guests × drink cost per person)
# •	Venue cost: $0 if they do not need a venue, $250.00 if they do
# •	Grand total (food + drinks + venue)
food_total = num_guests * food_cost
drink_total = num_guests * drink_cost
if rent_venue == "yes": 
    cost_venue = 250
else:
    rent_venue = 0 
grand_total = (food_total + drink_total + cost_venue)
# 3.	Print a formatted summary using f-strings with costs formatted to 2 decimal places:
# --- Party Cost Summary ---
# Guests: 20
# Food total: $300.00
# Drink total: $100.00
# Venue cost: $250.00
# Grand total: $650.00
# 4.	If the grand total exceeds $500, print: "Tip: Ask guests to bring a dish to reduce costs!"
print(f"--- Party Cost Summary ---\n"
      f"Guests: {num_guests}\n"
      f"Food total: ${food_total:.2f}\n"
      f"Drink total: ${drink_total:.2f}\n"
      f"Venue cost: ${cost_venue:.2f}\n"
      f"Grand total: ${grand_total:.2f}") 
if grand_total > 500: 
    print(f"Tip: Ask guests to bring a dish to reduce costs!")
# Constraints
# •	You must use at least one if/else (for the venue check)
# •	You must use f-strings for all output
# •	Handle "yes", "Yes", "YES", etc. (case-insensitive)

# Example Run
# Number of guests: 20
# Food cost per person: $15.00
# Drink cost per person: $5.00
# Do you need to rent a venue? (yes/no): Yes

# --- Party Cost Summary ---
# Guests: 20
# Food total: $300.00
# Drink total: $100.00
# Venue cost: $250.00
# Grand total: $650.00

# Tip: Ask guests to bring a dish to reduce costs!

