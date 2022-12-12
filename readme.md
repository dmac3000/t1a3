# David McArthur T1A3 - Terminal App Documentation

## R1 Answers to all the documentation requirements below
  
## R2 Your README.md should have a separate heading for each documentation requirement and answers organised under the appropriate headings.
  
## R3 Provide full attribution to referenced sources (where applicable)

Formula for calculating BMR: https://www.calculator.net/bmr-calculator.html

## R4 Provide a link to your source control repository

## R5 Identify any code style guide or styling conventions that the application will adhere to. Reference the chosen style guide appropriately.

## R6 Develop a list of features that will be included in the application

### Menu

This menu allows the user to navigate the app with 3 menu options and an exit app function. It also clears the screen after completing a feature.

### Feature 1. Calculate recommended carb intake based on a range of inputs

Feature 1 is a function that will get users input (weight, height, age, gender, activity level) and output a recommended daily carb intake via two formulas

The first formula is based on the Mifflin-St Jeor Equation for calculating basal metabolic rate (BMR).
https://reference.medscape.com/calculator/846/mifflin-st-jeor-equation

```py
bmr = 10 * weight + 6.25 * height - 5 * age + s
```

The above formula outputs the users basal metabolic rate in calories, which is the minimum amount of calories required for a person with those characteristics to function. We then take that information and run it through another formula as a multiplier for activity level. This formula uses conditional statements to determine which formula to run based the activity level the user has input.

```py
  if activity_level == "1":
    der = bmr * 1.2
  elif activity_level == "2":
    der = bmr * 1.375
  elif activity_level == "3":
    der = bmr * 1.55
  elif activity_level == "4":
    der = bmr * 1.725
```

The last formula takes the daily energy requirement abd runs it through a formula for calculating carb intake.
  
```py
  daily_carb_intake = der * 0.4 / 4
```
All of the above is wrapped up in a function called calc_carb_intake.

Once this function is defined, the program asks the user for their input, calls the function to crunch the formulas, then returns the data in the variable "daily_carb_intake" and writes it to a text file "daily_carb_goal.txt" as per the following:

```py
while option != "4":
  system('cls')
    # Call function print options and return the selected option
  option = print_options()
  system('cls')
  if option == "1":
    # Get user input
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    age = int(input("Enter your age in years: "))
    gender = input("Enter your gender (male or female): ")
    activity_level = input("Enter your activity level - (1) Sedentary (2) Lightly active (3) Moderately active or (4) Very active: ")

    # Calculate and print the daily carb intake based on above user input
    daily_carb_intake = calc_carb_intake(weight, height, age, gender, activity_level)
    # Write the daily_carb_intake number to the file, then close it 
    with open("daily_carb_goal.txt", "w") as f:
      f.write(str(daily_carb_intake))   
    # Output details for user to show function has executed correctly
    print("Your daily energy requirement is", der)
    print("Your recommended daily carb intake is: ", daily_carb_intake, "g/day")
    input("press Enter to continue...")
    system('cls')
    continue
```

### Feature 2. Record and save actual daily carbs

This feature allows a user to record their most recent 7 days worth of carb intake. Firstly it defines a list (carbs_consumed) to store the information, then uses a for loop that iterates 7 times to get users daily data from the past week (7 days). Each input is then appended to the list, then each item in the list is saved to the text file carb_intake.txt.

```py
elif option == "2":
      # access function to track weekly intake, create new file for weekly intake.
      # def get_carb_intake():
      # Initialize an empty list to store the carb intake for each day
      carbs_consumed = []
    
        # Ask the user for their carb intake for each of the previous 7 days
      for i in range(7):
          # Prompt the user to enter their carb intake for a day
        intake = input(f"Enter your carb intake for day {i+1}: ")
        
        # Add the intake to the list
        carbs_consumed.append(intake)
    
        # Open a file in write mode
      with open("carb_intake.txt", "w") as f:
          # Write the carb intake for each day to the file, one day per line
        for intake in carbs_consumed:
          f.write(str(intake) + "\n")
```

### Feature 3. Report weekly intake compared to recommended/goal

This feature takes the text files from the previous two features, and compares the output of the text file from Feature 1 (daily_carb_goals), compares it with the sum of all the lines in the text file from feature 2 (carb_intake.txt) and returns a message based on whether the value is lower or higher. If Feature 1 or Feature 2 have not been completed yet, it returns a message telling the user to go back and complete options 1 and 2. it does this by catching any FileNotFound exceptions and printing an error message if that exception is raised.

Note: Ensure that your features above allow you to demonstrate your understanding of the following language elements and concepts:

- use of variables and the concept of variable scope
- loops and conditional control structures

## R7 Develop an implementation plan which

- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

    Utilise a suitable project management platform to track this implementation plan.

    Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan.
    Your checklists for each feature should have at least 5 items.

## R8 Design help documentation which includes a set of instructions which accurately describe how to use and install the application

You must include:

- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application