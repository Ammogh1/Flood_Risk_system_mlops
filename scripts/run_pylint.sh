#!/bin/bash

# Ensure we are in the project root
cd "$(dirname "$0")/.." || exit

echo "Running PyLint on src/ and tests/..."
python -m pylint --rcfile=.pylintrc src/ tests/

echo "Linting complete!"
