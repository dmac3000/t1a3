def validate_gender(gender):
    while gender != "male" and gender != "female":
        gender = input("Invalid input. Please enter your gender as male or female for the purposes of this app: ")
        if gender == "male" or gender == " female":
            continue
    return (gender)