# Write a program that calculates the cost of a road trip. The program should:
# 1. Ask the user for:
#    - Total distance in miles (a number)
#    - Vehicle fuel efficiency in miles per gallon (a number)
#    - Current gas price per gallon (a number)
#    - Whether they have a toll pass: yes or no (a string)
total_distance = float(input("What is the total distance in miles? "))
fuel_efficiency = float(input("What is the vehicle fuel efficiency in miles per gallon? "))
gas_price = float(input("what is the current gas price per gallon? "))
toll_pass = input("Do you have a toll pass? yes or no ").lower()

# 2. Calculate:
#    - Gallons of gas needed (distance / fuel efficiency)
#    - Gas cost (gallons * price per gallon)
#    - Toll cost: $0 if they have a toll pass, $15.00 if they do not
#    - Total trip cost (gas cost + toll cost)
gallons_needed = total_distance / fuel_efficiency
gas_cost = gallons_needed * gas_price
if toll_pass == "yes":
    toll_cost = 0
else:
    toll_cost = 15
total_trip_cost = (gas_cost + toll_cost)

# 3. Print a summary using f-strings with costs formatted to 2 decimal places:
#    --- Trip Cost Summary ---
#    Distance: 300 miles
#    Gas needed: 10.00 gallons
#    Gas cost: $35.00
#    Toll cost: $15.00
#    Total cost: $50.00
print(f"--- Trip Cost Summary ---\n"
      f"Distance: {total_distance:.2f} miles\n"
      f"Gas needed: {gallons_needed:.2f} gallons\n"
      f"Gas cost: ${gas_cost:.2f}\n"
      f"Toll cost: ${toll_cost:.2f}\n"
      f"Total cost: ${total_trip_cost:.2f}")
if total_trip_cost > 100:
    print("Consider carpooling to split the cost!")

# 4. If the total cost exceeds $100, print: "Consider carpooling to split the cost!"

# Constraints:
# - You must use at least one `if`/`else` (for the toll pass check)
# - You must use f-strings for all output
# - Your program should handle both "yes" and "Yes" and "YES" (case-insensitive)

