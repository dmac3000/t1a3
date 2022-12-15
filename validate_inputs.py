def validate_inputs(checknum):
  while checknum == '' or not checknum.isnumeric() or int(checknum) <= 0:
    checknum = input("Invalid input. Please enter a positive number: ")
  return checknum