#!/bin/bash

# Set the PYTHONPATH to the project root (the directory containing models.py)
export PYTHONPATH=$(pwd)

echo "Running unit tests..."
pytest tests/test_unit.py

echo "Running integration tests..."
pytest tests/test_integration.py

echo "Running end-to-end tests..."
pytest tests/test_e2e.py
