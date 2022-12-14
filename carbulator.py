# Import the required libraries
from os import name, system
import math
import random
import pprint as pp
from datetime import datetime

def day_react():
  global current_day
  current_day = datetime.now().strftime("%A")
  return current_day

# Prints a menu with four options and returns the selected option
def print_options():
  if day_react() != "Monday":
    print(f"Welcome to the Carbulator. Happy {day_react()}! Select a menu option and press Enter to continue...")
  else:
    print(f"Welcome to the Carbulator. Hope you're surviving {day_react()}! Select a menu option to continue...")
  print("1. Calculate my recommended daily carb intake")
  print("2. Track my weekly achieved carb intake")
  print("3. See my average achieved intake vs. my goal")
  print("4. Exit")
  opt = input("Select your option (1-3): ")
  return opt
option = ""

def validate_inputs(checknum):
  while checknum == '' or not checknum.isnumeric() or int(checknum) <= 0:
    checknum = input("Invalid input. Please enter a positive number: ")
  return checknum
    
#function for clearing screen depending on which OS the user is using
def clear_screen():
  # Get the current operating system
  os_name = name

  # Use the appropriate command to clear the screen
  if os_name == 'posix':
    system('clear')
  elif os_name == 'nt':
    system('cls')
  else:
    print('Sorry, I am not able to clear the screen on your operating system.')

# Function that calculates carb intake
def calc_carb_intake(weight, height, age, gender, activity_level):
  global der

  # Convert weight, height, and age to numeric values
  weight = int(weight)
  height = int(height)
  age = int(age)

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

# Main program logic
while option != "4":
  clear_screen()
    # invoke print options and return the selected option
  option = print_options()
  clear_screen()
  if option == "1":
    # Get user input
    weight = input("Enter your weight in kilograms (kg): ")
    weight = validate_inputs(weight)
    height = input("Enter your height in centimetres (cm): ")
    height = validate_inputs(height)
    age = input("Enter your age in years: ")
    age = validate_inputs(age)

    
    gender = input("Enter your gender (male or female): ")
    while gender != "male" and gender != "female":
      gender = input("Invalid input. Please enter your gender as male or female for the purposes of this app: ")
      if gender == "male" or gender == " female":
        continue
    valid_activity_levels = ["1","2","3","4"]
    activity_level = input("Enter your activity level - (1) sedentary (2) lightly active (3) moderately active or (4) very active: ")
    while activity_level not in valid_activity_levels:
      activity_level = input("Invalid input. Please enter (1) for sedentary, (2) for lightly active (3) for moderately active or (4) for very active: ")
      if activity_level in valid_activity_levels:
        continue

    # Calculate and print the daily carb intake based on above user input
    daily_carb_intake = calc_carb_intake(weight, height, age, gender, activity_level)
    # Write the daily_carb_intake number to the file, then close it 
    with open("daily_carb_goal.txt", "w") as f:
      f.write(str(daily_carb_intake))   
    # Output details for user to show function has executed correctly
    print("Your daily energy requirement is", int(der), "calories.")
    print("Your recommended daily carb intake is: ", int(daily_carb_intake), "g/day")
    input("press Enter to continue...")
    clear_screen()
    continue
  elif option == "2":
      # access function to track weekly intake, create new file for weekly intake.
      # Initialize an empty list to store the carb intake for each day
      carbs_consumed = []
    
        # Ask the user for their carb intake for each of the previous 7 days
      for i in range(7):
          # Prompt the user to enter their carb intake for a day
        intake = input(f"Enter your carb intake for day {i+1}: ")
        # Check if input is numeric
        while not intake.isnumeric():
          # Prompt user to enter again if input was not numeric
          intake = input("Please enter a valid number: ")
          # Add the intake to the list
        carbs_consumed.append(intake)
    
        # Open a file in write mode
      with open("carb_intake.txt", "w") as f:
          # Write the carb intake for each day to the file, one day per line
        for intake in carbs_consumed:
          f.write(str(intake) + "\n")
      pp.pprint(f" You entered: {carbs_consumed}")
  elif option == "3":
      # access function for comparing weekly achieved vs goal.open file, compare goal on line one with sum of all 7 lines in results file. return discrepancy

      # Try to open the daily_carb_goal.txt file in read mode
      try:
          with open("daily_carb_goal.txt", "r") as f:
              # Read the first line of the file and convert it to a float
              daily_carb_goal = float(f.readline())

          # Try to open the carb_intake.txt file in read mode
          try:
              with open("carb_intake.txt", "r") as f:
                  # Initialize a variable to store the sum of the carb intake for each day
                  total_carb_intake = 0

                  # Read each line of the file (corresponding to one day's carb intake)
                  for line in f:
                      # Convert the line to an integer and add it to the total
                      total_carb_intake += int(line)
              # Calculate the average carb intake for the week
              average_carb_intake = total_carb_intake / 7

              # Compare the total carb intake to the daily carb goal
              print(f"Your average daily carb intake for the week was {average_carb_intake:.2f}, vs your goal of {daily_carb_goal:.2f}.")
          except FileNotFoundError:
              print("No carb intake data has been found. Please return to the menu and ensure option 2 is completed.")
      except FileNotFoundError:
          print("No daily carb goal data has been found. Please return to the menu and ensure option 1 is completed.")
  elif option == "4":
      continue
  else:
      print("Invalid option")
    #adds a break in the control flow until the user presses Enter    
  input("press Enter to continue...")
  clear_screen()

# delete the results.txt file enabling the next user to start fresh???
print("Goodbye!") 