# Prints a menu with four options and returns the selected option
def print_options():
    print("Welcome to the Carbulator! Select a menu option to continue...")
    print("1. Calculate my recommended daily carb intake")
    print("2. Track my weekly achieved carb intake")
    print("3. See my achieved intake vs. my goal")
    print("4. Exit")
    opt = input("Select your option (1-3): ")
    return opt
option = ""