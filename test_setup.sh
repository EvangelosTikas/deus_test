#!/bin/bash

# Purpose of the script is to generate a local venv for running setup with test folder
# Replace the path with your python3 installation

echo "Creating python virtual environment"

python3 -m venv venv
##  or using python location (personalized)
#/tools/common/pkgs/pyenv/versions/3.8.13/bin/python3 -m venv venv

echo "Activating the venv"
source venv/bin/activate

echo "Installing python libraries"
pip install -r requirements.txt

echo "Running the python script"
pytest test_run/



echo "Deactivting the venv"
deactivate

exit

