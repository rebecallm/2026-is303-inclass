"""
Rebeca Llontop 
IS 303 - In Class Exercise

Inputs: 
- Student Name 
- Grade for three classes (Math, Science, English)
- Credits for three classes

Process:
- Calculate the GPA using the grades and the credit total 

Outputs:
- GPA 
- Report card for student
"""
# INPUTS
name = input("Student name: ")
grade1 = int(input("Course 1 grade point: "))
grade2 = int(input("Course 2 grade point: "))
grade3 = int(input("Course 3 grade point: "))
credit1 = int(input("Course 1 credis: "))
credit2 = int(input("Course 2 credis: "))
credit3 = int(input("Course 3 credis: "))

# PROCESSES
total_credits = credit1 + credit2 + credit3
gpa = (grade1*credit1 + grade2*credit2 + grade3*credit3) / total_credits

# OUTPUT

print(f"{name}'s Report Card")
print(f"Credits taken: {total_credits}")
print(f"Course 1: {grade1} credits: {credit1}\n"
      f"Course 2: {grade2} credits: {credit2}\n"
      f"Course 3: {grade3} credits: {credit3}")
print(f"GPA: {gpa}")