def validate_activity_levels(activity_level):
    valid_activity_levels = ["1","2","3","4"]
    while activity_level not in valid_activity_levels:
        activity_level = input("Invalid input. Please enter (1) for sedentary, (2) for lightly active (3) for moderately active or (4) for very active: ")
        if activity_level in valid_activity_levels:
            continue
    return activity_level
