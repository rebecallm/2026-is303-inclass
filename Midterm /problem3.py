# A university club is hosting an event and needs a registration system. Write a program that:

# 1. Ask for the event name (a string)
event_name = input("What is the name of the event? ")
attendees =[]
register_yes = "yes"
while register_yes == "yes": 
    full_name = input("What is your full name? ").capitalize()
    email_address = input("What is your email address? ").lower().strip()
    role = input("Are you a member or guest? ").lower
    if role == "member":
        is_member = True 
    else: 
        is_member = False 

    register_yes = input("Register another? (yes/no)")
    attendees.append({
        "name":full_name, "email": email_address, "role": role
    })
# 5. Store each attendee as a dictionary in a list with keys: "name", "email", "role"
number_members = 0 
number_guests = 0 
total_attendees = 0 
for attendee in attendees: 
    total_attendees += len(attendees)
    number_members += is_member
    number_guests -= is_member

print(f"--- Registration Report: Python Workshop ---\n"
      f"Total attendees: {total_attendees}\n"
      f"Members: {number_members}\n"
      f"Guests: {number_guests}\n")
for attendee in attendees:
    counter= 1 
    print (f"Attendee list:\n"
           f"{counter}. {attendees[0]['name']}")
    counter += 1 

#    Attendee List:
#    1. Alice Chen (member)
#    2. Bob Smith (guest)
#    3. Carol Jones (guest)
#    4. David Lee (guest)
# Consider a membership drive!")

# 6. After registration closes, produce a report:
#    - Total number of attendees
#    - Number of members and number of guests (use an accumulator or counter)
#    - A list of all attendee names, numbered (use a for loop with the index)
#    - If there are more guests than members, print: "Consider a membership drive!"

#    Example output:
#    --- Registration Report: Python Workshop ---
#    Total attendees: 4
#    Members: 1
#    Guests: 3

#    Attendee List:
#    1. Alice Chen (member)
#    2. Bob Smith (guest)
#    3. Carol Jones (guest)
#    4. David Lee (guest)
# Consider a membership drive!


# Constraints:
# - You must use a while loop for the registration process (not a for loop with a fixed count)
# - You must use string methods to clean the data (title case, lowercase, strip)
# - You must use a list of dictionaries to store attendees
# - You must use at least one loop pattern (accumulator or counter) for the member/guest counts
# - You must use a conditional for the membership drive messag
