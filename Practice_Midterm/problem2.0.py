
workout_logs = int(input("How many workouts have you done this week? "))
logs= []
for i in range(workout_logs):
    activity = input("What activity did you do? ").lower()
    duration = int(input("How long was the activity in muntes? "))
    outdoors = input("Was it outdoors? yes/no ").lower().strip()
    if outdoors == "yes":
        outdoors = True 
    elif outdoors == "no":
        outdoors = False 
    logs.append({
        "activity": activity, "duration": duration, "outdoors": outdoors
    })

total_duration = 0 
longest_duration = 0 
longest_activity = ""
for log in logs: 
    total_duration += log["duration"]
    if log["duration"] > longest_duration: 
        longest_duration = log["duration"]
        longest_activity = log["activity"].capitalize()
outdoors_yes = []
for log in logs: 
    if log["outdoors"] == True:
        outdoors_yes.append(log["activity"])

print    (f"--- Weekly Workout Summary ---\n"
          f"Total minutes: {total_duration}\n"
          f"Longest workout: {longest_activity} ({longest_duration} minutes)")
if not outdoors_yes:
    print("No outdoor workout this week")
else: 
    print(f"Outdoor workouts: {','.join(outdoors_yes)}")
