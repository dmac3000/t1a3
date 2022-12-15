from validate_inputs import validate_inputs

def test_validate_inputs():
    assert validate_inputs("10") == "10"
    # assert validate_inputs("") == "Invalid input. Please enter a positive number: "
    # assert validate_inputs("-10") == "Invalid input. Please enter a positive number: "
    # assert validate_inputs("hello") == "Invalid input. Please enter a positive number: "