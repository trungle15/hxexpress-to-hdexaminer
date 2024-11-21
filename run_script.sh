#!/bin/bash

# Ensure the script runs in its directory
cd "$(dirname "$0")"

# Activate the virtual environment
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "Virtual environment activated."
else
    echo "Error: Virtual environment '.venv' not found."
    exit 1
fi

# Run the Python script
if [ -f "script.py" ]; then
    python script.py
    echo "Script executed successfully."
else
    echo "Error: script.py not found in the directory."
    deactivate
    exit 1
fi

# Deactivate the virtual environment
deactivate
echo "Virtual environment deactivated."
