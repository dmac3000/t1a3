# Import the required libraries
from os import system
import math

# Prints a menu with four options and returns the selected option
def print_options():
    print("Welcome to the Carbulator! Select a menu option to continue...")
    print("1. Calculate my recommended daily carb intake")
    print("2. Track my weekly achieved carb intake")
    print("3. See my average achieved intake vs. my goal")
    print("4. Exit")
    opt = input("Select your option (1-3): ")
    return opt
option = ""

# Define a function to calculate carb intake
def calc_carb_intake(weight, height, age, gender, activity_level):
  global der
  # Check if the input values are valid
  if weight <= 0 or height <= 0 or age <= 0:
    # If any of the input values are not valid, raise an error
    raise ValueError("Invalid input values. Weight, height, and age must be positive numbers.")

#   # Calculate the body mass index (BMI) using the formula:
#   # BMI = weight (kg) / height^2 (m^2)
#   bmi = weight / math.pow(height, 2)

  # Calculate the basal metabolic rate (BMR) using the formula:
  # BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age (years) + s
  # where s is the value of 5 for males and -161 for females
  if gender == "male":
    s = 5
  elif gender == "female":
    s = -161
  else:
    # If the gender is not male or female, raise an error
    raise ValueError("Gender must be either male or female for the purposes of this app.")

#  Calculate BMR using the Mifflin-St Jeor Equation:
  bmr = 10 * weight + 6.25 * height - 5 * age + s
  
  # Calculate the daily energy requirement (DER) using the formula:
  # DER = BMR * activity_level
  # where activity_level is the value of 1.2 for sedentary, 1.375 for lightly active, 1.55 for moderately active, and 1.725 for very active

  if activity_level == "1":
    der = bmr * 1.2
  elif activity_level == "2":
    der = bmr * 1.375
  elif activity_level == "3":
    der = bmr * 1.55
  elif activity_level == "4":
    der = bmr * 1.725
  else:
    # If the activity level is not valid, raise an error
    raise ValueError("Invalid activity level. Activity level must be sedentary, lightly active, moderately active, or very active.")

  # Calculate the daily carb intake using the formula:
  # Daily carb intake = der * 0.4 / 4 (kcal/day)
  daily_carb_intake = der * 0.4 / 4
  # Return the calculated value
  return daily_carb_intake

while option != "4":
  system('cls')
    # invoke print options and return the selected option
  option = print_options()
  system('cls')
  if option == "1":
     # Test the function by getting user input
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    age = int(input("Enter your age in years: "))
    gender = input("Enter your gender (male or female): ")
    activity_level = input("Enter your activity level - (1) Sedentary (2) Lightly active (3) Moderately active or (4) Very active: ")

      # Calculate and print the daily carb intake
    daily_carb_intake = calc_carb_intake(weight, height, age, gender, activity_level)
    with open("daily_carb_goal.txt", "w") as f:
      # Write the daily_carb_intake number to the file
      f.write(str(daily_carb_intake))   

    print("Your daily energy requirement is", der)
    print("Your recommended daily carb intake is: ", daily_carb_intake, "g/day")
    input("press Enter to continue...")
    system('cls')
    continue 