from validate_inputs import validate_inputs

def test_validate_inputs():
    #1. Correct input should pass through function correctly
    assert validate_inputs("10") == "10"
    #2. Input negative number should prompt user to input again? Enter pos number to complete
    assert validate_inputs("-10") == "Invalid input. Please enter a positive number: "
    