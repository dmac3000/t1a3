from validate_gender import validate_gender

def test_validate_gender():
    assert validate_gender("female") == "female"
    # assert validate_inputs("") == "Invalid input. Please enter a positive number: "
    # assert validate_gender("-10") == "Invalid input. Please enter your gender as male or female for the purposes of this app:"
    # assert validate_inputs("hello") == "Invalid input. Please enter a positive number: "