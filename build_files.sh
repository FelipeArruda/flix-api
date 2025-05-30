#!/bin/bash

echo "Upgrading pip..."
python3.9 -m pip install --upgrade pip

# Build the project
echo "Building the project..."
python3.9 -m pip install -r requirements.txt

echo "Collect Static..."
python3.9 manage.py collectstatic --noinput --clear

echo "Make Migration..."
python3.9 manage.py makemigrations
python3.9 manage.py migrate