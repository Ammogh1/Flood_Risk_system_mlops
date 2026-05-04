# Ensure we are in the project root
Set-Location -Path "$PSScriptRoot\.."

Write-Host "Running PyLint on src/ and tests/..."
python -m pylint --rcfile=.pylintrc src/ tests/

Write-Host "Linting complete!"
