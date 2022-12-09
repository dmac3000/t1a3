from carbulator import print_options
from io import StringIO
import sys

def test_print_options(capsys):
    # Test that the function prints the expected menu options
    print_options()
    captured_output = capsys.readouterr()
    assert captured_output.out == "Welcome to the Carbulator! Select a menu option to continue...\n1. Calculate my recommended daily carb intake\n2. Track my weekly achieved carb intake\n3. See my achieved intake vs. my goal\n4. Exit\n"
    