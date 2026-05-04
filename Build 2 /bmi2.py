"""
Calculate BMI (Body Mass Index)

Inputs:
- name 
- height 
- weight 
- age 
- sex 

Processes: 
- Input Validation 
- Calculate BMI - weight / height^2 * 703
- Categorize BMI 
 - underwight <18.5
 - healthy 18.5-24.9
 - overweight 25.0-29.9
 - obesity 30.0-39.9
 - severe obesity 40+

Outputs: 
- Report for an individual 

"""

#COLELCT INPUTS
name = input("Name: ")
age = input("Age: ")
sex = input("Sex: ")
height = input("Height (inches): ")
weight = input("Weight (pounds): ")

#INPUT VALIDATION 
age = age.replace(".","",1)
age_is_int = age.isdigit() 
if age_is_int == True:
    age = int(age)
age_is_reasonable = False  
if age_is_int == True and age < 140 and age > 1:
    age_is_reasonable = True

sex = sex.lower()
sex_is_valid = False
if sex == "male" or sex == "female":
    sex_is_valid = True 

height = height.replace(".","",1)
height_is_int = height.isdigit()
if height_is_int == True:
    height = int(height)
height_is_reasonable = False
if height_is_int == True and height > 12 and height < 140:
    height_is_reasonable = True

weight = weight.replace(".","",1)
weight_is_int = weight.isdigit()
if weight_is_int == True:
    weight = int(weight)
weight_is_reasonable = False
if weight_is_int == True and weight > 12 and weight < 1200:
    weight_is_reasonable = True

ready_to_process = True

if age_is_int == False or age_is_reasonable == False:
    print("You enetered a non-expected age, please use whole numbers") 
    ready_to_process = False

if sex_is_valid == False:
    print("You enetered a non-expected sex. Please enter male or female")
    ready_to_process = False

if height_is_int == False or height_is_reasonable == False:
    print("You enetered a non-expected height. Please use whole numbers between 12 and 140 inches.")
    ready_to_process = False

if weight_is_int == False or weight_is_reasonable == False:
    print("You enetered a non-expected weight in pounds. Please use whole numbers between 12 and 1200 pounds.")
    ready_to_process = False

#PROCESSES
if ready_to_process == True:
    bmi = (weight / height**2) * 703
    bmi_category = ""
    if bmi < 18.5:
        bmi_category = "underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        bmi_category = "healthy"
    elif bmi >=25.0 and bmi <=29.9:
        bmi_category = "overweight"
    elif bmi >=30.0 and bmi <=39.9:
        bmi_category = "obesity"
    elif bmi >= 40:
        bmi_category = "severe obesity" 

#OUTPUTS
    print(f"Report for {name}\n"
      f"{age} years old {sex}\n"
      f"Your BMI is {bmi:.2f}\n"
      f"Your BMI category is {bmi_category}\n")
