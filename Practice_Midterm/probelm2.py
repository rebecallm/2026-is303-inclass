# A personal trainer needs a weekly workout summary. Write a program that:

# 1.	Ask the user how many workouts to log (a number)
# 2.	For each workout, ask for:
# •	Activity name (a string) — e.g., Running, Swimming, Yoga
# •	Duration in minutes (a number)
# •	Whether it was outdoors: yes or no (a string)
num_workout = int(input("How many weekly workouts? "))
logs = []
for i in range(num_workout):
    activity = input("Activity name: ")
    duration = int(input("Duration in minutes: "))
    outdoors = input("Was it outdoors? (yes or no) ").lower()
    if outdoors == "yes":
        outdoors = True
    else:        outdoors = False
    logs_dict = {"activity": activity, "minutes": duration, 
                 "outdoor": outdoors}
# 3.	Store each workout as a dictionary in a list. Each dictionary 
# should have keys: "activity", "minutes", and "outdoor" (True or False)
    logs.append(logs_dict)

# 4.	After all workouts are entered, calculate and display:

# Total minutes (sum of all workout durations). Use the accumulator pattern.
# Longest workout (the activity name and duration of the longest single 
# workout). Use the min/max pattern. If no workouts were entered, print "No workouts logged."
# Outdoor workouts (a list of activity names that were done outdoors). Use the filter pattern. If none were outdoors, print "No outdoor workouts this week."
total_minutes = 0
longest_workout = 0 
for log in logs:
    total_minutes += log["minutes"]
    if log["minutes"] > longest_workout:
        longest_workout = log["minutes"]
        print(log["activity"], longest_workout)
outdoor_workouts = []
for log in logs:
    if log["outdoor"]:
        outdoor_workouts.append(log["activity"])
if len(outdoor_workouts) == 0:
    print("No outdoor workouts this week.")

# 5.	Print a formatted summary:
# --- Weekly Workout Summary ---
# Total minutes: 245
# Longest workout: Swimming (60 min)
# Outdoor workouts: Running, Cycling

# Constraints
# •	You must use a for loop to process the list
# •	You must store data in a list of dictionaries
# •	You must use at least two named loop patterns (accumulator, min/max, or filter)
 
 
 