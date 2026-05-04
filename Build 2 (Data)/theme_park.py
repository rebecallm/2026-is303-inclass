"""
Theme Park 

Inputs: 
- age 
- day of the week
- height
- VIP 
- Signed waiver
- parent present

Process:
- Use the variables to identify which rides are avilable for the person to go on

Outputs:
- A list of rides the person can go on
"""

# INPUTS
age = int(input("Age: "))
day_of_week = input("Day of week: ")
height = int(input("Height in inches: "))
vip = input("VIP? yes/no: ").lower()
signed_waiver = input("Signed waiver? yes/no: ").lower()
parent_present = input("Parent present? yes/no: ").lower() 

#PROCESSES & OUTPUTS
# 1.1 MEGADROP
if age >=14 and signed_waiver == "yes":
    if height >= 54:
        print("MegaDrop")
    elif vip == "yes" and height >= 50:
        print("MegaDrop")
# 1.2 THUNDERBOLT 
if age >= 10 and height >= 48 and day_of_week != "monday":
    print("Thunderbolt")
# 1.3 KDDIE COASTER
if age >= 8 or parent_present == "yes":
    print("Kiddie Coaster")
else:
    print("Sorry, you do not meet the requirements for any rides")
