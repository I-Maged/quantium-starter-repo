#!/bin/bash

if [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
elif [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Virtual environment not found. Ensure 'venv' exists or update the script to match your environment path."
fi

python -m pytest test_app.py

TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "Tests failed. Please check the output above."
    exit 1
fi
