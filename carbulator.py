# Import the required libraries
import time
from os import name, system
from datetime import datetime
from validate_inputs import validate_inputs
from validate_activity_levels import validate_activity_levels
from validate_gender import validate_gender


def day_react():
  global current_day
  current_day = datetime.now().strftime("%A")
  return current_day

# Prints a menu with four options and returns the selected option
def print_options():
  if day_react() != "Monday":
    print(f"Welcome to the Carbulator. Happy {day_react()}! Enter a menu option to continue...")
  else:
    print(f"Welcome to the Carbulator. Hope you're surviving {day_react()}! Enter a menu option to continue...")
  print("1. Calculate my recommended daily carb intake")
  print("2. Track my weekly achieved carb intake")
  print("3. See my average achieved intake vs. my goal")
  print("4. Exit")
  opt = input("Select an option (1-4): ")
  return opt
option = ""

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
    print('Unable to clear the screen on your operating system.')

# Function that calculates carb intake
def calc_carb_intake(weight, height, age, gender, activity_level):
  global der

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
  # where activity_level is the value of 1.2 for sedentary, 1.375 for lightly active, 
  # 1.55 for moderately active, and 1.725 for very active

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
    # Run Feature 1: Get user input
    weight = input("Enter your weight in kilograms (kg): ")
    weight = validate_inputs(weight)
    height = input("Enter your height in centimetres (cm): ")
    height = validate_inputs(height)
    age = input("Enter your age in years: ")
    age = validate_inputs(age)
    gender = input("Enter your gender (male or female): ")
    gender = validate_gender(gender)
    activity_level = input("Enter your activity level - (1) sedentary (2) lightly active (3) moderately active or (4) very active: ")
    activity_level = validate_activity_levels(activity_level)

    # Calculate and print the daily carb intake based on above user input
    daily_carb_intake = calc_carb_intake(weight, height, age, gender, activity_level)
    # der = calc_carb_intake(der)
    # s = calc_carb_intake(s)
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
      # Get user input to track weekly intake, create new file for weekly intake.
      carbs_consumed = []
    
        # Ask the user for their carb intake for each of the previous 7 days
      for i in range(7):
        intake = input(f"Enter your carb intake for day {i+1}: ")
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
      print(f" You entered: {carbs_consumed}")
      
  elif option == "3":
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
      print("Invalid input, please select 1, 2, 3 or 4.")
    #adds a break in the control flow until the user presses Enter.
  input("press Enter to continue...")
  clear_screen()

print("Goodbye!") 
#Keep app open long enough for user to read "Goodbye!" message before closing
time.sleep(5)