#!/bin/bash

# Try running the script using the python executable
python carbulator.py

# If the above command failed, try running the script using the python3 executable
if [ $? -ne 0 ]; then
  python3 carbulator.py
fi