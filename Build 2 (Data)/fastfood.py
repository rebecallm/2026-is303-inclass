name = input("what is your name? ")
classes = input("what classes are you in? science/math/english: ")
grade = input("what are the grades for those classes? A/B/C/D/F: ")
grade = int(grade)
if grade >= 90:
    grade = "Good Job"
elif grade >= 80:
    grade = "Not Bad"
elif grade >= 70:
    grade = "You can do better"
elif grade >= 60:
    grade = "You need to work harder"
else:
    grade = "You need to get your act together"
print(F"Hello {name}, you are in {classes} and your grades are {grade}.")

