from carbulator import print_options

def test_print_options():
    # Call the function and save the selected option
    option = print_options()

    # Check if the selected option is returned correctly
    assert option == 1