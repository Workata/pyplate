# run checks and potentialy fix them

echo "Run pre-commit checks"
pre-commit run --all-files

echo "Test with PyTest... (+ check coverage)"
coverage run -m pytest ./src/

echo "Report coverage..."
coverage report -m
