from carbulator import validate_inputs

def test_validate_inputs():
    result = validate_inputs(-1)
    assert result == "Invalid input. Please enter a positive number: "