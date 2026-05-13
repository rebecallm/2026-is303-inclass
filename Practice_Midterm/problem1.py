# Write a program that helps plan a party by calculating costs. The program should:
# 1.	Ask the user for:
# •	Number of guests (a whole number)
# •	Cost per person for food (a number)
# •	Cost per person for drinks (a number)
# •	Whether they need to rent a venue: yes or no (a string)
num_guest = int(input("Number of guests: "))
cost_per_person = int(input("Cost per person for food: "))
cost_drinks = int(input("Cost per person for drinks: "))
rent = input("Do you need to rent a venue? (yes or no) ").lower()
# 2.	Calculate:
# •	Food total (guests × food cost per person)
# •	Drink total (guests × drink cost per person)
food_total = num_guest * cost_per_person
drink_total = num_guest * cost_drinks
# •	Venue cost: $0 if they do not need a venue, $250.00 if they do
if rent == "yes": 
    venue_cost = 250.00
else:
    venue_cost = 0.00
# •	Grand total (food + drinks + venue)
grand_total = (food_total + drink_total + venue_cost)

# 3.	Print a formatted summary using f-strings with costs formatted to 2 decimal places:
print (f"--- Party Cost Summary ---")
print (f"Guests: {num_guest}")
print (f"Food total: ${food_total:.2f}")
print (f"Drink total: ${drink_total:.2f}")
print (f"Venue Cost: ${venue_cost:.2f}")
print (f"Grand total: ${grand_total:.2f}")

if grand_total > 500:
    print("Tip: Ask guests to bring a dish to reduce costs!")


