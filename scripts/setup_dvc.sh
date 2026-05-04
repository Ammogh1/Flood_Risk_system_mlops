#!/bin/bash

# Ensure we are in the project root
cd "$(dirname "$0")/.." || exit

# Initialize DVC if not already initialized
if [ ! -d ".dvc" ]; then
    echo "Initializing DVC..."
    dvc init
else
    echo "DVC is already initialized."
fi

# Make sure data directory exists
mkdir -p data
mkdir -p models

# Add data to DVC
echo "Tracking data/ directory with DVC..."
dvc add data/

# Track models directory
echo "Tracking models/ directory with DVC..."
dvc add models/

# Add DVC files to git
echo "Adding DVC tracking files to Git..."
git add data.dvc models.dvc .gitignore

echo "DVC setup complete. Remember to configure a remote (e.g., dvc remote add -d myremote s3://mybucket/dvcstore) if you want to push data."
