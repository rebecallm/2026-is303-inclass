# A personal trainer needs a weekly workout summary. Write a program that:

# •	Activity name (a string) — e.g., Running, Swimming, Yoga
# •	Duration in minutes (a number)
# •	Whether it was outdoors: yes or no (a string)
num_workouts = int(input("How many workouts? "))
logs = []
for i in range(num_workouts): 
    activity = input("What workout? ").lower().strip()
    minutes = float(input("How long in mnutes? "))
    outdoor = input("Was it outdoors? ").lower()
    if outdoor == "yes":
        outdoor = True 
    elif outdoor == "no":
        outdoor = False 
# 3.	Store each workout as a dictionary in a list. 
# Each dictionary should have keys: "activity", "minutes", and "outdoor" (True or False)
    logs.append({
        "activity": activity, "minutes": minutes, "outdoor": outdoor
    })

# 4.	After all workouts are entered, calculate and display:
# Total minutes (sum of all workout durations). Use the accumulator pattern.
# Longest workout (the activity name and duration of the longest single workout). Use the min/max pattern. If no workouts were entered, print "No workouts logged."
# Outdoor workouts (a list of activity names that were done outdoors). Use the filter pattern. If none were outdoors, print "No outdoor workouts this week."
total_minutes = 0 
longest_workout = 0
longest_activity = ""
for log in logs:
    total_minutes += log["minutes"]
    if log["minutes"] > longest_workout: 
        longest_workout = log["minutes"]
        longest_activity = log["activity"].capitalize()
if  num_workouts == 0: 
    print("No workouts logged")
outdoor_yes = []
for log in logs: 
    if log["outdoor"] == True:
        outdoor_yes.append(log["activity"])

print(f"--- Weekly Workout Summary ---\n"
      f"Total minutes: {total_minutes}\n"
      f"Longest workout: {longest_activity} ({longest_workout} min)")
if not outdoor_yes: 
    print("No outdoor workouts this week.")
else: 
    print(f"Outdoor workouts: {', '.join(outdoor_yes).capitalize()}")


# 5.	Print a formatted summary:
# --- Weekly Workout Summary ---
# Total minutes: 245
# Longest workout: Swimming (60 min)
# Outdoor workouts: Running, Cycling

# Constraints
# •	You must use a for loop to process the list
# •	You must store data in a list of dictionaries
# •	You must use at least two named loop patterns (accumulator, min/max, or filter)

# Example Run
# How many workouts to log? 3
# Workout 1 - Activity: Running
# Workout 1 - Duration (minutes): 45
# Workout 1 - Outdoors? (yes/no): yes
# Workout 2 - Activity: Yoga
# Workout 2 - Duration (minutes): 30
# Workout 2 - Outdoors? (yes/no): no
# Workout 3 - Activity: Cycling
# Workout 3 - Duration (minutes): 60
# Workout 3 - Outdoors? (yes/no): yes

# --- Weekly Workout Summary ---
# Total minutes: 135
# Longest workout: Cycling (60 min)
# Outdoor workouts: Running, Cycling
