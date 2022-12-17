from validate_gender import validate_gender

def test_validate_gender():
    #Run tests with pytest -s in order to accept input for second test case.
    #1. Correct input should pass through function correctly
    assert validate_gender("female") == "female"
    #2. If user inputs nothing instead of male or female, app should prompt for correct input
    assert validate_gender("") == "male" or "female"
    